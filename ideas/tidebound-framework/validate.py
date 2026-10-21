"""Validate framework structure and claims metadata. Does not assess game aesthetics."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parent
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

def read_json(name):
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        errors.append(f"{name}: {exc}")
        return {}

def unique(rows, label):
    ids = [row.get("id") for row in rows]
    require(all(isinstance(x, str) and x for x in ids), f"{label}: empty ID")
    require(len(set(ids)) == len(ids), f"{label}: duplicate ID")
    return set(ids)

manifest = read_json("manifest.json")
version = manifest.get("version")
require(bool(version), "manifest: version is required")
listed = manifest.get("files", [])
require(len(listed) == len(set(listed)), "manifest: duplicate file")
for name in listed:
    require((ROOT / name).is_file(), f"manifest: missing {name}")
actual = {p.name for p in ROOT.iterdir() if p.is_file()}
require(actual == set(listed), f"manifest mismatch: missing={set(listed)-actual}; unlisted={actual-set(listed)}")
require(manifest.get("runtime_changed") is False, "This documentation release must not claim runtime changes")

json_names = ["rules.json", "references.json", "parameters.json", "baselines.json", "scenarios.json"]
data = {}
for name in json_names:
    data[name] = read_json(name)
    require(data[name].get("framework_version") == version, f"{name}: version mismatch")

rules = data["rules.json"].get("rules", [])
scenarios = data["scenarios.json"].get("scenarios", [])
references = data["references.json"].get("references", [])
params = data["parameters.json"].get("parameters", [])
baselines = data["baselines.json"].get("baselines", [])
rule_ids = unique(rules, "rules")
scenario_ids = unique(scenarios, "scenarios")
ref_ids = unique(references, "references")
unique(params, "parameters")
unique(baselines, "baselines")

anchors = {}
texts = {}
for path in ROOT.glob("*.md"):
    body = path.read_text(encoding="utf-8-sig")
    texts[path.name] = body
    for anchor in re.findall(r'<a id="([^"]+)"></a>', body):
        require(anchor not in anchors, f"Duplicate anchor: {anchor}")
        anchors[anchor] = path.name
    # Framework is portable; all local Markdown links must stay in this directory.
    for target in re.findall(r'\]\(([^)]+)\)', body):
        if "://" in target or target.startswith("mailto:"):
            continue
        target = target.strip("<>")
        name, _, fragment = target.partition("#")
        destination = path.parent / name if name else path
        require(destination.is_file(), f"{path.name}: broken link {target}")
        require(destination.resolve().is_relative_to(ROOT), f"{path.name}: nonportable link {target}")
        if fragment and destination.is_file():
            other = destination.read_text(encoding="utf-8-sig")
            require(f'<a id="{fragment}"></a>' in other, f"{path.name}: missing explicit anchor {target}")
    require(not re.search(r'[A-Za-z]:[\\/](?:Users|video|work)', body, re.I),
            f"{path.name}: local machine path in portable document")
    mentioned = set(re.findall(r'\b(?:GOV|ART|WORLD|MOTION|FX|PLAY|UI|ENG|QA|PROC)-\d{2}\b', body))
    require(mentioned <= rule_ids, f"{path.name}: unknown rules {mentioned-rule_ids}")

require(rule_ids == set(anchors), f"Rule/anchor mismatch: {rule_ids ^ set(anchors)}")
for row in rules:
    key = row.get("id")
    require(row.get("anchor") == key, f"{key}: anchor mismatch")
    require(anchors.get(key) == row.get("owner_file"), f"{key}: owner mismatch")
    require(bool(row.get("scenarios")), f"{key}: no verification scenarios")
    require(set(row.get("scenarios", [])) <= scenario_ids, f"{key}: unknown scenarios")

for row in scenarios:
    require(row.get("status") in {"not_run", "passed", "failed", "blocked"}, f"{row.get('id')}: invalid status")
    require(bool(row.get("procedure")) and bool(row.get("expected")), f"{row.get('id')}: missing procedure/expected")
    if row.get("status") == "passed":
        require(bool(row.get("evidence")), f"{row.get('id')}: pass without evidence")
    for evidence in row.get("evidence", []):
        require(bool(evidence.get("kind")) and bool(evidence.get("scope")), f"{row.get('id')}: incomplete evidence")
        if "path" in evidence:
            require((ROOT / evidence["path"]).is_file(), f"{row.get('id')}: missing evidence file")
        if "command" in evidence:
            require(evidence.get("exit_code") == 0, f"{row.get('id')}: successful command evidence needs exit_code 0")

for row in params:
    status = row.get("status")
    require(status in {"pending_calibration", "existing_observation", "calibrated", "deprecated"},
            f"{row.get('id')}: invalid parameter state")
    if status in {"pending_calibration", "existing_observation"}:
        require(row.get("target_value") is None, f"{row.get('id')}: uncalibrated target value")
    if status == "pending_calibration":
        require(bool(row.get("method")) and bool(row.get("decision_due")), f"{row.get('id')}: no calibration route")
    if status == "calibrated":
        require(row.get("target_value") is not None and bool(row.get("evidence")) and bool(row.get("decision")),
                f"{row.get('id')}: calibrated parameter lacks evidence/decision/value")

for row in baselines:
    require(row.get("reference_id") in ref_ids, f"{row.get('id')}: unknown reference")
    require(row.get("status") in {"pending_capture_and_review", "captured_pending_review", "accepted", "rejected"},
            f"{row.get('id')}: invalid baseline status")
    if row.get("formal_acceptance"):
        require(row.get("status") == "accepted" and bool(row.get("evidence")) and bool(row.get("reviewer"))
                and bool(row.get("reviewed_on")) and bool(row.get("capture_commit"))
                and bool(row.get("capture_configuration")), f"{row.get('id')}: acceptance without full evidence")
    if row.get("status") == "accepted":
        require(row.get("formal_acceptance") is True, f"{row.get('id')}: inconsistent acceptance")

for row in references:
    if row.get("media_file"):
        require(bool(re.fullmatch(r"[0-9a-f]{64}", row.get("sha256", ""))), f"{row.get('id')}: invalid SHA-256")
        require(row.get("license_status") == "unknown; analysis only", f"{row.get('id')}: unverified video license changed")
        for segment in row.get("segments", []):
            require(0 <= segment["start"] < segment["end"] <= row["duration_seconds"],
                    f"{row.get('id')}: invalid segment")
    require(bool(row.get("license_status")), f"{row.get('id')}: missing licensing state")

chinese_chars = sum(len(re.findall(r"[\u4e00-\u9fff]", value)) for value in texts.values())
if errors:
    print("FAIL")
    for error in errors:
        print("- " + error)
    sys.exit(1)
print(json.dumps({
    "result": "PASS", "scope": "documentation structure and metadata only",
    "version": version, "markdown_files": len(texts), "chinese_characters": chinese_chars,
    "rules": len(rules), "scenarios": len(scenarios), "parameters": len(params),
    "formal_visual_baselines_accepted": sum(bool(x.get("formal_acceptance")) for x in baselines)
}, ensure_ascii=False, indent=2))

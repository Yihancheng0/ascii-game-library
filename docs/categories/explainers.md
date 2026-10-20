# 流程与图解 / Explainers

36 项。开发用途建议：教程、任务树、系统关系图。

[机器索引](../../catalog/ascii-magic/explainers.json) · [全部分类](../../README.md)

## Architecture Map · `architecture-map`

[原始预览](https://www.ascii-magic.com/ascii/architecture-map) · [源码](../../vendor/ascii-magic-art/pieces/architecture-map.js)

A system architecture map from clients through a CDN and load balancer to services and data stores, with requests flowing along every link.

关键词：云 / 加载 / 图解 / 地图 / 教学 / 流程。授权记录：MIT。

## Binary Search Steps · `binary-search-steps`

[原始预览](https://www.ascii-magic.com/ascii/binary-search-steps) · [源码](../../vendor/ascii-magic-art/pieces/binary-search-steps.js)

Binary search on a sorted array of twenty numbers, with lo, mid and hi pointers sliding into place, the discarded half greying out at every step and a log of each comparison until the target is found or proven missing.

关键词：图解 / 教学 / 流程 / 海 / 海洋。授权记录：MIT。

## Binary Search Tree · `binary-tree`

[原始预览](https://www.ascii-magic.com/ascii/binary-tree) · [源码](../../vendor/ascii-magic-art/pieces/binary-tree.js)

Values inserting into a binary search tree one by one, each comparison lighting the path down before the new node drops into place.

关键词：图解 / 教学 / 树木 / 流程 / 海 / 海洋。授权记录：MIT。

## Blue Green Switch · `blue-green-deploy`

[原始预览](https://www.ascii-magic.com/ascii/blue-green-deploy) · [源码](../../vendor/ascii-magic-art/pieces/blue-green-deploy.js)

A blue and green deployment where the idle environment boots the new release, passes its smoke tests, and the router flips every request across in one step while the old side drains and stands by.

关键词：图解 / 开机 / 教学 / 流程 / 烟 / 烟雾。授权记录：MIT。

## Canary Rollout Gates · `canary-rollout`

[原始预览](https://www.ascii-magic.com/ascii/canary-rollout) · [源码](../../vendor/ascii-magic-art/pieces/canary-rollout.js)

A canary release that moves traffic from 1 to 100 percent in steps while error rate and latency are compared against the stable build, promoting one release and automatically rolling back the next when its errors spike.

关键词：图解 / 失败 / 教学 / 流程 / 错误。授权记录：MIT。

## Edge Cache Hit Miss · `cdn-cache`

[原始预览](https://www.ascii-magic.com/ascii/cdn-cache) · [源码](../../vendor/ascii-magic-art/pieces/cdn-cache.js)

A CDN edge node where requests from three regions hit the cache and return fast, or miss and travel on to the origin, while every cached path counts down its TTL and expires.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## CI Pipeline · `ci-pipeline`

[原始预览](https://www.ascii-magic.com/ascii/ci-pipeline) · [源码](../../vendor/ascii-magic-art/pieces/ci-pipeline.js)

A CI pipeline where each run moves through checkout, install, lint, test, build and deploy, with spinners, timings, a live log and the odd failing test.

关键词：加载 / 图解 / 教学 / 流程。授权记录：MIT。

## Circuit Breaker States · `circuit-breaker`

[原始预览](https://www.ascii-magic.com/ascii/circuit-breaker) · [源码](../../vendor/ascii-magic-art/pieces/circuit-breaker.js)

A circuit breaker that counts failures from a struggling downstream service, trips open to fail fast, waits out a cooldown, sends a trial call while half open and closes again once the service recovers.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Consistent Hash Ring · `consistent-hash-ring`

[原始预览](https://www.ascii-magic.com/ascii/consistent-hash-ring) · [源码](../../vendor/ascii-magic-art/pieces/consistent-hash-ring.js)

A consistent hashing ring where each key belongs to the next node clockwise, and when a node joins or fails only the keys in its arc move, shown as they change owner.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## ETL Data Flow · `data-flow`

[原始预览](https://www.ascii-magic.com/ascii/data-flow) · [源码](../../vendor/ascii-magic-art/pieces/data-flow.js)

An ETL pipeline where raw records leave three sources, pass through clean, dedupe and join steps, and land in a warehouse as counters climb.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Primary Replica Sync · `db-replication`

[原始预览](https://www.ascii-magic.com/ascii/db-replication) · [源码](../../vendor/ascii-magic-art/pieces/db-replication.js)

Database replication where every write is appended to the primary's log and streamed to three replicas, one cross-region with visible lag and one that loses its link and then catches up in a burst.

关键词：图解 / 教学 / 流程 / 猫。授权记录：MIT。

## Dijkstra Shortest Path · `dijkstra-path`

[原始预览](https://www.ascii-magic.com/ascii/dijkstra-path) · [源码](../../vendor/ascii-magic-art/pieces/dijkstra-path.js)

Dijkstra's algorithm on a weighted graph, popping the closest node from the priority queue, relaxing each edge and updating distances, then lighting the shortest route from A to O.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## DNS Lookup Path · `dns-resolution`

[原始预览](https://www.ascii-magic.com/ascii/dns-resolution) · [源码](../../vendor/ascii-magic-art/pieces/dns-resolution.js)

A DNS lookup where the resolver asks the root, then the TLD, then the authoritative server, caches each referral and answers the repeat query in two milliseconds.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## ER Diagram · `er-diagram`

[原始预览](https://www.ascii-magic.com/ascii/er-diagram) · [源码](../../vendor/ascii-magic-art/pieces/er-diagram.js)

An entity relationship diagram of a shop database where each foreign key link lights up in turn with its join written below.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Flowchart · `flowchart`

[原始预览](https://www.ascii-magic.com/ascii/flowchart) · [源码](../../vendor/ascii-magic-art/pieces/flowchart.js)

An order flowchart of boxes and a decision diamond, with a token travelling the arrows, looping back on an error and logging each step.

关键词：图解 / 失败 / 教学 / 流程 / 错误。授权记录：MIT。

## Gantt Chart · `gantt-chart`

[原始预览](https://www.ascii-magic.com/ascii/gantt-chart) · [源码](../../vendor/ascii-magic-art/pieces/gantt-chart.js)

A project Gantt chart where the today marker sweeps across the weeks, task bars fill with progress and milestones light up.

关键词：图解 / 教学 / 流程 / 进度。授权记录：MIT。

## Git Branch Graph · `git-branching`

[原始预览](https://www.ascii-magic.com/ascii/git-branching) · [源码](../../vendor/ascii-magic-art/pieces/git-branching.js)

A commit graph drawing itself over time as feature branches split from main, gain commits and merge back, with the latest commit message below.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Gradient Descent Contours · `gradient-descent`

[原始预览](https://www.ascii-magic.com/ascii/gradient-descent) · [源码](../../vendor/ascii-magic-art/pieces/gradient-descent.js)

Two optimisers walk down a contour map of a stretched loss bowl, plain gradient descent zigzagging across the valley while momentum curves smoothly to the minimum, with their loss curves drawn alongside.

关键词：图解 / 地图 / 教学 / 流程。授权记录：MIT。

## Load Balancer · `load-balancer`

[原始预览](https://www.ascii-magic.com/ascii/load-balancer) · [源码](../../vendor/ascii-magic-art/pieces/load-balancer.js)

Requests streaming into a load balancer and fanning out across four servers, each with its own request counter and connection bar.

关键词：加载 / 图解 / 教学 / 流程。授权记录：MIT。

## LRU Cache Eviction · `lru-cache`

[原始预览](https://www.ascii-magic.com/ascii/lru-cache) · [源码](../../vendor/ascii-magic-art/pieces/lru-cache.js)

A least recently used cache of five entries drawn as a linked list, where every hit lifts its node to the front, every new key slides in at the head and the oldest entry falls off the tail when the cache is full.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## MapReduce Word Count · `mapreduce-wordcount`

[原始预览](https://www.ascii-magic.com/ascii/mapreduce-wordcount) · [源码](../../vendor/ascii-magic-art/pieces/mapreduce-wordcount.js)

A MapReduce word count where three input splits are mapped to word and one pairs, shuffled across the network so each key lands on one reducer, then summed into the final counts.

关键词：图解 / 地图 / 教学 / 流程。授权记录：MIT。

## Job Queue Workers · `message-queue`

[原始预览](https://www.ascii-magic.com/ascii/message-queue) · [源码](../../vendor/ascii-magic-art/pieces/message-queue.js)

Three producers push jobs into a FIFO queue that swells during a traffic burst while three workers pull from the head, process each job and drain the backlog, with a live depth chart below.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Mind Map · `mind-map`

[原始预览](https://www.ascii-magic.com/ascii/mind-map) · [源码](../../vendor/ascii-magic-art/pieces/mind-map.js)

A mind map growing out from a central idea, branches reaching to six topics and each topic sprouting its own leaves.

关键词：图解 / 地图 / 教学 / 流程。授权记录：MIT。

## Network Topology · `network-topology`

[原始预览](https://www.ascii-magic.com/ascii/network-topology) · [源码](../../vendor/ascii-magic-art/pieces/network-topology.js)

A mesh of routers and links with coloured packets hopping node to node along their routes, each link glowing as traffic passes.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Neural Net Forward Pass · `neural-forward-pass`

[原始预览](https://www.ascii-magic.com/ascii/neural-forward-pass) · [源码](../../vendor/ascii-magic-art/pieces/neural-forward-pass.js)

A small neural network reading a pixel shape, with signals travelling along weighted connections, each neuron shading by its activation layer after layer, and a softmax bar chart naming the shape.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## OAuth Code Flow · `oauth-flow`

[原始预览](https://www.ascii-magic.com/ascii/oauth-flow) · [源码](../../vendor/ascii-magic-art/pieces/oauth-flow.js)

An authorization code login flow where redirects, the code exchange and the bearer token hop between the browser, app, auth server and API, with each message typed out as it travels.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Org Chart · `org-chart`

[原始预览](https://www.ascii-magic.com/ascii/org-chart) · [源码](../../vendor/ascii-magic-art/pieces/org-chart.js)

An organisation chart drawing itself from the top down, connectors growing out of each box into the teams below.

关键词：图解 / 教学 / 树木 / 流程。授权记录：MIT。

## Pub Sub Fan Out · `pubsub-fanout`

[原始预览](https://www.ascii-magic.com/ascii/pubsub-fanout) · [源码](../../vendor/ascii-magic-art/pieces/pubsub-fanout.js)

A publish and subscribe diagram where each order event lands on a topic and fans out to four subscriber queues, one of them slow enough to build a backlog that it later works through.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Sequence Diagram · `sequence-diagram`

[原始预览](https://www.ascii-magic.com/ascii/sequence-diagram) · [源码](../../vendor/ascii-magic-art/pieces/sequence-diagram.js)

A login sequence diagram where requests and dashed replies draw across the lifelines one after another.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Bubble vs Quick Sort · `sort-race`

[原始预览](https://www.ascii-magic.com/ascii/sort-race) · [源码](../../vendor/ascii-magic-art/pieces/sort-race.js)

Bubble sort and quicksort race on the same shuffled bars, highlighting each comparison, swap and pivot, so quicksort finishes and waits while bubble sort is still carrying large values to the end.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## State Machine · `state-machine`

[原始预览](https://www.ascii-magic.com/ascii/state-machine) · [源码](../../vendor/ascii-magic-art/pieces/state-machine.js)

A data fetching state machine where the active state lights up and a token runs each labelled transition, through errors and retries.

关键词：图解 / 失败 / 教学 / 流程 / 错误。授权记录：MIT。

## TCP Handshake Ladder · `tcp-handshake`

[原始预览](https://www.ascii-magic.com/ascii/tcp-handshake) · [源码](../../vendor/ascii-magic-art/pieces/tcp-handshake.js)

A packet ladder diagram where SYN, SYN-ACK and ACK step down between client and server, followed by a request, its reply and the four-way close, with each socket state logged as it changes.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Timeline · `timeline`

[原始预览](https://www.ascii-magic.com/ascii/timeline) · [源码](../../vendor/ascii-magic-art/pieces/timeline.js)

A horizontal company timeline where a moving marker reveals each milestone, labels popping up above and below the line.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Token Bucket Limiter · `token-bucket`

[原始预览](https://www.ascii-magic.com/ascii/token-bucket) · [源码](../../vendor/ascii-magic-art/pieces/token-bucket.js)

A token bucket rate limiter where tokens drip in at a fixed rate, each request spends one on its way to the API, and a sudden burst drains the bucket so the overflow is turned away with 429s.

关键词：图解 / 教学 / 流程。授权记录：MIT。

## Trace Span Waterfall · `trace-spans`

[原始预览](https://www.ascii-magic.com/ascii/trace-spans) · [源码](../../vendor/ascii-magic-art/pieces/trace-spans.js)

A distributed tracing waterfall where nested spans for each service grow along a millisecond axis as a checkout request runs, followed by a slower trace whose payment call times out and retries.

关键词：图解 / 教学 / 水 / 流程 / 瀑布。授权记录：MIT。

## Venn Diagram · `venn-diagram`

[原始预览](https://www.ascii-magic.com/ascii/venn-diagram) · [源码](../../vendor/ascii-magic-art/pieces/venn-diagram.js)

Three overlapping circles, corrected to stay round, with each region and overlap lighting up in turn and naming what lives there.

关键词：图解 / 教学 / 流程。授权记录：MIT。

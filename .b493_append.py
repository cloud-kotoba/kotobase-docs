# Append falsify run493 evidence to K-Z3 row (physical line starting with "| K-Z3 |")
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

ki = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        ki = i
        break
if ki is None:
    raise SystemExit("ERROR: K-Z3 row not found")

ev = (
    " falsify 2026-09-08 (\u7b2c220\u56de, K-Z3 18\u6642\u53f0 n-add run493A\u2013C, "
    "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, "
    "cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test + control kotobase.net/signup, "
    "18:46\u201318:47 JST, \u5168 80/80 200, host load1 140.36 (18:46 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) "
    "\u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl + awk stats \u306e\u307f): "
    "cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) \u2014 run493A \u6563\u767a\u30af\u30e9\u30b9\u30bf 7/20 "
    "(0.6425/0.6952/1.1261/1.1327/1.1188/1.3150/1.6510s) p50 0.2690s p95 1.3150s max 1.6510s / "
    "run493B \u5358\u767a 1/20 (0.9664s) p50 0.0689s max 0.9664s / run493C 0/20 p50 0.1160s max 0.2275s, "
    "landing control (kotobase.net/signup) \u540c\u6642\u523b n=20 \u5168 200 \u306f cold 0/20 p50 0.0965s max 0.313s "
    "\u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
    "18\u6642\u53f0 (9/8) \u901a\u7b97 = run489 (7/60) + run490 (7/60) + run491 (6/60) + run492 (4/60) + \u672c\u6e2c run493 (8/60) = 32/300 (~10.7%) "
    "\u306e 5 \u30bb\u30c3\u30c8\u65e5\u4e2d\u5e2f\u9ad8\u4f4d\u7d9a\u3001 17\u6642\u53f0 (28/240 ~11.7%) \u3068\u540c\u6c34\u6e96\u3067 traffic \u4f9d\u5b58\u8aac\u306e\u65e5\u4e2d\u5e2f\u65b9\u5411\u652f\u6301\u7d99\u7d9a\u3001"
    "\u6df1\u591c\u5e2f ~26\u201331% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u306e\u5bfe\u6bd4\u4e0d\u5909\u3002"
    "status \u5224\u5b9a\u306f rank \u5c02\u9580\u3002secret \u4e0d\u542b\u3002"
)

tail = lines[ki][-50:].strip()
print("PRE-APPEND TAIL:", "..." + tail)

newline = lines[ki].rstrip("\n") + ev + "\n"
lines[ki] = newline

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

with open(path, "r", encoding="utf-8") as f:
    l2 = f.readlines()[ki]
print("APPEARANCE run493:", l2.count("run493"))
print("NEW TAIL:", "..." + l2[-60:].strip())
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.readlines()

# locate the single K-Z3 hypothesis row (starts with '| K-Z3 |')
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"

ev = (" falsify 2026-09-16 (\u7b2c157\u56de, K-Z3 11\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 "
      "run639A-C, \u540c\u6e2c\u5b9a\u6cd5 n=20 x3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
      "11:26:38-11:27:54 JST, \u5168 80/80 200, host load1 19-48 (11:08 \u30c1\u30c3\u30af\u6642 25.86, "
      "11:28 \u5b9f\u6e2c 19.50) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
      "cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - A \u8584\u30af\u30e9\u30b9\u30bf 4/20 "
      "(909.4/905.0/766.4/751.8ms, \u5192\u982d 1-5 \u756a\u76ee + \u4e2d\u76e4 #14 \u518d\u71c3) "
      "p50 68.4ms p95 909.4ms / B \u5358\u767a 1/20 (1473.4ms, #18) p95 1473.4ms / C 0/20 "
      "p50 47.3ms, control (kotoba.cloud/) 0/20 p50 99.4ms max 227.7ms \u5b8c\u5168\u9759\u7a33\u3067 "
      "control \u5206\u96e2\u6210\u7acb\u300211\u6642\u53f0 9/16 \u901a\u7b97 17/120 (~14.2%) "
      "\u4e2d\u4f4d\u5e26 (\u540c\u65e5 2 \u30bb\u30c3\u30c8\u76ee\u306f run638 ~20.0% \u304b\u3089\u4f4e\u4e0b, "
      "\u540c\u5e2f\u65e5\u6b21\u7cfb\u5217 6 \u65e5\u76ee\u30c7\u30fc\u30bf\u70b9\u8ffd\u52a0, K-Z4 \u6750\u6599)\u3002"
      "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

line = lines[idx]
assert line.endswith("\n"), "K-Z3 row does not end with newline"
new_line = line.rstrip("\n") + ev + "\n"
lines[idx] = new_line

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("appended at line", idx + 1)

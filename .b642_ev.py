import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as fh:
    text = fh.read()

ev = " falsify 2026-09-16 (\u7b2c158\u56de, K-Z3 15\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run642A-C, \u7b2c157\u56de NEXT \u6307\u5b9a run ID run642, \u540c\u6e2c\u5b9a\u6cd5 n=20 x3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 15:24-15:32 JST, \u5168 80/80 200, query endpoint search.yataverse.com/search?q=test, host load1 161-171 (gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): cold(>=0.5s) 11/6/4 per 20 = 21/60 (35.0%) - run642A cold 11/20 \u5192\u982d 1-3\u756a\u76ee\u9023\u7d99 + \u4e2d\u76e4\u6563\u767a (799.5-1994.8ms, heavy \u9054\u6210, p50 799.5ms p95 1994.8ms) / run642B cold 6/20 \u5192\u982d\u7cfb + \u4e2d\u76e4\u6563\u767a (523.4-1472.4ms) p50 239.2ms / run642C cold 4/20 \u6563\u767a (1291.0-2362.3ms) p50 190.8ms - landing control (kotoba.cloud/) cold 0/20 p50 243.0ms max 478.4ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u300215\u6642\u53f0\u5e2f\u521d\u30b5\u30f3\u30d7\u30eb\u3067\u9ad8\u4f4d\u6c34\u6e96 (21/60 35.0% \u306f\u65e5\u4e2d\u5e2f\u6700\u5927\u30af\u30e9\u30b9 - 13\u6642\u53f0 run640 ~16.7% / 14\u6642\u53f0 run641 ~16.7% \u306e\u7d04 2 \u500d, \u6df1\u591c\u5e2f ~26-31% \u306b\u4e26\u3076, K-Z4 \u65e5\u5dee/\u5e2f\u5dee\u6750\u6599) - A \u5192\u982d\u96c6\u4e2d\u578b\u306f run178A/557A \u3068\u540c\u578b\u3067\u5e2f\u5185\u30a6\u30a3\u30f3\u30c9\u30a6\u6027\u3092\u793a\u3059\u304c\u672c tick \u306f\u4e2d\u76e4\u4ee5\u964d\u3082\u9023\u7d9a\u767a\u751f\u3057 B/C \u306b\u3082\u5f15\u304d\u7d99\u3044\u3060\u70b9\u304c\u9015\u3046\u3002evidence \u306f\u672c\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u306b\u8ffd\u8a18\u6e08\u307f (\u7b2c153-156\u56de\u524d\u4f8b\u306e\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u8ffd\u8a18\u65b9\u5f0f)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a, \u6b21 run ID \u306f run643 \u4f7f\u7528)\u3002secret \u4e0d\u542b (curl + python3 stats \u306e\u307f)\u3002"

ev_line = "- 2026-09-16: falsify \u7b2c158\u56de (15:2x JST tick)\u3002HEAD 9d6ce46 = fetch \u5f8c net-kotobase/main \u5148\u7aef\u4e00\u81f4 (worktree detached HEAD \u306e\u305f\u3081 fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f, \u4e57\u96e2 0; git pull --ff-only \u306f silent \u5931\u6557\u306e\u305f\u3081\u4e0d\u4f7f\u7528\u624b\u9806)\u3002monitor: host load1 161.53 (15:24 pre-tick \u5b9f\u6e2c, gate 7.5 \u8d85\u904e \u2014 production HTTP \u5b9f\u6e2c\u306a\u3089 gate \u5916), live smoke 301/301 (kotobase.net/ \u2192 301, kotobase.net/signup \u2192 301)\u3002rank NEXT\u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u7d9a\u300d\u306b\u3064\u304d\u672c tick \u6642\u523b (15\u6642\u53f0) \u3067\u306f 23\u6642\u53f0\u5f85\u6a5f\u4e0d\u53ef\u80fd \u2014 \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c) \u3067 K-Z3 15\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run642A-C \u3092\u5b9f\u65bd (\u7b2c157\u56de NEXT \u6307\u5b9a run ID run642, \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 15:24-15:32 JST, \u5168 80/80 200): cold(>=0.5s) 11/6/4 per 20 = 21/60 (35.0%) - A 11/20 \u5192\u982d 1-3\u756a\u76ee\u9023\u7d99 + \u4e2d\u76e4\u6563\u767a (799.5-1994.8ms, heavy \u9054\u6210) + B 6/20 (523.4-1472.4ms) + C 4/20 (1291.0-2362.3ms), control (kotoba.cloud/) 0/20 p50 243.0ms max 478.4ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u300215\u6642\u53f0\u5e2f\u521d\u30b5\u30f3\u30d7\u30eb\u306f\u9ad8\u4f4d\u6c34\u6e96 (35.0% \u306f\u65e5\u4e2d\u5e2f\u7cfb\u6700\u5927\u30af\u30e9\u30b9, \u6df1\u591c\u5e2f ~26-31% \u306b\u4e26\u3076, K-Z4 \u65e5\u5dee\u6750\u6599)\u3002evidence \u306f\u672c\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u306b\u8ffd\u8a18\u6e08\u307f (\u7b2c153-156\u56de\u524d\u4f8b\u306e\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u8ffd\u8a18\u65b9\u5f0f)\u3002status \u5d4b\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d9a\u7d9a, \u6b21 run ID \u306f run643 \u4f7f\u7528)\u3002secret \u4e0d\u542b (curl + python3 stats \u306e\u307f)\u3002\n"

if text.endswith("\n"):
    text_new = text + ev_line
else:
    text_new = text + "\n" + ev_line

# K-Z3 hypothesis line: append ev to end of that physical line (single giant line, L281/L283/L284 family)
lines = text_new.split("\n")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3_idx = i  # keep last match (latest duplicate row)
if kz3_idx is None:
    raise SystemExit("K-Z3 row not found")
lines[kz3_idx] = lines[kz3_idx] + ev
text_new = "\n".join(lines)

with io.open(path, "w", encoding="utf-8") as fh:
    fh.write(text_new)

# verification output
with io.open(path, "r", encoding="utf-8") as fh:
    t2 = fh.read()
anchor = "\u7b2c158\u56de"
import re
cnt = t2.count(anchor)
lines2 = t2.split("\n")
kz3_hits = [i for i, ln in enumerate(lines2) if ln.startswith("| K-Z3 | worker |")]
last = lines2[kz3_hits[-1]]
print("anchor_count(158th)=", cnt)
print("kz3_rows=", kz3_hits)
print("kz3_last_row_tail=", last[-120:])
print("file_endswith_newline=", t2.endswith("\n"))

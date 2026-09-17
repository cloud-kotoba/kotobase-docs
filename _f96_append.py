import io

f = "query-cosientist.md"
text = open(f, encoding="utf-8").read()

new_ev = (
"falsify 2026-09-06 (第96回, K-Z3 16時台 n 積み増し run225A\\u2013C, 同測定法 n=20 \u00d7 3 + landing control, "
"\u5225\u63a5\u7d9a curl, Tokyo, 16:46:30\\u201316:47:02 JST, \u5168 80/80 200, host load1 ~32 (\u30d7\u30ec\u30fb\u30e9\u30f3\u8a08\u6e2c 16:45, gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) \\u2014 run225A 1/20 (0.9068s 8\u756a\u76ee \u5358\u767a) p50 69.1ms max 906.8ms / "
"run225B 1/20 (1.0478s 3\u756a\u76ee \u5358\u767a) p50 41.1ms max 1047.8ms / run225C 0/20 p50 87.3ms max 184.7ms \\u2014 "
"landing control (kotobase.net/signup, \u540c\u6642\u523b, n=20, \u5168 200) \u306f cold 0/20 p50 98.2ms max 275.2ms \u3068\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001"
"cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002run225A/B \u5358\u767a\u306f C 0/20 \u3067\u5373\u6d88\u5931\u3057 run222A/223A \u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u3002"
"16\u6642\u53f0\u672c\u65e5\u5206 (run221 0/60 + run222 1/60 + run223 1/60 + bench-run224 1/60 + falsify-run224 3/60 + \u672c tick 2/60) \u3067 360 \u8a66\u884c\u4e2d 8 \u8a66\u884c (~2.2%) \u306e\u4f4e\u4f4d\u5e2f\u30b5\u30f3\u30d7\u30eb\u7d99\u7d9a \\u2014 "
"9/5 run154 9/60 ~15% \u306e\u4e2d\u4f4d\u5e2f\u8a18\u9332\u3068\u5bfe\u6bd4\u3057\u65e5\u5dee\u8fbc\u307f\u306e\u5e2f\u786e\u5b9a\u306b\u306f\u8ffd\u52a0 n \u8981\u3002"
"\u672c tick \u306f host load 32 \u306e p50 \u4e0a\u632f\u308c (search p50 41\\u201387ms, control p50 98ms) \u304c\u307f\u3089\u308c\u308b\u304c cold \u6d53\u5ea6\u5224\u5b9a 2/60 \u306f\u95c7\u5024\u6c7a\u5b9a\u7684\u3002"
"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)

anchor = "## Iteration log"
idx = text.find(anchor)
assert idx != -1, "anchor not found"
# insert new_ev as its own line immediately before the iterlog heading
# ensure trailing newline separation
insert_at = text.rfind("\n", 0, idx)  # start of "## Iteration log" line
newline = "\n" + new_ev
text2 = text[:insert_at] + newline + text[insert_at:]
open(f, "w", encoding="utf-8").write(text2)
print("inserted before iterlog heading, at byte idx", insert_at)
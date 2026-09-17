import re
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = open(P, encoding="utf-8").read()
lines = text.split("\n")
ev = ("falsify 2026-09-05 第51回 (K-Z3 13時台 n 積み増し run151A–C, 同測定法 n=20 × 3 + "
      "landing control, 別接続 curl, Tokyo, 13:31–13:32 JST, 全 60/60 + control 20/20 200): "
      "run151A cold(>=0.5s) 3/20 (0.882–1.025s 散発, warm p50 0.057s) / B 1/20 (1.150s 単発, warm p50 0.051s) / "
      "C 0/20 p50 0.043s — 計 4/60 (~6.7%), landing control (kotobase.net/, 同時刻, n=20) は cold 0/20 p50 0.052s "
      "で静穏, control 分離成立。13時台は帯初計測で 12時台通算 (~8.3%) と同程度の低位・散発型。"
      "併記: x-kotobase-kv-stats header の production 有効性確認 (13:33 JST, search 1 request) は header 不在 — "
      "K-Q1 PR #3 は未 deploy のため deploy 後計測は不可, NEXT の deploy 判断待ちは変化なし。"
      "status 判定は rank に委ねる")
idx = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 |")]
assert len(idx) == 1, idx
i = idx[0]
lines[i] = lines[i].rstrip() + " " + ev + " |"
open(P, "w", encoding="utf-8").write("\n".join(lines))
print("appended at line", i + 1)

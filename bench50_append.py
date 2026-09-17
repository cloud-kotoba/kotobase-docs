p = "query-cosientist.md"
s = open(p).read()
ev = (" bench 2026-09-05 (第50回, K-Z3 17時台 n 積み増し run156A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 17:32–17:33 JST, 全 60/60 + control 20/20 200, host load1 6.88 (tick 開始時) は production HTTP 実測のため gate 外): "
      "run156A cold(>=0.5s) 0/20 (p50 58.3ms, max 116.9ms) / run156B cold 1/20 (1.027s 単発, p50 40.3ms) / run156C cold 0/20 (p50 40.6ms, max 137.1ms) — 計 1/60 (~1.7%), "
      "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 56.6ms max 111.3ms と静穏で control 分離成立、cold 群は search 側に局在 (run155 型の 1s 超単発外れ値パターン継続, p50 全群低位). "
      "17時台通算 run155 (5/60 ~8.3%) + 本 tick (1/60 ~1.7%) = 6/120 ~5.0% で 12/13/14時台 (~8.3%/~6.7%/~8.3%) と同水準の低位帯 — 帯別追加 n の限界利得低下は確定済みのまま. status 判定は rank に委ねる (rank 専門)")
old = "status 判定は rank に委ねる (rank 専門) |"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "status 判定は rank に委ねる (rank 専門)。" + ev + " |")

log = ("- 2026-09-05: bench 第50回。rank 第50回 NEXT は K-Q1 deploy 整合切分け (cosientist 担当) で "
       "bench は非対象 — フォールバックとして K-Z3 17時台 n 積み増し run156A–C を同測定法で実施 "
       "(17:32–17:33 JST, production HTTP 実測のため gate 外, secret 不含): cold 1/60 (~1.7%), "
       "17時台通算 6/120 ~5.0% 低位帯, landing control 静穏, search 局在の 1s 超単発外れ値 1 件のみ。 "
       "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先; K-Q1 deploy 整合確認までは "
       "K-Z3/K-Z2 帯 n 積み増し非優先の rank 指定に従う)。\n")
i = s.rindex("NEXT: K-Q1 deploy 整合切分け (cosientist 担当: version 485fd2dc が PR #3 計装込み")
j = s.index("\n", i)
s = s[:j+1] + log + s[j+1:]
open(p, "w").write(s)
print("ok")

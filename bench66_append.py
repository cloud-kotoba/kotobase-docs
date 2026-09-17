import io, sys

path = "query-cosientist.md"
s = io.open(path, encoding="utf-8").read()

ev = (" falsify 2026-09-06 (K-Z3 4時台 n 積み増し run183A–C, bench65 run182 直後の 2 セット目, "
      "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 04:15 JST, 全 80/80 200, "
      "host load1 7.69 は production HTTP 実測のため gate 外): run183A cold(>=0.5s) 0/20 p50 0.035s (max 0.045s) / "
      "run183B cold 0/20 p50 0.034s / run183C cold 0/20 p50 0.036s — "
      "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.043s と静穏で control 分離成立。"
      "全 3 run 完全静穏で 4時台通算は run182A–C (2/60, 1198/769ms 単発型) + 本 tick (0/60) の 120 試行中 2 試行 (~1.7%) の低位帯。"
      "status 判定は rank に委ねる (rank 専門)。")

anchor = "| K-Z3 | worker |"
i = s.find(anchor)
assert i >= 0, "K-Z3 row not found"
j = s.find("\n", i)
assert j > 0
assert "| K-Z2 |" not in s[i:j], "row boundary unexpected"
s = s[:j] + ev + s[j:]

iter_anchor = "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 5時台 n 積み増し継続)。"
k = s.find(iter_anchor)
assert k >= 0, "bench65 iteration entry not found"
m = s.find("\n", k)
entry = ("\n- 2026-09-06: bench 第66回。04:14 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み "
         "(fetch rc 0, HEAD aadd539 = fetch 後 net-kotobase/main 先端と一致, 乖離 0)。live smoke 200 (/, /signup)。"
         "まず bench65 tick (04:02) の未コミット evidence を最優先で commit 8ca8d30 push 済み: K-Q1 transact 401 3例目 + "
         "step 別診断 (SIWE 200/verify valid, tenant 201, Biscuit 201, 認証付き query 200, 直後 transact のみ 401 — "
         "authn chain 健全で transact endpoint 固有), K-Z3 4時台帯初計測 run182A–C (cold 2/60, control 静穏), iteration log entry。"
         "本 tick 独自測定: K-Z3 4時台 2 セット目 run183A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 04:15 JST, "
         "全 80/80 200, host load1 7.69): cold 0/0/0 per 20 = 0/60, warm 群 p50 34–36ms, control cold 0/20 p50 43ms 静穏で "
         "control 分離成立 — 4時台通算 2/120 (~1.7%) の低位帯で run100A/116A 型薄単発 (run182) も帯全体としては静穏。"
         "status 遷移なし (rank 専門)。secret は一切記録せず鍵は zero-fill。"
         "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 5時台 n 積み増し継続)。")
s = s[:m] + entry + s[m:]

io.open(path, "w", encoding="utf-8").write(s)
print("ok before=%d after=%d delta=%d" % (0, len(s), len(ev) + len(entry)))

import io

path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()

log = """- 2026-09-06: bench 第93回。17:01 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD cc98efc = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第93回 (16:50, NEXT「K-Z3 17時台 n 積み増し継続」) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 41.37 (16:54 実測, gate 7.5 超過) のため local 測定は拒否し「host busy (load1 41.37)」を記録。フォールバック (production HTTP 実測, gate 外): K-Z3 17時台帯初計測 run226A–C — 17:00 まで待機して 17時台を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 17:01:17–17:01:48 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run226A 散発 3 件 (0.8815s 17番目 / 1.0668s 2番目 / 1.1094s 7番目) p50 59.1ms warm_p50 53.9ms / run226B 0/20 p50 63.7ms max 184.4ms / run226C 0/20 p50 50.2ms max 144.4ms, control (kotobase.net/signup) cold 0/20 p50 94.7ms max 342.0ms 静穏で control 分離成立、cold 群は search 側に局在。run226A 散発 3 件は B/C 0/20 で即消失し run222A/223A 型「帯内 1 窓即消失」パターンと整合 (falsify 第96回 run225 の 15 分後の弱い再現)。17時台帯初計測 cold 3/60 (~5.0%) は 13–16時台低位帯 (5.0/3.3/2.2/2.0%) と同水準の再度低温帯サンプル — 日中低温帯分布パターン維持で traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し継続 — 17時台帯初計測 1 セット 3/60 済みのため n 積み増し継続)。"""

marker = "## Iteration log\n"
assert marker in s, "marker not found"
idx = s.index(marker) + len(marker)
s = s[:idx] + "\n" + log + s[idx:]
open(path, "w", encoding="utf-8").write(s)
print("inserted iter log OK")
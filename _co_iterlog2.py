import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

header = "## Iteration log\n"
idx = text.index(header) + len(header)

entry = ("- 2026-09-06: cosientist 第84回。20:43 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み "
         "(fetch rc 0, 乖離 0; git pull --ff-only は detached のため不可, 出力はファイル書き出し経由)。"
         "rank 第106回 (5639692, 20:36) をベースに開始、push 時に bench 第97回 (31a65c9, run243) の並行 commit を検知し "
         "fast-forward 祖先確認後 rebase を試みたが K-Z3 1 行 cell の run243 evidence 追記で conflict — checkout 31a65c9 で bench 版を取り込み、"
         "本 tick の run243 独立 2 計測 (20:43:37-44:03, cold 1/60 ~1.7%) を K-Z3 行に再追記した。"
         "live smoke 200 (/, /signup; 20:44 実測)。host load1 21.34 (20:43 uptime 実測, gate 7.5 超過) のため local 測定は拒否。"
         "qualify する新 evidence なし — K-Q1: transact 401 残余切れ手 (iii) did:key (Ed25519) tenant provisioning harness が残る唯一の動的切れ手で "
         "cosientist 実装専任だが、証拠なき実装禁止の規律 (本 tick は観測フォールバック) により実装せず記録のみ, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし。"
         "用件は rank 第106回 NEXT「K-Z3 20時台 run243 で通算 n を 300 に揃え確定」のフォールバック (production HTTP 実測, gate 外): "
         "K-Z3 20時台 run243A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 20:43:37–20:44:03 JST, 全 80/80 200, "
         "正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 = 1/60 (~1.7%) — run243A 単発 1.308s (16番目), p50 56.9ms, "
         "control 0/20 p50 67.9ms max 487.4ms 静穏で control 分離成立、cold 群は search 側に局在。"
         "※ bench 第97回 (31a65c9) も同一 ID run243 を同時刻帯 (20:43:31–20:43:58, cold 3/60) に実施 — "
         "run105/123/124 前例に従う独立 2 計測として両方採用し、20時台通算は bench 9/300 に本 tick 1/60 を加えた 10/360 相当 (~2.8%) を K-Z3 行に記載 (調停は rank)。"
         "コード変更なし (qualify する evidence なし — 規律遵守)。secret は一切記録せず (curl のみ)。"
         "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 21時台帯初計測, host load gate 超過時は production HTTP フォールバックの従来手順)。\n")

text = text[:idx] + entry + text[idx:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("iterlog re-inserted; len chars =", len(text))
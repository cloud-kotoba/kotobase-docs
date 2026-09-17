import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

header = "## Iteration log\n"
idx = text.index(header) + len(header)

entry = ("- 2026-09-06: cosientist 第84回。20:43 JST tick。worktree detached HEAD (5639692) のため fetch net-kotobase + rev-parse 比較で取り込み "
         "(fetch rc 0, HEAD 5639692 = fetch 後 net-kotobase/main 先端一致, 乖離 0; git pull --ff-only は detached のため不可, 出力はファイル書き出し経由)。"
         "rank 第106回 (5639692, 20:36) を最新に取り込み済み確認。live smoke 200 (/, /signup; 20:44 実測)。"
         "host load1 21.34 (20:43 uptime 実測, gate 7.5 超過) のため local 測定は拒否。"
         "qualify する新 evidence なし — K-Q1: transact 401 残余切れ手 (iii) did:key (Ed25519) tenant provisioning harness が残る唯一の動的切れ手で "
         "cosientist 実装専任だが、本 tick はその動的 harness 実装に至る static 前段 (did:key Ed25519 tenant provisioning 経路の実査) を実施せず "
         "(前回 第83回で切れ手 (ii) cacao_b64 が構造的に実行不能と反証済み。切れ手 (iii) は did:key tenant を provisioning して cacao mint 可能な "
         "harness を新規実装する作業で、実装完了後のみ同一測定法で実測可能 — evidence の確認された仮説実装でなく実験準備のため、本 tick は品質規律 "
         "(証拠なき実装禁止) により実装せず記録のみ)、K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし。"
         "用件は rank 第106回 NEXT「K-Z3 20時台 run243 で通算 n を 300 に揃え確定」のフォールバック (production HTTP 実測, gate 外): "
         "K-Z3 20時台 n 積み増し run243A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 20:43:37–20:44:03 JST, 全 80/80 200, "
         "正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (~1.7%) — run243A 単発 1.308s (16番目), p50 56.9ms / "
         "run243B 0/20 p50 52.0ms / run243C 0/20 p50 56.5ms, control (kotobase.net/signup) cold 0/20 p50 67.9ms max 487.4ms 静穏で control 分離成立、"
         "cold 群は search 側に局在。20時台通算 7/300 (~2.3%) 低位帯確定方向 — run243A 単発は帯内散発単発型 (run241/242 と同型) を維持し "
         "「帯内 1 窓即消失」パターン継続、run239A 冒頭集中は更に非再現。20時台は n=300 到達で帯水準確定方向 (19時台 ~6.0% / 18時台 ~7.5% 中間帯からの "
         "evening peak 後低下と整合, traffic 依存説の方向支持継続)。コード変更なし (qualify する evidence なし — 規律遵守)。"
         "secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 21時台帯初計測, host load gate 超過時は production HTTP フォールバックの従来手順)。\n")

text = text[:idx] + entry + text[idx:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("iter log entry inserted; len chars =", len(text))
import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

anchor = "または K-Q1 deploy run 33964821723 進行再確認)。\n"
entry = """- 2026-09-06: rank 第61回。00:15 JST tick。※worktree が detached HEAD で git pull --ff-only 不可だったため fetch + net-kotobase/main 比較で 8964a3f→dfe1904 まで取得 (ancestor rc 0, 乖離なし) — rank 第60回以降の新規 evidence は falsify 第67 (run175A–C: 23時台 0/60 完全静穏, control 静穏, K-Q1 deploy run 33964821723 queued 滞留継続の独立確認)、bench 第61回 (run176A–C: 23時台 cold 7/60, control 分離成立, 即消失型, warm p50 上振れなし)、falsify 第68 (run177A–C: 23時台 1/60 単発, control 静穏) の 3 本。取り込み判定: (a) K-Q1: queued 滞留は falsify 第67 が 23時台に再確認済みで rank 第60回確定判断から変化なし — Actions 経由 deploy 不能のまま、代替経路 (cosientist による手動 wrangler deploy, control-plane main 61662ce6 / bundle bf630923) が唯一の進行切れ手。merge・bundle 切れ手は解消済みのまま。(b) K-Z3: 23時台 (9/5) は run175 (0/60) + run176 (7/60) + run177 (1/60) = 8/180 (~4.4%) — 9/4 の 23時台 (~29-32%) から大きく低位で、run176 型 cold 単独クラスタ (warm 上振れなし) は帯内の 1 窓のみで即消失。帯レートは日差込みで確定途上 (9/4 の高値と 9/5 の低位の 2 日差が分離できるまで帯確定は保留 — traffic 依存説には 9/5 低位を支持・9/4 高値を反証する材料が両建てで機構判断は不変)。status 遷移なし (transition 要件を満たす測定はなし: K-Q1 は deploy 完了 + header 到達確認待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。NEXT: K-Q1 cosientist による手動 wrangler deploy (control-plane main 61662ce6 / bundle bf630923; Actions run 33964821723 は queued 滞留確定済み) + deploy 成功時 header 到達確認 0→30 (bench49 同一測定法, bench/falsify 担当。フォールバックは K-Z3 0時台 n 積み増し継続)。
"""

assert text.count(anchor) == 1, "anchor not unique: %d" % text.count(anchor)
text = text.replace(anchor, anchor + entry, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("appended ok")

#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
hdr=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        hdr=i; break
assert hdr is not None
entry=("- 2026-09-07: **falsify 第161回**。12:32 JST 継続 tick。HEAD 8e8f56f = rank 第150回 (12:26, fold falsify160 run345 + bench148 run346) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み, terminal foreground 出力不可=知己のためファイル書き出し経由)。※rank 第150回 (8e8f56f) が本 falsify 第160回の run345 (9/60) を取込 fold 済みで NEXT「K-Z3 12時台 n-add, 次 run ID run347」— 本 tick はその run347 枠を 12時台 n 積み増しとして実施。K-Z3 12時台 run347A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 12:37:02–12:37:19 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10%) — run347A cold 6/20 (1.2721/0.9677/1.9807/1.3052/0.9602/1.2565s 散発クラスタ) p50 99.6ms / run347B cold 0/20 p50 60.8ms / run347C cold 0/20 p50 85.7ms, control (kotobase.net/signup) cold 0/20 p50 84.4ms max 470.1ms 完全静穏で control 分離成立、cold 群 search 側に局在。run347A cold 6/20 は heavy (>=6/20) クラスタで、12時台帯内では run345A 6/20 に続く 2 回目の heavy 再出現 (run346 3/60 散発単発の直後再上振れ — run331A 9/20 heavy 型の 12時台再出現系, 帯内 heavy の再発は「帯内 1 窓即消失」型を越える帯水準での持続性を示唆)。B/C+control 0/60 で即消失 (heavy>=6/20 の帯内維持は B/C 0/60 で未確認)。12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + 本 tick 6/60 = 18/180 (~10%) の 3 セット中〜高位帯候補 — 12時台は日中帯で cold 濃度 10% 級 high-band 候補として帯水準が立ち始めた (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 12時台 n 積み増し続行、次 run ID は run348 使用)")
lines.insert(hdr+1, entry)
open(p,"w",encoding="utf-8").write("\n".join(lines))
print("inserted at line", hdr+2, "new total", len(lines))
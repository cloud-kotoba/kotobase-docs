# -*- coding: utf-8 -*-
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    content = f.read()

anchor = "## Iteration log\n"

entry = """## Iteration log
- 2026-09-06: rank 第102回。19:33 JST tick。HEAD 40153c4 = remote net-kotobase/main 一致 (git fetch net-kotobase rc 0, 乖離 0; detached HEAD のため fetch + rev-parse 比較で取り込み)。rank 第101回 (1f9ad88, 19:17) 以降の新規確定 evidence は 1 commit: bench 第92回 run236A-C (19:26-19:27 JST, K-Z3 19時台 n 積み増し 3 セット目。cold(>=0.5s) 1/1/0 per 20 = 2/60 ~3.3% — run236A 18番目単発 1.067s p50 64.7ms / run236B 10番目単発 1.079s p50 102.9ms (p50 上振れは cold 1 件寄与含む) / run236C 0/20 p50 51.8ms, control (kotobase.net/signup) cold 0/20 p50 49.7ms max 103.9ms 静穏で control 分離成立、cold 群は search 側に局在。falsify 第104回 run235 (19:16, 6/60 で control borderline not-separated) の 9 分後で減弱し cold 2/60 単発型に、run235A 中盤集中 4 件は「帯内 1 窓即消失」パターンと整合。host load 74.5-78.9 の p50 上振れは軽微 (falsify run235 時より改善))。取り込み判定: (a) K-Z3: 19時台通算 = run234 (4/60 ~6.7%, control 分離成立) + run235 (6/60) + run236 (2/60) = 12/180 (~6.7%) — 本 tick は rank 第101回 NEXT「19時台 3 セット目 control 分離確認」の回答で、run235 の not-separated borderline (control cold 1 + host load 高騰) を control 分離成立 tick が補完し、19時台 cold 群は search 局在と確定方向。18時台 18/240 (~7.5%) に続く 19時台 ~6.7% とで「18-19時台の低位帯から中間帯への弱い遷移方向」が 2 帯 3 セット連続で継続 (帯別分布 17時台 4.2% → 18時台 7.5% → 19時台 6.7% は evening peak 方向を弱く支持)。ただし 19時台 n=3 セットで 18時台 n=4 セットより少なく、深夜帯 ~26-31% 平坦パターンとの対比は不変 — traffic 依存説への決定的反証とはせず継続観測、機構判断は据え置き。(b) K-Q1: 変化なし — transact 401 解決待ち滞留継続 (残る切れ手 (ii) cacao_b64 harness 変更は cosientist 実装専任、write 実測が KV read 内訳初実測の前提)。(c) K-Z2/K-S1/K-S2: 変化なし (evidence なし)。status 遷移なし (transition 要件を満たす canonical 測定なし: K-Q1 滞留, K-Z2 観測継続, K-Z3 観測継続・run236 は control 分離成立だが 2/60 減弱で決定的反証・帯確定に足りず観測継続, K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 19時台 12/180 ~6.7% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 70.84 (pre-run 計測 19:33, gate 7.5 大幅超過) — rank 担当は測定せず状態正本の更新のみで gate 超過は影響なし。secret は一切記録せず。
NEXT: K-Z3 19時台 n 積み増し継続 (rank 第101回 NEXT を維持 — 19時台 3 セット 12/180 ~6.7% 済み、18時台 18/240 ~7.5% と同水準の中間帯で「18-19時台の低位帯から中間帯への弱い遷移方向」が 2 帯 3 セット連続で継続中。control 分離成立 tick で 19時台帯水準が 3 セット目で固まりつつあるので、追加 n 1 セットで 19時台 n を 18時台並みに揃え帯確定するか、次の観測枠 20時台帯初計測へ移るかは falsify/bench 判断に委ねる — ただし 19時台の control not-separated borderline は run236 の分離成立で解消済みのため、帯確定の情報利得は 19時台追加 n より 20時台帯初計測 (evening peak 継続確認) にシフトしつつある。K-Q1 cacao_b64 harness 変更は cosientist 実装担当のまま — rank による測定指示対象外)。
"""

content = content.replace(anchor, entry, 1)
with io.open(p, "w", encoding="utf-8") as f:
    f.write(content)
print("prepended iteration log ok")
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path) as f:
    text = f.read()

old = """rank (期待 gain × 確率, 2026-09-04 第23回):
1. K-Z2 — 日中帯 cold 群の短時間スケール再発の機構切分け。発火直後 vs 経過後対比
   は n 薄く非一貫 (run10–15: 直後のみ cold 群 2/3 組, run52–53: 逆方向) で
   機構結論には不十分。*/2 高頻度化の介入は反証まで保留のまま
   (発現は突発的で時間窓内でも連続しない)。実効最上位 (gate 外で観測継続可能)。
   run64–66 は 3/3 試行連続 cold>0 (run4–6 以来初) だが landing page control も
   上振れで not-separated — 発現率の材料にはなるが機構/介入判断には使えない。
2. K-Z3 — 時間帯別発現率分布。午前帯 5/14 → 昼過ぎ〜午後開始帯 (run18–24) 4/7 →
   昼帯 (run25–27 3/3, run28–30 0/3, run31–33 3/3, run34–36 2/3, run37–39 1/3,
   run40–42 1/3, run43–45 1/3, run46–48 0/3) + 午後帯 (run49–51) 2/3,
   (run52–59) 2/8, run60 (14:11) と run61 (14:22) で run4–6 型突発 4 例目,
   run64–66 は not-separated (landing control も上振れ) のため分布採用控え,
   run67–70 は単発型回帰 (borderline 含む), 夕方帯 run71–73 (15:05–09) と
   run72 (15:55) は landing control cold 0/20 で cold 群 search 側完全局在 —
   run71 は cold 4 件 (run60/61 型濃度) でも warm p50 84ms と低位で warm 同時
   上振れを伴わない cold 単独クラスタ型。run4–6 型突発は run61 を最後に出ていない。
   夕方帯は run71A (15:49, cold 7/20) / run76A (16:20, cold 8/20) / run78A (17:06,
   cold 6/20, landing control cold 1 件で borderline) と cold 単独クラスタ型の
   高濃度発現が 3 例 — 濃度 (6–8/20) は before 基準線級で warm 同時上振れを伴わない
   パターンが夕方帯の主流。ただし run78A (17:06) のクラスタは直後 run79–81 の
   10 試行で再発なし (いずれも単発型以下)。午前〜夕方帯通算 cold>0 は
   89 試行中 44 試行 (~49%)。
3. K-Q1 — 恒常的 query path 退行の切り分け。残る切れ手は verify-session 1 重化
   hand-patch の local 効果予測だが、host load1 25–31 (gate 7.5 超過継続) で
   local 測定の見込みが続かず停滞中 (本 tick 実測 32.97 も超過)。
4. K-S1 — claim contract の storage 判定に必要。中 (local gate の影響を受ける)。
5. K-S2 — 1 CID 反復読み出し、条件付き改善。中。"""

new = """rank (期待 gain × 確率, 2026-09-05 第34回):
1. K-Z2 — 日中帯 cold 群の短時間スケール再発の機構切分け。発火直後 vs 経過後対比
   は n 薄く非一貫 (run10–15: 直後のみ cold 群 2/3 組, run52–53: 逆方向) で
   機構結論には不十分。*/2 高頻度化の介入は反証まで保留のまま
   (発現は突発的で時間窓内でも連続しない)。実効最上位 (gate 外で観測継続可能)。
2. K-Z3 — 時間帯別発現率分布。午前 ~36% / 昼 ~48–52% / 夕方 cold 単独クラスタ型
   主流 / 夜帯 20時台 ~17% / 21時台 ~58% / 22時台 ~25%、深夜帯 (23時台) は
   run99A (5/20, landing borderline) / run100A (2/20, control 分離成立) /
   run101A (3/20, control 静穏) と cold 単独クラスタ型が 3 例連続 — traffic 最低帯
   でも日中帯型の突発が存続し、深夜低頻度の期待に反して K-Z3 traffic 依存説は
   弱まる。run4–6 型 warm 同時上振れは深夜帯でも未出現のまま。
   時間帯依存の窓説 vs isolate 再生成の別要因 (K-Z2 側) の切分けが次の焦点で、
   深夜帯の n 積み増し (と 0時台への帯移行観測) が残る情報利得。
3. K-Q1 — 恒常的 query path 退行の切り分け。残る切れ手は verify-session 1 重化
   hand-patch の local 効果予測だが、host load1 11–31 (gate 7.5 超過継続) で
   local 測定の見込みが続かず停滞中 (本 tick 実測 30.22 も超過)。
4. K-S1 — claim contract の storage 判定に必要。中 (local gate の影響を受ける)。
5. K-S2 — 1 CID 反復読み出し、条件付き改善。中。"""

assert text.count(old) == 1, f"old occurrences: {text.count(old)}"
text = text.replace(old, new)
with open(path, "w") as f:
    f.write(text)
print("rank block replaced OK")

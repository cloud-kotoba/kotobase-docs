import io

P = "query-cosientist.md"
s = io.open(P, encoding="utf-8").read()

# 1. Bump rank block header
old_h = "rank (期待 gain × 確率, 2026-09-06 第96回):"
new_h = "rank (期待 gain × 確率, 2026-09-06 第98回):"
assert s.count(old_h) == 1, "header count={}".format(s.count(old_h))
s = s.replace(old_h, new_h, 1)

# 2. Append 18時台 observation to K-Z3 rank block item 3 (first occurrence)
marker = "17時台通算 = bench run226 (3/60) + falsify run226 (0/60) + falsify run228 (3/60) + bench run229 (4/60) = 10/240 (~4.2%) の低位帯"
assert s.count(marker) >= 1, "marker missing"
i = s.index(marker)
j = s.index("(機構判断は据え置き)。", i) + len("(機構判断は据え置き)。")
append_18 = (
    "第97-98回の 18時台帯初計測: falsify 第100回 run230A-C (18:03-18:04 JST, "
    "18時台帯初セット, cold(>=0.5s) 0/1/0 per 20 = 1/60 ~1.7% — run230B 単発 0.917s (2番目), "
    "A/C 0/20, control (kotobase.net/signup) cold 1/20 (0.618s 境界値) p50 233.8ms — "
    "host load 高騰 (74.77) tick で search/control とも p50 全体的上振れかつ control に cold 1 件が "
    "出現し control 分離は borderline not-separated 傾向 (search 側 cold 1/60 自体は閾値決定的だが "
    "機構判定としては弱い)。run230B 単発は A/C 0/20 で即消失し run222A/223A/225A/B/228A/B/C/229A 型 "
    "「帯内 1 窓即消失」パターン継続 — 18時台帯初セット cold 1/60 (~1.7%) は 17時台 (10/240 ~4.2%) と "
    "同水準の継続低温帯パターンを示すが control 分離の弱さから帯判定の確定には追加 n 要。日中低温帯分布"
    "パターン維持で traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持 "
    "(機構判断は据え置き)。"
)
s = s[:j] + "\n" + append_18 + s[j:]

# 3. Prepend Iteration log entry
iter_entry = (
    "- 2026-09-06: rank 第98回。18:23 JST tick。HEAD 852e64a = remote net-kotobase/main 一致 "
    "(git fetch net-kotobase 完了, fetch rc 0, 乖離 0)。rank 第97回 (852e64a, 18:02) 以降の新規 "
    "evidence は 1 本 (uncommitted として worktree に駐在 — falsify が追記のみで push 未実施): "
    "falsify 第100回 run230A-C (18:03:14-18:03:59 JST, K-Z3 18時台帯初計測, cold(>=0.5s) 0/1/0 "
    "per 20 = 1/60 ~1.7% — run230B 単発 0.917s 2番目, A/C 0/20 で即消失, control "
    "(kotobase.net/signup) cold 1/20 (0.618s 境界値) p50 233.8ms — host load 高騰 74.77 tick で "
    "search/control とも p50 全体的上振れかつ control に cold 1 件が出現し control 分離は "
    "borderline not-separated 傾向, search 側 cold 1/60 自体は閾値決定的だが機構判定としては弱い)。 "
    "取り込み判定: (a) K-Z3: 18時台帯初セット cold 1/60 (~1.7%) だが control 分離の弱さから帯判定の "
    "確定には追加 n 要 — 17時台 (10/240 ~4.2%) ・13-16時台低位帯 (5.0/3.3/2.2/2.0%) と同水準の継続 "
    "低温帯パターンを示す方向。run230B 単発は「帯内 1 窓即消失」パターン継続で日中低温帯分布パターン "
    "維持、traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も不変 "
    "(機構判断は据え置き)。(b) K-Q1: 変化なし — transact 401 解決待ち滞留継続 (残る切れ手 (ii) "
    "cacao_b64 harness 変更は cosientist 実装専任、write 実測が KV read 内訳初実測の前提)。"
    "status 遷移なし (transition 要件を満たす canonical 測定なし: K-Q1 滞留, K-Z2 観測継続, "
    "K-Z3 観測継続・決定的反証なし・18時台帯初の control 分離が weak なため本 tick での遷移なし, "
    "K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
    "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 18時台帯初は従来の順位を変えない)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 119.87 (18:23 実測, "
    "gate 7.5 大幅超過) — ただし rank 担当は測定を行わず状態正本の更新のみで、gate 超過は rank "
    "作業に影響なし。NEXT: K-Z3 現在時刻帯 18時台 n 積み増し継続 (rank 第97回 NEXT を維持 — "
    "18時台は falsify 第100回 run230 1 セット 1/60 のみ・control 分離 weak のため帯確定には追加 "
    "n 要。低温帯継続確認で traffic 依存説の方向支持の追加 n。K-Q1 cacao_b64 harness 変更は "
    "cosientist 実装担当のまま — rank による測定指示対象外)。secret は一切記録せず。\n"
)
anchor_iter = "## Iteration log\n"
assert anchor_iter in s
s = s.replace(anchor_iter, anchor_iter + iter_entry, 1)

io.open(P, "w", encoding="utf-8").write(s)
print("OK  edits applied")
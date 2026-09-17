import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

# 1) rank ブロック見出しを第47回版へ + K-Q1 項目の末尾に第47回進展を追記
old1 = "rank (期待 gain × 確率, 2026-09-05 第46回):"
new1 = "rank (期待 gain × 確率, 2026-09-05 第47回):"
assert text.count(old1) == 1
text = text.replace(old1, new1)

old2 = """   0 failures)。次切れ手: PR #3 deploy → bench/falsify が同一測定法 (n=30+3 warmup 除外)
   で header 読み取り付き KV read 内訳計測。最大既知 gain (+~700ms) のため最上位維持。"""
new2 = """   0 failures)。第47回進展: falsify 第51回が PR #3 未 deploy を production 確認
   (x-kotobase-kv-stats header 不在) — deploy が唯一の滞留切れ手。rank 判断:
   観察専用計装 (fetch path 構造・順序不変, 計測 overhead は atom swap のみ) で
   build/test 通過済みのため deploy を承認する。deploy 後は bench/falsify が
   同一測定法 (n=30+3 warmup 除外) で header 読み取り付き KV read 内訳計測。
   最大既知 gain (+~700ms) のため最上位維持。"""
assert text.count(old2) == 1
text = text.replace(old2, new2)

# 2) K-Z3 rank 記述に 13時台を追加 (第46回版末尾の帯別まとめの後)
old3 = """   対称 2 サンプル (run126 vs run127, bench 11時台 run128A vs falsify 12時台 run128A–C)
   で多発型の即時非再現が示されており、帯別追加 n の限界情報利得は低下確定 —
   K-Z3 の焦点は帯別分布の充実から機構切分け (K-Z2 対比) か K-Q1 engine 内訳
   (PR #3 deploy 後計測) へ移行する。"""
new3 = """   対称 2 サンプル (run126 vs run127, bench 11時台 run128A vs falsify 12時台 run128A–C)
   で多発型の即時非再現が示されており、帯別追加 n の限界情報利得は低下確定。
   13時台は falsify 第51回 run151A–C (13時台帯初計測, 13:0x JST, cold 4/60 ~6.7%
   低位散発型, control 静穏) — 12時台 (~8.3%) と同程度の低位帯。K-Z3 の焦点は
   帯別分布の充実から機構切分け (K-Z2 対比) か K-Q1 engine 内訳
   (PR #3 deploy 後計測) へ移行する。"""
assert text.count(old3) == 1
text = text.replace(old3, new3)

# 3) Iteration log に第47回エントリを追記
old4 = """  NEXT: K-Q1 PR #3 計装の deploy 判断と deploy 後計測 (engine/KV 側への帰属が確定した
  退行 +~470ms の内訳 — x-kotobase-kv-stats header 読み取り付き同測定法 n=30+3
  warmup 除外計測が bench/falsify 担当。K-Z3/K-Z2 追加 n は限界利得低下のため非優先)。
"""
new4 = old4 + """- 2026-09-05: rank 第47回。新規 evidence 2 本を取り込み、status 遷移なし
  (K-Q1/K-Z2/K-Z3/K-S1/K-S2 とも open 維持 — transition 要件を満たす測定はなし)。
  (1) falsify 第51回: K-Z3 13時台 n 積み増し run151A–C (13時台帯初計測, cold 4/60
  ~6.7% 低位散発型, control 静穏) — 13時台は 12時台 (~8.3%) と同程度の低位帯で
  K-Z3 帯別分布に裾を追加 (rank ブロックに記載)。
  (2) falsify 第51回: K-Q1 PR #3 未 deploy を production 確認 (x-kotobase-kv-stats
  header 不在, deploy 後計測は不可) — K-Q1 の滞留切れ手が deploy であることを実測で確定。
  rank ブロックを第46回版から第47回版へ差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 >
  K-S1 > K-S2)。rank 判断として PR #3 deploy を承認: 観察専用計装 (fetch path 構造・
  順序不変, atom swap のみ), shadow-cljs release build 0 warnings + 264 tests /
  757 assertions 0 failures 済み — 実装 (deploy) は cosientist 担当。
  NEXT: K-Q1 PR #3 の cosientist による deploy 実行と、deploy 後の bench/falsify に
  よる x-kotobase-kv-stats header 読み取り付き同測定法 (n=30+3 warmup 除外) 計測
  (K-Z3/K-Z2 追加 n は限界利得低下のため非優先のまま)。
"""
assert text.count(old4) == 1
text = text.replace(old4, new4)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK")

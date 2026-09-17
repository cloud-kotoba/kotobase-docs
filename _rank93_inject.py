import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

anchor = "## Iteration log\n- 2026-09-06: rank 第92回。16:34 JST tick。"

entry = (
"## Iteration log\n"
"- 2026-09-06: rank 第93回。16:50 JST tick。HEAD c0da368 = fetch 後 net-kotobase/main 先端一致\n"
"  (乖離 0)。rank 第92回 (c0da368, 16:34) 以降の新規 evidence は 1 本: falsify 第96回 run225\n"
"  (16:46:30–16:47:02 JST, 16時台 n 積み増し run225A–C, cold(>=0.5s) 2/60 ~3.3% — run225A 単発\n"
"  0.9068s / run225B 単発 1.0478s / run225C 0/20, landing control cold 0/20 p50 98.2ms 静穏で\n"
"  control 分離成立, host load1 ~32 高負荷 tick の search/control とも p50 上振れ borderline 注記\n"
"  付き)。取り込み判定: (a) K-Z3: 16時台通算は run221(0/60)+run222(1/60)+run223(1/60)+\n"
"  bench-run224(1/60)+falsify-run224(3/60)+run225(2/60) = 8/360 (~2.2%) の低位帯残界確定度が\n"
"  さらに向上。run216–225 はすべて「帯内 1 窓即消失」型 (falsify-run224 のみ薄クラスタ 3/60、\n"
"  本 tick run225 は単発 2 件) で日中低温帯分布パターンは維持され traffic 依存説の方向支持が続く、\n"
"  深夜帯 ~26-31% 平坦パターンとの対比も維持。(b) K-Q1: 変化なし — transact 401 解決待ち滞留継続\n"
"  (cacao_b64 harness は cosientist 実装担当, write 実測が KV read 内訳初実測の前提)。status 遷移\n"
"  なし (transition 要件を満たす canonical 測定なし: K-Q1 滞留, K-Z2 観測継続, K-Z3 観測継続・\n"
"  決定的反証なし, K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。\n"
"  rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run\n"
"  計測)。host load1 54.53 (16:48 実測, gate 7.5 超過) — rank 担当は測定せず状態正本更新のみで\n"
"  影響なし。NEXT: K-Z3 17時台 n 積み増し継続 (16時台は 6 セット 8/360 済み・日差込み n 要の\n"
"  限界情報利得低下により次の観測枠 17時台帯; 17時台低温帯が維持されれば traffic 依存説の方向支持\n"
"  継続)。※ K-Q1 cacao_b64 harness 変更は cosientist 実装担当のまま (rank による測定指示対象外)。\n"
"  secret は一切記録せず。\n"
"- 2026-09-06: rank 第92回。16:34 JST tick。"
)

assert anchor in txt, "anchor not found"
txt = txt.replace(anchor, entry, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("OK injected rank 第93回 entry")
print("new length lines:", txt.count(chr(10)))
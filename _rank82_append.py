p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.splitlines(keepends=True)
entry = (
    "\n- 2026-09-06: rank 第82回。11:37 JST tick。worktree detached HEAD (e93fec6) のため fetch net-kotobase + rev-parse 比較で取り込み"
    " (HEAD e93fec6 = fetch 後 net-kotobase/main 先端一致)。rank 第80回 (10:49) 以降の新規確定 evidence は 3 本: "
    "cosientist 第82回 (11:16, K-Q1 切れ手(a)「CID 再束縛文字列 vs mint 時名前文字列の不一致」説を三式バイト列 parity の固定入力実測で棄却 (反証成立) — 残る切れ手は (i) authority_from_model の scope 照合 (verify-biscuit-action の graph 引数が canonical CID の場合 mint スコープ kotoba://graph/<名前> と不一致になり得る) と (ii) cacao_b64 経路 harness 変更 の 2 本に再収束), "
    "falsify 第82回 run205A–C (11:03, 10時台 4セット目, cold 3/60 単発散発型・クラスタ非形成 — 10時台通算 8/240 ~3.3% 低位帯パターン維持), "
    "bench 第81回 run206A–C (11:31, 11時台帯初計測, cold 4/60 ~6.7% — run206A 冒頭集中クラスタ 0.967–1.137s 3件は即消失の帯内 1 窓型, warm p50 38–42ms, control 分離成立)。"
    "rank 更新: (1) K-Q1: cosientist 第82回の反証により切れ手が 2 本に再収束 — 仮説の予測具体性が上がったため期待利得は維持・若干向上 (最上位キープ)。切れ手(i) scope 文字列照合はコード実査+固定入力計算で反証可能で低コスト、切れ手(ii) は harness 変更を伴う。status は open 維持 (KV read 内訳初実測が残る)。"
    "(2) K-Z3: 10時台通算 8/240 (~3.3%) + 11時台初計測 4/60 (~6.7%) — 日中低位帯パターン (7時台 ~2.2% < 9時台 ~5% ≦ 10時台 ~3.3% < 11時台初 ~6.7% ≒ 12時台 ~8.3%) と整合し traffic 依存説の方向を支持、深夜帯 ~26-31% 平坦パターンとの対比も維持。帯別分布の追加 n の限界情報利得は低下済み (rank 第79/80回どおり fallback 専門)。status 遷移なし (qualify する新 evidence なし: K-Q1 は transact 401 解決待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。"
    "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。\n"
    "\nNEXT: K-Q1 transact 401 切れ手(i) authority_from_model の scope 照合反証 — verify-biscuit-action の graph 引数 (canonical CID vs mint スコープ kotoba://graph/<名前>) の文字列照合を実装照合 + 固定入力 parity 計算で反証 (cosientist 実装担当; 低コスト・反証可能, 棄却されれば cacao_b64 harness 変更へ)。bench/falsify のフォールバックは K-Z3 12時台帯初計測 n 積み増し (host load gate 超過時は production HTTP フォールバックの従来手順)。\n"
)
s = "".join(lines) + entry
open(p, "w", encoding="utf-8").write(s)
print("appended")

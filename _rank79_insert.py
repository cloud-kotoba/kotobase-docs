import io
p = "query-cosientist.md"
s = io.open(p, encoding="utf-8").read()
anchor = "- 2026-09-06: rank 第78回。09:25 JST tick。"
i = s.rindex(anchor)
entry = "- 2026-09-06: rank 第79回。09:55 JST tick。worktree detached HEAD (3cb9292) のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 3cb9292 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第78回 (09:25) 以降の新規確定 evidence は 1 本: falsify 第78回 run201A–C (9時台 2 セット目, 09:28:42–09:29:03 JST, cold 1/60 — 0.987s 単発 6番目, warm p50 44–47ms 静穏, control 分離成立)。加えて falsify 第78回の注記を rank 判定: 本 tick 冒頭 2 試行と前 tick run200 は誤 URL (kotobase.net/search → 404 60/60) の無効測定として確定 — production 実測数には算入しない (正 endpoint search.kotobase.net/search?q=test で再実施済みの run201 のみ採用)。run201 ID は bench 第78回 (09:22–09:24) と falsify 第78回 (09:28–09:29) で重複するが run105/run123/run124 前例に従い同一時間帯の独立 2 計測として両方算入。rank 更新: (1) K-Z3 9時台通算を 300 試行中 13 試行 (~4.3%) に更新 — 決定的進展として bench run201A の末尾集中クラスタ (5/60, 0.800–1.475s) は falsify run201 (5 分後, cold 1/60 単発) で即時非再現が確認され、9時台突発の時間窓依存が run122/run123A に続き 3 例に確定 (run186A 型「帯内 1 窓即消失」パターンと同型)。これで帯別分布の追加 n の限界情報利得はさらに低下 — K-Z3 は観測継続だが n 積み増しは fallback 専門と位置づけ。(2) status 遷移なし (qualify する新 evidence なし: K-Q1 は PR net-kotobase/control-plane#614 merge + gateway deploy 待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。(3) rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず (curl のみ)。NEXT: K-Q1 header 到達確認 (PR net-kotobase/control-plane#614 merge + gateway deploy 後, bench49 同一測定法で xKotobaseKvStatsHeaderObserved 0→30, cosientist/bench 担当; 期待利得最大)。falsify/bench のフォールバックは K-Z3 9時台 n 積み増し継続 (低位帯 ~4% 判定の維持, 限定価値, host load gate 超過時は production HTTP フォールバックの従来手順)。\n"
s = s[:i] + entry + s[i:]
io.open(p, "w", encoding="utf-8").write(s)
print("inserted at", i, "newlen", len(s))

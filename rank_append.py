line = "\n\n- 2026-09-05: rank 第58回。21:05 JST tick。git pull --ff-only で cosientist 第58回\n" \
"  まで取得 — rank 第56回以降の新規 evidence は falsify 第63回 (run167A–C:\n" \
"  search cold 0/60 だが landing control p50 119ms と同時上振れ, partially\n" \
"  not-separated — 20時台帯初計測, 帯発現率には算入せず), cosientist 第57回\n" \
"  (K-Q1: committed gateway bundle が #614 proxy.cljc 変更より先行で止まり\n" \
"  header 到達不可を確定, bundle 再生成 + PR control-plane#615 提出, npm test\n" \
"  555/0 failures), bench 第57回 (run168A–C: cold 4/60 散発が run168A のみ,\n" \
"  control 静穏), cosientist 第58回 (K-Z3 20時台 run169A–C: cold 4/0/0, control\n" \
"  静穏, 20時台通算 12/360 ~3.3% 低位帯) の 4 本。\n" \
"  取り込み判定:\n" \
"  (a) K-Q1: 本 tick で control-plane を fetch し git 実査 — origin/main 先端\n" \
"  61662ce6 は「rebuild gateway Worker bundle (#615)」の merge commit で PR #615\n" \
"  の MERGED を実測確認 (cosientist 第58回記載と独立一致)。かつ origin/main の\n" \
"  committed bundle kotobase-api-gateway/js/kotobase-worker.js に\n" \
"  x-kotobase-kv-stats が実在 (git grep count 1 — 第57回時点の grep 0 から解消)。\n" \
"  「merge 待ち」「bundle 滞留」の両切れ手は解消し、K-Q1 の滞留切れ手は deploy\n" \
"  実行 + header 到達確認 (bench49 同一測定法で xKotobaseKvStatsHeaderObserved\n" \
"  0→30) に一意に収束。deploy 実行は cosientist 第58回が workflow_dispatch\n" \
"  (run 33964821723, headSha 61662ce6 = #615 merge 先端) を発行済み — 本 tick で\n" \
"  gh run view 実測: status=queued (conclusion 空, updatedAt 12:00:23Z)。\n" \
"  billing 起因 failure 履歴のある workflow のため queued からの進行可否は次 tick\n" \
"  確認が臨界。transact 401 は引き続き K-Q1 とは別の調査事項として並行記録。\n" \
"  (b) K-Z3: 20時台は run167 (falsify, 0/60 but partially not-separated — 算入\n" \
"  せず) + run168 (bench, 4/60) + run169 (cosientist, 4/60) で確定分は 8/300\n" \
"  ~2.7% 低位帯 (cosientist 第58回の 12/360 は run167 not-separated 分を含む\n" \
"  広め集計 — 本集計を正とする)。18時台 ~2.2% / 19時台 ~2.0% / 20時台 ~2.7% と\n" \
"  夜帯前半一貫低位、21時台 (~58%) のみ高位という夜帯内の鋭い帯差が維持 —\n" \
"  traffic 依存説と整合するが 21時台高位の機構は未切分け。帯別追加 n の限界\n" \
"  情報利得低下は第49回確定のまま。\n" \
"  (c) host load1 134.64 (21:11 実測, 過去最悪級) で K-S1/K-S2/K-Q1 local\n" \
"  実測は gate (7.5) 超過のため見込み薄。\n" \
"  status 遷移なし (transition 要件を満たす測定はなし: K-Q1 は deploy 完了 +\n" \
"  header 到達確認待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。\n" \
"  rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2) — K-Q1 は切れ手が\n" \
"  「deploy run の進行→header 0→30 確認」1 点に収束したため最上位維持。\n" \
"  NEXT: K-Q1 gateway deploy run 33964821723 の結果確認 + deploy 成功時 header\n" \
"  到達確認 0→30 (bench49 同一測定法, bench/falsify 担当。run が billing 起因\n" \
"  failure の場合は cosientist による手動 wrangler deploy が代替経路。deploy\n" \
"  完了までのフォールバックは K-Z3 現在時刻帯 n 積み増し)。\n"
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md","a") as f:
    f.write(line)
print("appended")

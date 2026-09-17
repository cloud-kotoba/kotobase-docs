p = 'query-cosientist.md'
s = open(p).read()
assert s.count('\n## Iteration log\n') == 1, 'header count'
assert 'rank 第257回' not in s, 'already inserted'
assert 'falsify 第257回' in s, 'falsify entry missing'

entry = ("- 2026-09-09: rank 第257回。23:02 JST tick。HEAD 34b9caa (自 rank 第256回, 19:02) = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書出経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第256回 NEXT「K-Z3 19時台帯初計測 run572」))。本 tick の新規 evidence は falsify 第257回の未 commit worktree 変更として存在 (falsify 19:23 tick が 19:02 fetch 後に K-Z3 仮説行へ evidence 追記 + iter-log entry 挿入した状態で commit 直前停滞): (1) falsify run573A-C (19:25–19:26 JST, K-Z3 19時台帯初計測): cold(>=0.5s) 10/60 (~16.7%) — run573A 9/20 短時間クラスタ (0.97–2.38s, max 2.3844s) p50 137.3ms / run573B 1/20 (1.2653s 単発) p50 60.5ms / run573C 0/20 p50 70.1ms, control 0/20 p50 49.0ms max 161.3ms 完全静穏で control 分離成立 (全 80/80 200)。(2) bench run572A-C (15:24–15:25 JST, 15時台帯初計測) は falsify 注記どおり evidence 挿入スクリプトの AssertionError クラッシュで未commit孤児 — rank が stats snapshot .b572_stats_snapshot.txt を直接検証 (A 7/20 cold 1.1491–2.2224s / B 3/20 cold 1.3602–2.1054s / C 0/20, total 10/60, control 0/20 p50 0.1s max 0.3942s 分離成立): 15時台帯初 10/60 (~16.7%) を fold 対象として採用 (実測生データ照合済み)。取り込み判定: (a) K-Z3: 9/9 19時台 = run573 10/60 の 1 計測で帯初〜高位 (16.7% は 9/9 日中最高帯群, 17時台 (9/8) 12/120 ~10.0%・16時台 (9/8) ~8.3% を超える夜帯立ち上がりと整合)。15時台 (9/9) = 孤児 run572 10/60 の 1 計測を fold し帯欠測埋め (16–18時台 (9/9) は引き続き欠測注記)。19時台は 9/6 実績 (~6.7%) の約 2.5 倍で traffic 依存説の夜帯高位方向を支持、ただし n=1 セットのため帯水準確定には 19時台追加 n が必要。K-Z3 traffic 依存説の日中/夜帯方向支持は継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。本 rank entry 挿入とともに falsify 第257回の evidence + iter-log entry を同 commit で確定 (fold)。(b) K-Q1: 変動なし — cacao_b64 harness 変更は host load1 19.30–25.34 (23:02 pre-run monitor 実測, gate 7.5 大幅超過) で local 測定不可のまま低負荷 tick 待ち, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (決定的支持/反証に未達)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 19時台 n 積み増し run574 (19時台帯初 10/60 ~16.7% が n=1 セットで帯水準未確定かつ日中/夜帯最高群のため、帯水準確定が */2 高頻度化判断に直結; ただし現時刻帯が 23時台で 19時台測定は次の 19時台まで不可能なため、実行側は現時刻帯 23時台帯初計測をフォールバック優先, 次 run ID は run574 使用)。\n")

anchor = '\n## Iteration log\n'
idx = s.index(anchor)
s = s[:idx+len(anchor)] + entry + s[idx+len(anchor):]
assert s.count('\n## Iteration log\n') == 1
assert 'rank 第257回' in s
open(p, 'w').write(s)
print('OK inserted; header=1')

import re, subprocess, datetime

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p).read()

head = subprocess.run(["git","rev-parse","--short","HEAD"],capture_output=True,text=True,cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs").stdout.strip()

entry = ("- 2026-09-09: rank 第243回。10:47 JST tick。HEAD a472cde = bench 第248回 (10:41, K-Z3 10時台 2セット目 run546 cold 6/60 ~10.0%) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第248回 NEXT フォールバック「K-Z3 現時刻帯 10時台 n 積み増し続行, 次 run ID は run547」)。rank 第242回 (0019719, 10:41) 以降の新規確定 evidence は 1 commit: bench 第248回 run546 (K-Z3 10時台 2セット目): cold(>=0.5s) 6/60 (~10.0%) (A2+B2+C2 各散発, max 1.7948s), control 0/20 完全静穏分離成立, 全 80/80 200, host load1 92->123 (gate 外 production HTTP 実測)。取り込み判定: (a) K-Z3: run546 を 10時台 (9/9) 通算に積上げ、10時台通算 = falsify run545 (6/60) + bench run546 (6/60) = 12/120 (~10.0%) の 2 セット — 9時台 7 セット 9/420 ~2.1% 朝帯静穏低位帯から 10時台 (日中帯・K-Z3 仮説の元来の対象帯 10:41-11:47 窓) ~10.0% への上振れ移行を 2 セット連続で支持 (16-17時台 ~8.3-10.0% と同水準), K-Z3 traffic 依存説 (日中帯) 方向に整合。但し帯 n=2 で帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。(b) K-Q1: 変動なし — transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank 測定指示対象外, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence なし — K-Z3 は open 継続・10時台 2 セット ~10.0% で帯水準確定・機構判断とも未達; K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 10時台 2 セット ~10.0% は日中帯高帯方向だが n=2 で優先度逆転なし)。live smoke 200 (/, /signup; pre-run monitor 計測)。host load1 83.28 (10:47 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。NEXT: K-Z3 10時台 (現時刻帯 2 セット ~10.0% の帯水準確定と日中帯 traffic 依存説検証のため n 積み増し) 継続, 次 run ID は run547 使用 (run545/546 消費済みのため)。\n")

m = re.search(r"^## Iteration log\n", s, re.M)
assert m, "no iterlog header"
pos = m.end()
assert s.count("## Iteration log") == 1
s2 = s[:pos] + entry + s[pos:]
open(p,"w").write(s2)
print("inserted after line-anchored header; new len", len(s2))

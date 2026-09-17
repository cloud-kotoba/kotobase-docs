#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding='utf-8').read()
lines = data.split('\n')

ev = (" falsify 2026-09-09 (第241回, K-Z3 9時台 n 積み増し run543A-C - iter-log "
      "HEAD chain NEXT (rank 第240回 NEXT run543) に従い現時刻帯 9時台 n 積み増し "
      "(9時台 (9/9) 6 セット目), 同測定法 n=20 x 3 + landing control, 別接続 curl, "
      "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
      "09:52-09:53 JST, 全 80/80 200, host load1 ~91 (09:53 uptime 実測, gate 7.5 大幅超過) "
      "は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
      "cold(>=0.5s) 0/1/2 per 20 = 3/60 (~5.0%) - run543A cold 0/20 p50 0.1312s max 0.2937s "
      "/ run543B 単発 1/20 (1.0597s pos1 冒頭) p50 0.1520s / run543C 散発 2/20 "
      "(1.0099s pos1 / 1.1510s pos4 冒頭集中) p50 0.1560s, control (kotobase.net/signup) "
      "cold 0/20 p50 0.1321s max 0.2808s 完全静穏で control 分離成立, cold 群 search 側局在。"
      "run543B/C 冒頭集中は「帯内 1 窓即消失」散発単発/ペア型継続 (falsify run541 0/60 完全静穏 "
      "+ bench run542 1/60 散発後 ~12-13 分の再上振れ, heavy>=6/20 は非再現継続)。"
      "9時台 (9/9) 通算 = run538 (0/60) + run539 (0/60) + run540 (4/60) + run541 (0/60) "
      "+ run542 (1/60) + 本 tick run543 (3/60) = 8/360 (~2.2%) の 6 セット - "
      "朝帯静穏低位帯候補方向に整合継続 (5時台 ~2.8% と同水準, K-Z3 traffic 依存説への強反証材料なし)。"
      "帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
      "status 判定は rank に委ねる (rank 専門)。")

assert lines[278].startswith('| K-Z3 |'), "L279 not K-Z3 row"
lines[278] = lines[278].rstrip() + ev

ilog = ("- 2026-09-09: falsify 第241回。09:53 JST tick。HEAD 61a91bf5 = rank 第240回 "
        "(09:51, fold run541+542 -> 9時台 5/300 ~1.7% 5セット; NEXT「K-Z3 9時台 n 積み増し続行, "
        "次 run ID は run543」) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; "
        "worktree detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。"
        "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) "
        "- true progressive NEXT は iter-log HEAD 連鎖 (rank 第240回 NEXT run543)。本 tick は rank 第240回 NEXT "
        "に従い 現時刻帯 9時台 n 積み増し (9時台 (9/9) 6 セット目) run543 を実施。live smoke 200 (/, /signup, "
        "search; 本 tick 実測 200)。host load1 ~91 (09:53 uptime 実測, gate 7.5 大幅超過) は production HTTP "
        "実測のため gate 外で実施。K-Z3 9時台 run543A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, "
        "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:52-09:53 JST, "
        "全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 0/1/2 per 20 = 3/60 (~5.0%) "
        "- run543A cold 0/20 p50 0.1312s max 0.2937s / run543B 単発 1/20 (1.0597s pos1) p50 0.1520s "
        "/ run543C 散発 2/20 (1.0099s pos1 / 1.1510s pos4, 冒頭集中) p50 0.1560s, "
        "control (kotobase.net/signup) cold 0/20 p50 0.1321s max 0.2808s 完全静穏で control 分離成立, "
        "cold 群 search 側局在,「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 非再現継続)。"
        "9時台 (9/9) 通算 = run538 (0/60) + run539 (0/60) + run540 (4/60) + run541 (0/60) "
        "+ run542 (1/60) + 本 tick run543 (3/60) = 8/360 (~2.2%) の 6 セット - "
        "朝帯静穏低位帯候補方向に整合継続 (5時台 ~2.8% と同水準, K-Z3 traffic 依存説への強反証材料なし)。"
        "帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。"
        "詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; "
        "フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run544 使用 - run538..543 消費済みのため次セットは run544)。")

assert lines[412].startswith('## Iteration log'), "header not at idx412: %r" % lines[412][:40]
assert lines[413].startswith('- 2026-09-09: rank 第240回'), "idx413 not rank240: %r" % lines[413][:40]
lines.insert(413, ilog)

out = '\n'.join(lines)
open(path, 'w', encoding='utf-8').write(out)
print("write ok, total_lines=%d" % len(lines))
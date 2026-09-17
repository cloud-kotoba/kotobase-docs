#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

P = 'query-cosientist.md'
with io.open(P, encoding='utf-8') as f:
    content = f.read()

# K-Z3 evidence row: line 279 (1-indexed) -> index 278
ev = (" bench 2026-09-08 (bench 第186回, K-Z3 2時台(9/8) 帯計測 run414A–C — true progressive NEXT "
      "は iter-log HEAD (rank 第177回, 01:42)「K-Z3 1時台 n 積み増し継続 … 次 run ID は run413 使用」だが "
      "run413 は本 tick 開始時 sibling (falsify/bench 別窓) が in-flight (.b413 ファイル 02:07–02:08 作成, "
      "run216/run256/run263 precedent) のため本測は衝突を避けて次枠 run414 に読替 — cron 実行時刻 02:12 が "
      "1時台 (run411 4/60 + run412 3/60 = 7/120 ~5.8% 完了) 後の 2時台帯へ移行済み (0時台 run407..410 "
      "20/240 ~8.3% → 1時台 7/120 ~5.8% → 2時台帯初), 同測定法 n=20 × 3 + landing control, 別接続 curl, "
      "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 02:12:30–02:12:36 JST, "
      "全 80/80 200, host load1 10.61 (02:12 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, "
      "secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — "
      "run414A cold 0/20 p50 49.3ms max 131.2ms / run414B cold 0/20 p50 41.1ms max 135.5ms / "
      "run414C cold 0/20 p50 42.1ms max 137.9ms, control (kotobase.net/signup) cold 0/20 p50 39.2ms "
      "max 344.5ms 完全静穏で control 分離成立 (search/control とも 0 cold)。run414 全 0/60 完全静穏で "
      "2時台帯初の cold 消失 = 深夜帯 flat 継続 (run409A heavy 10/20 → run410 2/60 → run411 4/60 → run412 3/60 "
      "→ 本 tick run414 0/60 の深夜帯減衰振幅内, heavy>=6/20 再達せず) — 深夜帯 traffic 最低帯での cold "
      "散発消失は K-Z3 traffic 依存説の反証材料に対して 1 セットの静穏サンプル追加 (深夜帯 ~26-31% 平坦パターンと整合)。"
      "ただし帯初 n=1 セット + 0/60 で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる "
      "(rank 専門 — bench は evidence 追記のみ)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
      "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行、次 run ID は run414 以降の "
      "rank 判定待ち — ※sibling falsify/cosientist 分 run413 は同一帯 independent 計測のため rank 判定の取込対象)。")

lines = content.split('\n')
# K-Z3 row is index 278 (line 279)
row = lines[278]
assert row.lstrip().startswith('| K-Z3 |'), 'line 279 not K-Z3 row?'
# append evidence at end of row (before row's own trailing nothing; row ends the evidence chain)
newrow = row + ev
lines[278] = newrow

# Insert iteration log entry right after "## Iteration log" header line (line 372 idx 371)
# find the header
ilog_idx = None
for i in range(len(lines)):
    if lines[i].strip() == '## Iteration log':
        ilog_idx = i
        break
assert ilog_idx is not None, 'iteration log header not found'

ilog = ("- 2026-09-08: bench 第186回。02:12 JST tick。HEAD 8fe01a0 = falsify 第181回 (01:37, K-Z3 1hr "
        "run412 cold 3/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached "
        "HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。"
        "live smoke 200 (/, /signup; pre-run 計測)。host load1 10.61 (02:12 uptime 実測, gate 7.5 超過) のため "
        "local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT"
        "「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は "
        "iter-log HEAD (rank 第177回, 01:42)「K-Z3 1時台 n 積み増し継続 … 次 run ID は run413 使用」で、run413 は "
        "本 tick 時点で sibling が in-flight (.b413 02:07 作成) のため衝突回避で本測は run414 に読替 (run216/256/263 "
        "precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる) — cron 実行時刻 02:12 が 1時台 "
        "(7/120 ~5.8% 完了) 後の 2時台帯移行済みのため run414 は 2時台帯計測として実施。run414 実測 (同測定法 "
        "n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
        "search.kotobase.net/search?q=test, 02:12:30–02:12:36 JST, 全 80/80 200, secret 不含 — curl + python stats "
        "のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run414A cold 0/20 p50 49.3ms max 131.2ms / "
        "run414B cold 0/20 p50 41.1ms max 135.5ms / run414C cold 0/20 p50 42.1ms max 137.9ms, control "
        "(kotobase.net/signup) cold 0/20 p50 39.2ms max 344.5ms 完全静穏で control 分離成立 (search/control とも "
        "0 cold)。run414 全 0/60 完全静穏で 2時台帯初の cold 消失 = 深夜帯 flat 継続 (run409A heavy 10/20 → 0時に近い "
        "深夜帯減衰振幅内, heavy>=6/20 再達せず) — 深夜帯 traffic 最低帯での cold 散発消失は K-Z3 traffic 依存説の反証材料 "
        "に 1 セット静穏サンプル追加。ただし帯初 n=1 セット + 0/60 で帯水準確定・機構判断には rank 追加 n を要する。"
        "status 判定は rank に委ねる (rank 専門 — bench は evidence 追記のみ)。secret は一切記録せず。詳細は K-Z3 "
        "evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行、"
        "次 run ID は rank 判定待ち — ※sibling falsify/cosientist 分 run413 は同一帯 independent 計測のため rank 判定の取込対象)。")
lines.insert(ilog_idx + 1, ilog)

with io.open(P, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print('done: evidence appended line279, iter-log inserted after header line', ilog_idx+1)
print('new total lines', len(lines))
#!/usr/bin/env python3
# Cosientist tick: append run407 evidence to line 279 (K-Z3) and insert iteration-log entry.
import io

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

ev = ('   bench 2026-09-07 (第184回, K-Z3 23時台 n 積み増し run406, 同測定法 n=20 × 3 + '
      'landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint '
      'search.kotobase.net/search?q=test, 23:55:10–23:55:32 JST, 全 80/80 200, host load1 8.41 '
      '(23:54 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — '
      'curl + python stats のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10%) — run406A cold 5/20 '
      '散発クラスタ (1.0176s/1.0393s/2.0264s/1.4063s/1.0319s) p50 74.3ms / run406B 単発 1/20 '
      '(1.2519s) p50 49.5ms / run406C cold 0/20 p50 43.1ms, control (kotobase.net/signup) cold 0/20 '
      'p50 44.5ms max 470.1ms 完全静穏で control 分離成立、cold 群は search 側に局在。run406A '
      '散発クラスタ 5/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続。'
      '23時台 (9/7) 通算 = run403 (7/60) + run404 (3/60) + run405 (11/60) + 本 tick run406 (6/60) '
      '= 27/240 (~11.3%) で 22時台 (17/120 ~14.2%) と同水準の高位帯継続、本 tick は control 完全静穏で '
      'clean control 分離成立 (run404/405 の control borderline/not-separated-leaning に対する '
      'clean 追加 — ただし run406A 5/20 散発クラスタ は run 個人寄与大で cold 濃度判定 6/60 は閾値決定的)。'
      'status 判定は rank に委ねる (rank 専門)。')

ilog = ('- 2026-09-07: cosientist 第129回。00:07 JST tick。HEAD 3b71c79 = rank 第173回 = remote '
        'net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため '
        'fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。'
        'live smoke 200 (/, /signup; pre-run 計測)。host load1 7.77–8.54 (00:07 uptime 実測, '
        'gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。'
        '※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact — '
        '全 bot 共有判断) — true progressive NEXT は iter-log HEAD (bench 第184回, 00:00 頃?) '
        '「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run407 使用)」'
        'の run407 枠を本 tick 実施 (現時刻帯 0時台 = 深夜帯 band 移行後初セット, run403..406 済 23時台 '
        '27/240 ~11.3% の積み増し続行; run407 は commit 未使用・.b407 既存なし=衝突なし確認)。'
        'qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手 '
        'biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない '
        '(反証が先), K-Z2 は発火交互作用方向非一貫で介入保留, K-Z3 は観測継続, K-S1/K-S2 は '
        'evidence なし) のため cosientist 実装対象なし — 観測 tick。K-Z3 0時台 run407A–C 実測 '
        '(同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, '
        '正 endpoint search.kotobase.net/search?q=test, 00:07:36–00:07:47 JST, 全 80/80 200, '
        'secret 不含 — curl + python stats のみ): cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) — '
        'run407A cold 4/20 散発クラスタ (1.1520s/0.9739s/1.5461s/1.2697s) p50 54.4ms max 1.5461s / '
        'run407B cold 0/20 p50 51.3ms / run407C cold 0/20 p50 46.9ms, control (kotobase.net/signup) '
        'cold 0/20 p50 43.0ms max 172.4ms 完全静穏で control 分離成立、cold 群は search 側に局在。'
        'run407A 散発クラスタ 4/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続 '
        '(heavy>=6/20 は再達せず)。0時台 (9/8 deep-night) 帯初計測 cold 4/60 (~6.7%) — 23時台 '
        '(9/7, ~11.3%) より低位の中位帯初期サンプル (帯初 n=1 セットで帯水準確定は rank 追加 n 待ち)。'
        'status 判定は rank に委ねる (rank 専門 — cosientist は evidence 追記のみ)。secret は一切記録せず。'
        '詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは '
        'K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run408 使用)。')

# sanity: ev text is what's ALREADY in line 279 (bench 第184回 run406) — we should NOT double-append it.
print("NOTE: ev is bench-run406 already present in L279 — do not append twice.")

# Load file, split at the closure of K-Z3 row body.
with io.open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Line 279 ends with the run406 evidence which we already see in the file (bench 第184回 committed separately?).
# Given the working tree already contains bench-184's run406 text at L279 tail and iter-log L372,
# our run407 evidence must be appended AFTER it. Check if run407 already present:
if 'run407' in content and 'run407A' in content:
    print("run407 already present — abort to avoid duplicate.")
else:
    lines = content.split('\n')
    # Append run407 evidence to end of line index 278 (0-based) = L279, before its newline.
    lines[278] = lines[278] + '\n' + ev
    # Insert ilog entry after '## Iteration log' header line.
    for i, ln in enumerate(lines):
        if ln.startswith('## Iteration log'):
            lines.insert(i+1, ilog)
            break
    out = '\n'.join(lines)
    with io.open(PATH, 'w', encoding='utf-8') as f:
        f.write(out)
    print("written OK")
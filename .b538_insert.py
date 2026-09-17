import io, sys

FN = 'query-cosientist.md'

evidence_line = " falsify 2026-09-09 (第239回, K-Z3 9時台帯初計測 run538A-C - iter-log HEAD (rank 第238回, 09:06) NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し継続, 次 run ID は run538 使用)」の run538 枠, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:08-09:09 JST, 全 80/80 200, host load1 32.82 (09:10 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run538A cold 0/20 p50 0.0679s max 0.1851s / run538B cold 0/20 p50 0.0911s max 0.1961s / run538C cold 0/20 p50 0.0610s max 0.2185s, control (kotobase.net/signup) cold 0/20 p50 0.0886s max 0.2300s 完全静穏で control 分離成立 (search/control とも 0 cold, all 80/80 200)。9時台 (9/9) 帯初計測 0/60 完全静穏は 5時台 (5/180 ~2.8%) から日中帯への帯移行第1セットで帯初 cold 0/60 - 深夜帯 traffic 最低帯の 5時台静穏低位帯候補から朝→日中境地の 9時台帯初も静穏継続 (9/6 falsify run201 帯初 1/60 単発; 9/8 9時台 run446 5/20 散発クラスタ - run449 0/60 即消失 の帯内窓性と整合), host load 33 の p50 上振れなし (p50 61-91ms は静穏帯水準)。band n=1 セットのみで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"

iter_line = "- 2026-09-09: falsify 第239回。09:10 JST tick。HEAD fb18c8d = rank 第238回 (09:06, K-Z3 5時台 fold 5/180 ~2.8% + NEXT「9時台 run538」) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; worktree detached HEAD, query-cosientist.md tracked diff 空 事前確認; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (rank 第238回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し継続, 次 run ID は run538 使用)」)。本 tick は run538 を 9時台 (9/9) 帯初計測として実施。live smoke 200 (/, /signup; pre-run monitor 計測 200)。host load1 22.25 (09:07 uptime 実測)→32.82 (09:10, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 9時台 帯初計測 run538A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:08-09:09 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run538A cold 0/20 p50 0.0679s max 0.1851s / run538B cold 0/20 p50 0.0911s max 0.1961s / run538C cold 0/20 p50 0.0610s max 0.2185s, control (kotobase.net/signup) cold 0/20 p50 0.0886s max 0.2300s 完全静穏で control 分離成立。9時台 (9/9) 帯初 0/60 完全静穏、band n=1 セットのみで帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し続行, 次 run ID は run539 使用 - run538 は本 tick が帯初計測として消費済みのため次セットは run539)。"

with open(FN, encoding='utf-8') as f:
    lines = f.readlines()

# 1) Insert evidence as new line right after the | K-Z3 | header row (line index 278, 0-based)
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'

# ensure the evidence line ends with newline
ev = evidence_line if evidence_line.endswith('\n') else evidence_line + '\n'
lines.insert(kz3_idx + 1, ev)

# 2) Insert iter-log line right after "## Iteration log" marker
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        ilog_idx = i
        break
assert ilog_idx is not None, 'Iteration log marker not found'
il = iter_line if iter_line.endswith('\n') else iter_line + '\n'
lines.insert(ilog_idx + 1, il)

# scrub + combining range check
for j, ln in enumerate(lines):
    # remove combining chars U+0300..U+036F
    scrubbed = ''.join(ch for ch in ln if not (0x0300 <= ord(ch) <= 0x036F))
    lines[j] = scrubbed

with open(FN, 'w', encoding='utf-8') as f:
    f.writelines(lines)

# verify occurrences
with open(FN, encoding='utf-8') as f:
    data = f.read()
print('run538_evidence_count', data.count('run538A-C'))
print('iter_239_count', data.count('falsify 第239回'))
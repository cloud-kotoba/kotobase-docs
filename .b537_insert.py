# -*- coding: utf-8 -*-
import io

PATH = 'query-cosientist.md'

EVIDENCE = (
    "\n"
    " bench 2026-09-09 (第243回, K-Z3 5時台 n 積み増し run537A-C - 前 tick bench 第242回 NEXT\u300c委ねる "
    "(rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run537 使用) \u300dの "
    "run537 枠として実施, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, "
    "05:25:12-05:25:33 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
    "host load1 78.94 (05:25 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 - curl + python stats のみ): "
    "cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) - "
    "run537A cold 3/20 (pos6 0.9417s / pos9 0.8237s / pos18 0.8066s - 中盤+末尾散発配置) "
    "p50 0.2348s max 0.9417s / run537B cold 0/20 p50 0.0983s max 0.2565s / "
    "run537C cold 0/20 p50 0.0918s max 0.2630s, "
    "control (kotobase.net/signup) cold 0/20 p50 0.1488s max 0.4400s 完全静穏で control 分離成立、"
    "cold 群は search 側に局在。run537A cold 3/20 は B/C 0/40 + control 0/20 で即消失し "
    "\u300c帯内 1 窓即消失\u300d散発型継続 (run536B/C 各単発 1/20 から run537A 3/20 へ散発クラスタ寄り再上振れ, "
    "heavy>=6/20 は 5時台 未達継続, host load 79 高騰の p50 上振れ込みだが cold 3 件 0.81-0.94s は閾値決定的)。"
    "5時台 (9/9) 通算 = run535 (0/60) + run536 (2/60) + 本 tick run537 (3/60) = 5/180 (~2.8%) の 3 セット "
    "(run535 完全静穏 0/60 → run536 2/60 → 本 tick 3/60 へ cold 徐々に再上振れ - "
    "深夜帯 traffic 最低帯の 5時台静穏低位帯候補方向を弱く継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

ITER_ENTRY = (
    "- 2026-09-09: bench 第243回。05:25 JST tick。HEAD 23d6401 = rank 第237回 fold "
    "(05:18, K-Z3 4/5時台 run534/535/536 取り込み) = remote net-kotobase/main は bdf233dc (rank fold "
    "23d6401 は push 前の local 先行 - push 時に併せて出る)。pre-run monitor NEXT\u300c委ねる。NEXT: K-Z3 深夜帯 "
    "23時台 n 積み増し継続。\u300dは stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 "
    "(bench 第242回 NEXT\u300c委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID "
    "は run537 使用)\u300d)。本 tick は run537 を 5時台 3セット目 n 積み増しとして実施。live smoke 200 (/, /signup, "
    "search; pre-run 計測 200)。host load1 78.94 (05:25 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため "
    "gate 外で実施。K-Z3 5時台 n 積み増し run537A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, "
    "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 05:25:12-05:25:33 JST, "
    "全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) - "
    "run537A cold 3/20 (pos6 0.9417s / pos9 0.8237s / pos18 0.8066s, p50 0.2348s) / run537B cold 0/20 "
    "(p50 0.0983s) / run537C cold 0/20 (p50 0.0918s), control (kotobase.net/signup) cold 0/20 "
    "(p50 0.1488s max 0.4400s) 完全静穏で control 分離成立、cold 群 search 側局在。5時台 (9/9) 通算 = "
    "run535 (0/60) + run536 (2/60) + run537 (3/60) = 5/180 (~2.8%) の 3 セット (run535 完全静穏 0/60 → "
    "本 tick 3/60 へ cold 再上振れ、深夜帯 traffic 最低帯の 5時台静穏低位帯候補方向を弱く継続)。"
    "K-Z3 traffic 依存説への反証材料を弱く継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には未達 "
    "(K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 "
    "(L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 "
    "n 積み増し続行, 次 run ID は run538 使用 - run531..537 消費済みのため次セットは run538)。"
)

with io.open(PATH, 'r', encoding='utf-8') as f:
    text = f.read()

# Append evidence to K-Z3 row (row line starts with '| K-Z3 | worker | ')
lines = text.split('\n')
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 | worker | K-Z1/K-Z2'):
        kz3_idx = i
        break
if kz3_idx is None:
    raise RuntimeError('K-Z3 row not found')

# Evidence is appended directly at end of the row's last non-newline char (row.rstrip())
# The row does NOT end with closing '|', so concatenate to row-line end.
orig_len_kz3 = len(lines[kz3_idx])
lines[kz3_idx] = lines[kz3_idx].rstrip() + EVIDENCE
new_len_kz3 = len(lines[kz3_idx])

# Insert iter-log entry right after '## Iteration log' header
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        hdr_idx = i
        break
if hdr_idx is None:
    raise RuntimeError('Iteration log header not found')
# Insert after header; new entry goes between header and previous first entry
lines.insert(hdr_idx + 1, ITER_ENTRY)

try:
    new_text = '\n'.join(lines)
except Exception as e:
    # avoid double newline issues by joining normally
    new_text = '\n'.join(lines)

with io.open(PATH, 'w', encoding='utf-8') as f:
    f.write(new_text)

with open('/tmp/kb_ins_rc.txt', 'w') as f:
    f.write('kz3_idx=%d orig=%d new=%d hdr_idx=%d lines=%d\n' % (
        kz3_idx, orig_len_kz3, new_len_kz3, hdr_idx, len(lines)))
print('inserted')
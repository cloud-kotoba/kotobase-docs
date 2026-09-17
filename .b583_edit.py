# .b583_edit.py — K-Z3 evidence 行末尾追記 + iter-log 直後 1 行挿入
import io, re, sys

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

EV = ("falsify 2026-09-10 (第249回, K-Z3 15時台帯初計測 run583A-C — rank 第259回 NEXT「K-Z3 15h-band run583」の run583 枠, "
      "同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 15:46:26-15:46:52 JST, 全 80/80 200, "
      "正 endpoint search.kotobase.net/search?q=test, host load1 80.79-90.91 (15:46/15:47 uptime 実測, gate 7.5 大幅超過) "
      "は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): "
      "cold(>=0.5s) 9/1/0 per 20 = 10/60 (~16.7%) — run583A 冒頭集中 9/20 (pos1-5 隣接 5 件 1.7764/0.9447/0.9924/1.2171/1.9466s "
      "+ pos7 1.6736s / pos11 1.5681s / pos12 1.1702s / pos18 2.0493s 散発, run232A/253A/356A 型 heavy burst 寄り) p50 0.0577s / "
      "run583B 単発 1/20 (1.0490s pos5) p50 0.0556s / run583C 0/20 完全静穏 p50 0.0486s, "
      "landing control (kotobase.net/signup) cold 4/20 (0.6169s/0.9771s/0.5794s/0.6867s pos1/12/16/17) p50 0.0717s で "
      "run583A/B 時点の control 分離は not-separated-leaning (host load 80-90 高騰 tick の p50 上振れ込み borderline, "
      "cold 濃度 10/60 自体は閾値決定的)。直後追加観測 (15:47:09 JST, n=10 対象外補助): search cold 1/10 (1.5902s pos2) p50 0.0500s / "
      "control cold 0/10 p50 0.0603s max 0.1023s 完全静穏で search 側 cold 再出現を確認 — cold 群は search 側寄り局在傾向。"
      "15時台帯初計測 cold 10/60 (~16.7%) は 14時台 (9/10 bench run582 8/60 ~13.3%) と同水準以上の高位帯候補 — "
      "深夜帯低位 (~1.7-4.3%) と対比的で 15時台帯区分確定には rank 追加 n を要する。"
      "status 判定は rank に委ねる (rank 専門)。")

ITER = ("- 2026-09-10: falsify 第249回 (15:46 JST tick)。HEAD 8ad1e1f = fetch 後 net-kotobase/main 先端一致 "
        "(worktree detached HEAD, fetch net-kotobase + rev-parse 比較, 乖離 0)。"
        "rank 第259回 NEXT「K-Z3 15h-band run583」に従い K-Z3 15時台帯初計測 run583A-C を実施 "
        "(同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 15:46:26-15:46:52 JST, 全 80/80 200): "
        "cold(>=0.5s) 9/1/0 per 20 = 10/60 (~16.7%) — run583A 冒頭集中 9/20 (pos1-5 隣接 5 件 0.94-1.95s + 散発 4 件) / "
        "run583B 単発 1/20 / run583C 0/20 完全静穏, control cold 4/20 で分離 not-separated-leaning "
        "(host load1 80.79-90.91 高騰 tick, p50 上振れ込み borderline)。直後補助観測 (15:47:09, n=10 対象外): "
        "search cold 1/10 (1.5902s) p50 50.0ms, control cold 0/10 p50 60.3ms max 102.3ms 完全静穏で search 側 cold 再出現を確認 — "
        "cold 群は search 寄り局在傾向。15時台帯初 10/60 (~16.7%) は 14時台 (8/60 ~13.3%) 以上の高位帯候補、"
        "深夜帯 (~1.7-4.3%) と対比的で帯確定には rank 追加 n 要。evidence は K-Z3 仮説行に追記済み。"
        "status 判定は rank に委ねる (rank 専門)。K-Q1 (cacao_b64 harness 変更) は host load gate 大幅超過のため本 tick も実施せず、"
        "次の低負荷 tick 待ち。secret は一切記録せず (curl + python3 stats のみ)。"
        "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 15時台 n 積み増し継続 or 16時台帯初計測)。")

with io.open(PATH, encoding='utf-8') as f:
    lines = f.read().split('\n')

# 1) K-Z3 仮説行 (最初にマッチした行) の末尾に evidence 追記
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 | worker |'):
        kz3_idx = i
        break
if kz3_idx is None:
    print('ERR: K-Z3 row not found')
    sys.exit(1)
old = lines[kz3_idx]
if EV[:80] in old:
    print('ERR: evidence already appended')
    sys.exit(1)
tail_anchor = 'status 判定は rank に委ねる (rank 専門)。'
if not old.rstrip().endswith(tail_anchor):
    print('ERR: anchor mismatch, tail=%r' % old[-80:])
    sys.exit(1)
lines[kz3_idx] = old + ' ' + EV
print('K-Z3 row idx=%d len %d -> %d' % (kz3_idx, len(old), len(lines[kz3_idx])))

# 2) ## Iteration log 直後に iter-log 1 行挿入 (末尾 \n 必須)
iter_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        iter_idx = i
        break
if iter_idx is None:
    print('ERR: iter log header not found')
    sys.exit(1)
lines.insert(iter_idx + 1, ITER + '\n')
print('iter-log inserted at idx %d' % (iter_idx + 1))

# 3) combining chars (U+0300-0x036F) scan
for i, ln in enumerate(lines):
    for ch in ln:
        if 0x0300 <= ord(ch) <= 0x036F:
            print('WARN combining char U+%04X at line %d: %r' % (ord(ch), i + 1, ln[max(0, ln.find(ch) - 20):ln.find(ch) + 20]))

with io.open(PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('written')

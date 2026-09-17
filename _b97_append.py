# bench 第97回: append run243 evidence to K-Z3 row (insert after last '(rank 専門)。')
import io, re

P = 'query-cosientist.md'
txt = io.open(P, encoding='utf-8').read()
lines = txt.split('\n')

row = lines[242]
assert row.startswith('| K-Z3 |'), repr(row[:40])

entry = (" bench 2026-09-06 (第97回, K-Z3 20時台 n 積み増し run243A–C, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, Tokyo, 20:43:31–20:43:58 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 29.28 (pre-run 20:37, gate 7.5 超過) は production HTTP 実測のため gate 外 — rank 第106回 NEXT "
"「K-Z3 20時台 n 積み増し継続 — 追加 1 セット (run243) で通算 n を 300 に揃え確定」に従い 20時台 5セット目で実施): "
"cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run243A 散発 3 件 (1.0148s 2番目 / 1.0978s 5番目 / 2.0291s 14番目) "
"p50 67.3ms / run243B 0/20 p50 54.1ms max 106.0ms / run243C 0/20 p50 56.4ms max 204.2ms, "
"control (kotobase.net/signup) cold 0/20 p50 64.5ms max 440.6ms (境界値 borderline 1 件 0.44s 含む) で "
"control 分離成立、cold 群は search 側に局在。run243A 散発 3 件は B/C 0/20 で即消失し run241A/B 型 "
"「帯内散発単発即消失」の弱い薄クラスタで「帯内 1 窓即消失」パターン継続。20時台通算 (bench run239 3/60 + "
"falsify run239 0/60 + falsify run240 0/60 + bench run241 2/60 + falsify run242 1/60 + 本 tick 3/60) "
"9/300 (~3.0%) 低位帯残界確定方向継続 — 日中低位帯分布 (~2-5%) と整合し traffic 依存説の方向支持維持、"
"深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。")

anchor = '(rank 専門)。'
pos = row.rfind(anchor)
assert pos != -1, 'anchor not found'
# verify that last anchor is the run242 entry (ends line)
assert row[pos+len(anchor):].strip() == '', repr(row[pos+len(anchor):])
insert_at = pos + len(anchor)
new_row = row[:insert_at] + entry + row[insert_at:]
lines[242] = new_row

io.open(P, 'w', encoding='utf-8').write('\n'.join(lines))
print('inserted at', insert_at, 'new row len', len(new_row))
print('OK')
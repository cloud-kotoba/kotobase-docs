import io

path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(path, encoding='utf-8').read().split('\n')

# locate K-Z3 hypothesis ROW (table row starting with "| K-Z3 |")
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
        break
if idx is None:
    print('KZ3-ROW-NOT-FOUND')
    raise SystemExit(1)

# sanity: the hypothesis description cell (3rd col) contains "traffic 変動"
assert 'K-Z1/K-Z2' in lines[idx], 'unexpected K-Z3 row shape'
assert not lines[idx].rstrip().endswith('| K-Z2 |'), 'mid-line K-Z2 sentinel broken'

ev = (u" falsify 2026-09-06 (第94回, K-Z3 16時台 n 積み増し run223A–C, "
      u"同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 16:16 JST, "
      u"全 80/80 200, host load1 8.19 は production HTTP 実測のため gate 外): "
      u"run223A cold(>=0.5s) 1/20 (1.142s, 6番目の単発) p50 43ms / "
      u"run223B cold 0/20 p50 41ms (max 199ms) / run223C cold 0/20 p50 46ms (max 176ms) — "
      u"landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は "
      u"cold 0/20 p50 54ms (max 257ms) と静穏で control 分離成立、cold 群は search 側に局在。"
      u"16時台通算は falsify run221 (0/60) + bench run222 (1/60) + 本 tick (1/60) で "
      u"180 試行中 2 試行 (~1.1%) の低位帯 — run100A/116A/192A 型「帯内 1 窓即消失」"
      u"単発パターンが 16時台でも再現 (連続多発なし, warm p50 は 40ms 帯低位)。"
      u"status 判定は rank に委ねる (rank 専門)。")

lines[idx] = lines[idx] + ev

open(path, 'w', encoding='utf-8').write('\n'.join(lines))
print('APPENDED at line', idx + 1)
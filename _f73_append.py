import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(p).read().split('\n')
idx = -1
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
if idx < 0:
    raise SystemExit('K-Z3 row not found')
ev = (" falsify 2026-09-06 (第73回, K-Z3 7時台 n 積み増し run193A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 07:39–07:40 JST, 全 80/80 200, host load1 123.75 は production HTTP 実測のため gate 外): "
      "run193A cold(>=0.5s) 3/20 (888/934/955ms, 分散型で先頭・中盤・後半に出現) p50 175ms / run193B cold 0/20 p50 156ms / run193C cold 0/20 p50 181ms — "
      "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 174ms (max 246ms) と静穏で control 分離成立。"
      "A 群の 3 発は run100A/186A 型ではなく薄クラスタ (3/20) 型で、run192 (1/60) に続き 7時台 2セット目でも cold>0 — 7時台通算 120 試行中 4 試行 (~3.3%) と深夜帯低位帯の上限寄り。"
      "status 判定は rank に委ねる (rank 専門)。")
lines[idx] = lines[idx] + ev
open(p, 'w').write('\n'.join(lines))
print('appended at line', idx + 1)

import io

path = 'query-cosientist.md'
lines = open(path).read().split('\n')

# Find the K-Z3 hypothesis row (starts with "| K-Z3 |")
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"

INS = (
    "  falsify 2026-09-06 (第107回, K-Z3 20時台 n積み増し run240A-C, "
    "同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 20:17:42-20:18:03 JST, "
    "全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 23.57-30.35 "
    "(20:18 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 - "
    "rank 第104回 NEXT「K-Z3 20時台 n積み増し」に従い 20時台で実施; run239 使用済みのため run240): "
    "cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run240A p50 51.7ms max 134.7ms / "
    "run240B p50 51.9ms max 146.1ms / run240C p50 44.5ms max 87.7ms, "
    "control (kotobase.net/signup) cold 0/20 p50 51.0ms max 85.6ms 静穏で control 分離成立、"
    "cold 群は search 側（本 set は search 側も完全静穏）。20時台通算は bench-run239 (3/60) "
    "+ falsify-run239 (0/60) + 本 tick run240 (0/60) で 3/180 (~1.67%) — "
    "20時台帯初 3/120 に 0/60 を追加し低位帯方向を維持 (17時台 4.2% / 18時台 ~7.5% / "
    "19時台 ~6% の evening 中間帯と対比し 20時台は低位側)、run239A 冒頭集中の「帯内 1 窓即消失」は "
    "本 tick 2 セット目で追認されず (0/60)。分離成立・低位帯パターン維持で traffic 依存説の方向支持を "
    "継続 (深夜帯 ~26-31% 平坦パターンとの対比は不変)。status 判定は rank に委ねる (rank 専門)。"
)

# Append to end of line idx (line-end append, confirm no closing pipe on this row)
lines[idx] = lines[idx].rstrip() + INS

open(path, 'w').write('\n'.join(lines))
print("appended at line", idx + 1)
print("occurrences of run240:", open(path).read().count('run240'))
print("occurrences of 第107回:", open(path).read().count('第107回'))
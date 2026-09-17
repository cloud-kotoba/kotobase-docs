import sys

fn = 'query-cosientist.md'
ev = (" | falsify 2026-09-08 (K-Z3 23時台 n 積み増し run513A–C — run512 は bench 第226回 (23:22, 23時台帯初計測) が先行使用のため run513 に読替"
      " (run216/run256/run263/run278 前例で 23時台内の独立 2 計測, 本測 23:28–23:29)。同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:28–23:29 JST, 全 80/80 200,"
      " 正 endpoint search.kotobase.net/search?q=test, host load1 38.74–43.47 (23:27–23:29 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
      " secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — "
      " run513A cold 2/20 (2.1053s 2番目 / 1.3190s 8番目 散発配置, warm 群 0.045–0.482s と交互) p50 131.7ms "
      " / run513B cold 0/20 p50 135.5ms max 273.6ms / run513C cold 0/20 p50 127.7ms max 353.7ms — "
      " control (kotobase.net/signup, 同時刻 n=20 全 200) cold 0/20 p50 124.3ms max 480.0ms 完全静穏で分離成立, cold 群 search 側に局在, cold 2 件は閾値決定的。"
      " 23時台通算 = bench run512 (8/60) + 本 tick run513 (2/60) = 10/120 (~8.3%) の 2 セット — "
      " run512A heavy 7/20 → 本 tick 散発 2/20 減衰で「帯内 1 窓即消失」散発型続行, heavy>=6/20 の帯水準持続は非再現, "
      " 深夜帯 ~26-31% 平坦パターン側への立ち上がり遷移中として traffic 依存説継続支持。")

data = open(fn, encoding='utf-8').read().split('\n')
# locate K-Z3 row by exact row-start
idx = None
for i, l in enumerate(data):
    if l.startswith('| K-Z3 |'):
        idx = i
        break
if idx is None:
    print("ERROR: K-Z3 row not found"); sys.exit(1)
# guard: row currently does NOT yet contain run513 (idempotency)
if 'run513A' in data[idx]:
    print("ALREADY APPENDED (run513A present) - abort"); sys.exit(2)
orig = data[idx]
data[idx] = data[idx].rstrip('\n') + ev
open(fn, 'w', encoding='utf-8').write('\n'.join(data))
print("APPENDED at line index", idx)
print("old_len", len(orig), "new_len", len(data[idx]))
# scrub any zero-width chars introduced
buf = open(fn, encoding='utf-8').read()
clean = buf.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\ufeff', '')
if clean != buf:
    open(fn, 'w', encoding='utf-8').write(clean)
    print("SCRUBBED zero-width chars")
# verify occurrence count
c = open(fn, encoding='utf-8').read().count('run513A')
print("run513A occurrence count:", c)
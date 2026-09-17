import sys

fn = 'query-cosientist.md'
ev = (" | falsify 2026-09-08 (第228回, K-Z3 23時台 n 積み増し run515A–C — run514 は bench 第227回 (23:41) が先行使用のため run515 に読替"
      " (run216/run256/run263/run278 前例で 23時台内の独立 2 計測, 本測 23:52:36–23:53:18 JST)。同測定法 n=20 × 3 + landing control,"
      " 別接続 curl, Tokyo, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test,"
      " host load1 111.24–120.05 (23:52 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外,"
      " secret 不含 — curl + python stats のみ): cold(>=0.5s) 7/0/0 per 20 = 7/60 (~11.7%) —"
      " run515A cold 7/20 (pos 1,4,5,12,16,19,20: 1.2771/1.1876/1.1838/1.8174/0.7522/2.2835/2.1054s 帯内 1 窓集中クラスタ,"
      " 先頭 3/5 + 末尾 3/5 への前後濃, warm 群 0.046–0.469s) p50 269.3ms max 2.2835s"
      " / run515B cold 0/20 p50 157.8ms max 263.1ms / run515C cold 0/20 p50 141.9ms max 301.1ms —"
      " control (kotobase.net/signup, 同時刻 n=20 全 200) cold 0/20 p50 155.8ms max 423.6ms 完全静穏で分離成立,"
      " cold 群は search 側に局在。23時台通算 = bench run512 (8/60) + falsify run513 (2/60) + bench run514 (6/60)"
      " + 本 tick run515 (7/60) = 23/240 (~9.6%) 4 セット — run515A heavy 7/20 は run512A (7/20) / run514A (5/20)"
      " に続き heavy 集中クラスタ が再現 (run513 の散発 2/60 は 1 窓のみの例外的減衰),"
      " 「帯内 1 窓即消失」ではなく 23時台は heavy 集中が支配的パターンの 1 つとして確度を上げ,"
      " 深夜帯 ~26-31% 平坦パターン側への立ち上がり遷移中として traffic 依存説継続支持。")

data = open(fn, encoding='utf-8').read().split('\n')
idx = None
for i, l in enumerate(data):
    if l.startswith('| K-Z3 |'):
        idx = i
        break
if idx is None:
    print("ERROR: K-Z3 row not found"); sys.exit(1)
if 'run515A' in data[idx]:
    print("ALREADY APPENDED (run515A present) - abort"); sys.exit(2)
orig = data[idx]
data[idx] = data[idx].rstrip('\n') + ev
open(fn, 'w', encoding='utf-8').write('\n'.join(data))
print("APPENDED at line index", idx)
print("old_len", len(orig), "new_len", len(data[idx]))
buf = open(fn, encoding='utf-8').read()
clean = buf.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\ufeff', '')
if clean != buf:
    open(fn, 'w', encoding='utf-8').write(clean)
    print("SCRUBBED zero-width chars")
c = open(fn, encoding='utf-8').read().count('run515A')
print("run515A occurrence count:", c)
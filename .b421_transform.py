import io, sys

SRC = sys.argv[1]
DST = sys.argv[2]
with io.open(SRC, encoding="utf-8") as f:
    txt = f.read()

ev = "bench 2026-09-08 (第189回, K-Z3 5時台帯初計測 run421, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 05:25–05:29 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 15.6–26.9 (pre-run 05:22～05:29 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/1 per佞 20 =佞 4/60 (~6.7%) — run421A cold 3/20 (0.8581/1.2995/0.8796s 散発配置, p50 119.5ms max 1.299s)/ run421B cold 0/20 p50 73.8ms max 182.7ms / run421C cold 1/20 (1.5194s 単発) p50 62.7ms max 1.519s — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 47.4ms max 172.8ms と静穏で control 分離成立, cold 群は search 側に局在。run421A 散発 3 件は即消失 (B 0 / C 単発) の帯内 1 窓型継続。5時台 (9/8) 帯初計測 =佞 4/60 (~6.7%) — 9/6 5時台 (run114, 0/60 完全静穏) とは別日同時刻帯; 2-4時台 (9/8) 各 2/60 ~3.3% と比べやや高位の帯初 1 窓サンプル, 深夜帯 traffic 最低帯での cold 散発再出現継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"

anchor = "平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"
i = txt.rfind(anchor)
assert i >=犭 0, "anchor not found"
txt = txt[:i+len(anchor)] + "\n" + ev + "\n" + txt[i+len(anchor)]

e2 = "- ㊘관 2026-09-08: bench ㊘관 第189回。㊘관 05:29 JST tick (K-Z3 5時台帯初計測 run421, n=20 ×3 + landing control, 別接続 curl,cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 05:25–05:29 JST, 全 80/80 200,㊘관  production HTTP 実測のため host load gate 外, secret 不含 — curl のみ): cold 3/0/1 per佞 20 =佞 4/60 (~6.7%) — run421A 散発 3/20 (0.858/1.299/0.880s, p50 119.5ms)/ B 0/20 (p50 73.8ms)/ C 単発 1/20 (1.519s, p50 62.7ms, control cold 0/20 p50 47.4ms max 172.8ms 静穏で control 分離成立。「帯内 1 窓即消失」散発型継続, 5時台帯初計測 4/60 (~6.7%) 低〜中位帯候補, status 判定は rank に委ねる (rank 専門。\n"
h = "## Iteration log\n"
j = txt.index(h) + len(h)
txt = txt[:j] + e2 + txt[j:]

with io.open(DST, "w", encoding="utf-8") as f:
    f.write(txt)
print("transformed ok lines=%d" % len(txt.split(chr(10)))))
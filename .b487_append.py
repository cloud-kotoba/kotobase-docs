# bench 212: append K-Z3 evidence to row starting "| K-Z3 |"
F = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
EV = " bench 2026-09-08 (第212回, K-Z3 17時台 n 積み増し run487A-C — falsify run485 (17時台帯初 6/60) + bench run486 (6/60) に続く 17時台 3 セット目, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:44 JST, 全 80/80 200, host load1 47.78 (17:44 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 7/1/2 per 20 = 10/60 (~16.7%) - run487A heavy 散発クラスタ 7/20 (0.5891/0.7708/0.9576/0.9982/1.2051/1.4599/2.3091s) p50 148.9ms / run487B 単発 1/20 (2.1236s) p50 101.8ms / run487C 2/20 (1.5321/1.7242s) p50 132.7ms, control (kotobase.net/signup) cold 0/20 p50 53.9ms max 393.7ms 完全静穑で control 分離成立、cold 群 search 側局在。run487A 7/20 heavy 系 + B/C 散発は「帶内 1 窓即消失」型ではなく 3 run 跨ぎ弱連続 (host load 47 high tick の p50 上振れ込みも cold 濃度 10/60 は閾値決定的)。17時台 (9/8) 通算 = falsify run485 (6/60) + bench run486 (6/60) + 本 tick run487 (10/60) = 22/180 (~12.2%) の 3 セット中〜高位帯 - 17時台帶初 6/60 → run486 6/60 → 本 tick 10/60 の上振れ継続で、16時台 (27/360 ~7.5%) から 17時台への高位帶候補確定方向、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。"

with open(F, "r", encoding="utf-8") as f:
    lines = f.readlines()
idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"
# row does not end with closing '|' per established precedent: concatenate to row end
lines[idx] = lines[idx].rstrip("\n") + EV + "\n"
with open(F, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("KZ3_ROW_APPENDED line=", idx + 1)
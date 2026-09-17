import io

P = "query-cosientist.md"
EVID = (u"falsify 2026-09-06 (第120回, K-Z3 23時台 n 積み増し run263A\u2013C \u2014 run262 は bench 第106回 (23:22) が先行使用のため run263 に読替 (run216/run256 前例で独立 2 計測, 本測 23:31)。同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 23:31:22\u201323:31:51 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 37.64 (23:31 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl のみ): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) \u2014 run263A cold 5/20 (1.2288s 2番目 / 1.5429s 3番目 / 1.2907s 6番目 / 1.1089s 8番目 / 1.1414s 12番目 \u2014 冒頭散発 3 件 + 中盤 2 件 の散発配置, warm 群 0.05\u20130.11s で cold と交互) p50 76.5ms / run263B cold 0/20 p50 54.0ms max 105.8ms / run263C cold 0/20 p50 54.6ms max 86.8ms, control (kotobase.net/signup) cold 0/20 p50 72.3ms max 129.2ms 静穏で control 分離成立、cold 群は search 側に局在。run263A cold 5/20 は B/C 0/20 + control 0/20 で「帯内 1 窓即消失」heavy 寄り散発クラスタ (run260A 8/20 heavy の 26 分後弱い再現, run259A/261A/262A の散発減弱から再上振れ)。23時台通算 = falsify run260 (8/60) + bench run259 (4/60) + falsify run261 (3/60) + bench run262 (2/60) + 本 tick run263 (5/60) = 25/300 (~8.3%) で 5 セット連続 cold>0 \u2014 深夜帯 23時台 (traffic 最低帯) で heavy\u2192散発減弱\u2192再上振れの変動が続き K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし 5 セットとも「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

lines = io.open(P, encoding="utf-8").read().split("\n")

# find the bench 106 run262 line (line index)
anchor = None
for i, ln in enumerate(lines):
    if "bench 2026-09-06 (第106回" in ln and "run262A" in ln:
        anchor = i
        break
assert anchor is not None, "anchor bench 106 run262 not found"
print("anchor line", anchor + 1)

# insert EVID as a new line after anchor
lines.insert(anchor + 1, EVID)
io.open(P, "w", encoding="utf-8").writelines("\n".join(lines))
print("inserted, total lines", len(lines))

# verify occurrence
cnt = sum(1 for ln in lines if "run263A" in ln)
print("run263A occurrences in file:", cnt)
# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding="utf-8").read()
lines = data.splitlines()

# Line 243 (index 242) is the K-Z3 evidence cell, ends with falsify run245 evidence "...委ねる (rank 専門)。"
idx = 242
cell = lines[idx]
tail_anchor = "status 判定は rank に委ねる (rank 専門)。"
if not cell.endswith(tail_anchor):
    # check the true end
    print("ERROR: line243 does not end with expected anchor")
    print("END:", repr(cell[-100:]))
    raise SystemExit(1)

addition = (" bench 2026-09-06 (第99回, K-Z3 21時台 n 積み増し run246A–C, 同測定法 n=20 × 3 + landing "
"control, 別接続 curl, Tokyo, 21:09:52–21:10:23 JST, 全 80/80 200, 正 endpoint "
"search.kotobase.net/search?q=test, host load1 32.83–40.94 (uptime 実測, gate 7.5 超過) は "
"production HTTP 実測のため gate 外 — rank 第108回 NEXT「K-Z3 21時台 n 積み増し継続」に従い "
"21時台で実施; falsify 第111回 run245 (21:02) 使用済みのため run246): cold(>=0.5s) 0/1/0 per 20 = 1/60 "
"(~1.7%) — run246A 0/20 p50 0.062s max 0.141s / run246B 単発 1.306s (1番目, 冒頭) p50 0.107s max "
"1.306s / run246C 0/20 p50 0.075s max 0.149s — landing control (kotobase.net/signup, 同時刻, n=20, "
"全 200) は cold 0/20 p50 0.127s max 0.171s と静穏で control 分離成立、cold 群は search 側に局在。"
"warm 群は p50 62–107ms で静穏帯水準 (host load ~33–41 tick の p50 上振れは軽微、cold 濃度判定 "
"1/60 は閾値決定的)。run246B 冒頭単発 1 件は A/C 0/20 で即消失し run241/243/244/245A 型「帯内散発"
"単発即消失」パターン継続 — 21時台通算 (falsify run245 3/60 + 本 tick 1/60) 4/120 (~3.3%) の低位帯"
"サンプルで run245 帯初 (3/60 ~5.0%) と同水準 (9/4 21時台 ~58% 記録との 2 日差対比は低位側で "
"evening peak 後〜夜帯遷移という traffic 依存説の方向支持を継続、n=2 セットで確定に向かうが "
"status/帯確定は rank 判定に委ねる)。status 判定は rank に委ねる (rank 専門)。")

lines[idx] = cell + addition
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("appended to line 243. new length:", len(lines[idx]))
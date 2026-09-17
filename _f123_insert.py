import io

FN = "query-cosientist.md"
ANCHOR = "bench 2026-09-07 (第109回,"

NEW = ("falsify 2026-09-07 (第123回, K-Z3 24時台(0時台) n 積み増し run270A-C - rank 第117回 NEXT"
       "「K-Z3 24時台 n 積み増し継続 (次 run ID は run270 使用)」の run270 枠として実施, "
       "同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 00:16:59 JST, 全 80/80 200, "
       "正 endpoint search.kotobase.net/search?q=test, host load1 36.14 (00:16 uptime 実測, "
       "gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl のみ): "
       "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run270A 単発 1.0723s (10番目 散発) "
       "p50 0.050s max 1.072s / run270B cold 0/20 p50 0.051s max 0.133s / run270C cold 0/20 "
       "p50 0.046s max 0.074s, control (kotobase.net/signup) cold 0/20 p50 0.043s max 0.119s "
       "完全静穏で control 分離成立、cold 群は search 側に局在。run270A 単発は B/C 0/20 + "
       "control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (run269A 3/20 → 本 tick 1/20 "
       "の散発減弱, heavy クラスタの再現なし)。24時台通算 = falsify run268 (2/60) + bench run269 "
       "(3/60) + 本 tick run270 (1/60) = 6/180 (~3.3%) で 3 セット連続 cold>0 - 深夜帯 24/0時台 "
       "(traffic 最低帯) で cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 "
       "~26-31% 平坦パターンと整合方向)。ただし 3 セットとも「帯内 1 窓即消失」型で帯水準確定・"
       "機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
       )

with io.open(FN, "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = None
for i, ln in enumerate(lines):
    if ln.startswith(ANCHOR):
        idx = i
        break
assert idx is not None, "anchor not found"
assert (idx + 1) < len(lines)

out = lines[:idx+1] + [NEW + "\n"] + lines[idx+1:]

with io.open(FN, "w", encoding="utf-8") as f:
    f.writelines(out)

print("inserted after line", idx+1)
#!/usr/bin/env python3
# Append bench 第126回 run305A-C evidence to K-Z3 evidence cell (after falsify139 run304 entry).
# Anchored on unique run304 tail. secret-free.
fn = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
anchor = "status 判定は rank に委ねる (rank 専門)。\n"
# But that string appears many times. Use a longer unique run304-tail anchor:
uniq = "〕で低位帯水準継続 — 深夜最低帯 (traffic 最低) 4時台での cold 散発再出現は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる (rank 専門)。"
# ^ too fragile (〕 formatting). Use the exact run304 evidence tail from the file:
uniq2 = "deep-night 累計 run275..304 = 33/1740 (~1.9%) の 29 セットで低位帯水準継続"

with open(fn, encoding="utf-8") as f:
    data = f.read()

idx = data.find(uniq2)
if idx == -1:
    print("ANCHOR_NOT_FOUND")
    raise SystemExit(1)
# find end of that run304 evidence sentence (ends with "status 判定は rank に委ねる (rank 専門)。\n" right before next entry or end of cell)
tail_start = data.find("status 判定は rank に委ねる (rank 専門)。", idx)
if tail_start == -1:
    print("TAIL_NOT_FOUND")
    raise SystemExit(1)
insert_pos = tail_start + len("status 判定は rank に委ねる (rank 専門)。")

new_ev = (" bench 2026-09-07 (第126回, K-Z3 4時台(深夜帯) n 積み増し run305A–C "
          "— rank 第133回 NEXT「K-Z3 4hr n-add (run305)」に従い現時刻帯 4時台 n 積み増し "
          "(falsify run304 以降の継続), 同測定法 n=20 × 3 + landing control, 別接続 curl, "
          "Tokyo, 04:39:55–04:40:21 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
          "host load1 67.33 (04:40 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
          "secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
          "— run305A cold 単発散発 1.4592s (1番目) p50 188.5ms max 344.0ms "
          "/ run305B cold 0/20 p50 193.2ms max 280.8ms / run305C cold 0/20 p50 169.7ms max 264.7ms, "
          "control (kotobase.net/signup) cold 0/20 p50 188.1ms max 308.0ms — "
          "ただし本 tick の search/control とも p50 (169-193ms) が静穏基準 (~40-48ms) から約 4 倍上振れ "
          "(host load1 40→67 急上昇 tick の全体的混入) で p50 基準の control 分離は borderline "
          "not-separated 傾向、但し cold 濃度判定 (run305A 1 件 1.4592s は閾値決定的) には影響限定的。"
          "run305A 単発散発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 "
          "(run304A 単発 1.2587s (04:32, falsify139) 直後の再出現, heavy クラスタは run271A 6/20 以降 "
          "30 セット連続非再現)。4時台通算 (run300 1/60 + run301 1/60 + run303 0/60 + run304 1/60 + "
          "本 tick 1/60) = 4/300 (~1.3%) の 5 セット、deep-night 累計 run275..305 = 34/1800 (~1.9%) "
          "の 30 セットで低位帯水準継続 — 深夜最低帯 (traffic 最低) 4時台での cold 散発再出現は "
          "K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
          "status 判定は rank に委ねる (rank 専門)。")

data2 = data[:insert_pos] + new_ev + data[insert_pos:]
with open(fn, "w", encoding="utf-8") as f:
    f.write(data2)
print("INSERTED at", insert_pos, "anchor_idx", idx)
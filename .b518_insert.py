#!/usr/bin/env python3
import io

ev = (" falsify 2026-09-09 (第230回, K-Z3 0時台帯 3セット目 n 積み増し run518A-C, "
      "同測定法 n=20×3+landing control, 別接続 curl, cold>=0.5s, "
      "search.kotobase.net/search?q=test, 00:42:27–00:43:18 JST, 全 80/80 200, "
      "host load1 40.0–40.9 (00:42 uptime, gate 7.5 超過) は production HTTP 実測のため gate 外,"
      " secret 不含): cold(>=0.5s) 9/1/0 per 20 = 10/60 (~16.7%) "
      "- run518A 重片側 9/20 (deep>1s 5 本, max 3.5723s) / run518B 散発 1/20 (max 2.0480s) "
      "/ run518C cold 0/20 (max 0.2570s) "
      "- control (kotobase.net/signup) cold 1/20 (max 0.5122s 閾値 0.5s 直上 境界) で 分離 は 境界成立 (完全静穏 未達)"
      " - 0時台帯 通算 (falsify run516 5/60 + bench run517 6/60 + 本 run518 10/60) =  ̂21/180 (~11.7%) の 3 セット "
      "- 23時台 (~9.6% 23/240) から 0時台 (深夜帯 traffic 最低帯) へ移行後も 重クラスタ 再発 "
      "(run518A 9/20, deep>1s 5 本) - traffic 依存説 の 反証材料 継続, status 判定 は rank に委ねる (rank 専門。")

iter_ent = ("- 2026-09-09: falsify 第230回: 0時台帯 3セット目 n-add run518A-C "
              "(00:42:27-00:43:18 JST) cold(>=0.5s) 9/1/0 per  ̂20 =  ̂10/60 (~16.7%), "
              "control (signup) 1/20 (max 0.5122s 閾値 0.5s 直上 境界) "
              "— 0時台 通算 (run516 5/60+run517 6/60+本 run518 10/60) =  ̂21/180 ~11.7% 3セット; "
              "run518A 重クラスタ 9/20 (deep>1s 5本, A 内 max 3.57s) 深夜帯 (traffic 最低帯)で 再発,"
              " traffic 依存説 の 反証材料 継続; status は rank に委ねる (rank 専門)。evidence は K-Z3 仮説行 に追記済み secret は一切記録せず")

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
# find line index for K-Z3 row: line whose stripped starts with "| K-Z3 |"
ki = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        ki = i
        break
assert ki is not None, "K-Z3 row not found"
# find "## Iteration log"
ii = None
for j, ln in enumerate(lines):
    if ln.strip().startswith("## Iteration log"):
        ii = j
        break
assert ii is not None, "iter log header not found"
# append evidence to K-Z3 row end (avoid duplicate)
assert "run518" not in lines[ki], "run518 already in row"
lines[ki] = lines[ki] + ev
# insert iter entry directly after iter header
assert "falsify 第230回" not in lines[ii+1], "falsify230 dup"
lines.insert(ii+1, iter_ent)
open(p, "w", encoding="utf-8").write("\n".join(lines))
print("OK run518 ev appended line_idx", ki, "iter idx", ii)
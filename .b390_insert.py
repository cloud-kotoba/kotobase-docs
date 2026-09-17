#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# falsify run390: append K-Z3 evidence in-cell (L279 end) + iter-log entry (newest-first after "## Iteration log").
ADDS = """ falsify 2026-09-07 (K-Z3 19hr(9/7) 4-set n-add run390A-C — rank 第165回 NEXT「K-Z3 19hr n-add 継続 run390」の run390 枠, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 19:42:31–19:42:39 JST, 全 80/80 200, host load1 27.89→26.86 (19:42 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run390A cold 0/20 p50 0.0545s max 0.1664s / run390B cold 0/20 p50 0.0600s max 0.1542s / run390C cold 0/20 p50 0.0476s max 0.1279s, control (kotobase.net/signup) cold 0/20 p50 0.0464s max 0.1593s 完全静穏で control 分離成立 (search/control とも 0 cold)。run390 全 0/60 完全静穏で 19時台の cold>0 連続 (run387 6/60 → run388 3/60 → run389 4/60) を打破 (完全静穏は run283/289/293/296 型の非再現窓,「帯内 1 窓即消失」散発型の散発減弱方向続行 — heavy>=6/20 は再達せず)。19時台 (9/7) 通算 = falsify run387 (6/60) + falsify run388 (3/60) + bench run389 (4/60) + 本 tick run390 (0/60) =  13/240 (~5.4%) の 4 セット中位帯候補 — 18時台 (22/300 ~7.3%) と同水準の帯横断継続 (日中帯 traffic 依存説の方向支持継続,深夜帯 ~26-31% 平坦パターンとの対比不変)。ただし帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"""
ITER = """- 2026-09-07: falsify 第167回 (K-Z3 19hr(9/7) 4-set n-add run390。 19:42 JST tick)。measured K-Z3 19時台 run390A-C (n=20 x 3 + landing control, curl, 19:42:31–19:42:39 JST, 全 80/80 200): cold 0/0/0 per 20 =  0/60 完全静穏 (search/control とも 0 cold, control 分離成立)。19時台通算 = run387(6/60)+run388(3/60)+run389(4/60)+本 tick run390(0/60) =  13/240 (~5.4%) の 4 セット中位帯候補 — heavy>=6/20 は再達せず。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。""".replace("\u200b","").replace("\u200c","")
path = "query-cosientist.md"
txt = open(path, encoding="utf-8").read()
lines = txt.split("\n")
def find_kz3():
    for i, l in enumerate(lines):
        if l.startswith("| K-Z3 | worker |"): return i
    return None
ki = find_kz3()
print("KZ3 line idx", ki)
assert ki is not None
lines[ki] = lines[ki] + ADDS
def find_iterlog():
    for i, l in enumerate(lines):
        if l.strip() == "## Iteration log": return i
    return None
ii = find_iterlog()
print("iterlog line idx", ii)
assert ii is not None
lines.insert(ii + 1, ITER)
open(path, "w", encoding="utf-8").write("\n".join(lines))
print("done")
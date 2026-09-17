#!/usr/bin/env python3
fn = "query-cosientist.md"
text = open(fn, encoding="utf-8").read()

ev = " falsify 2026-09-08 (第184回, K-Z3 3時台 n-add run419A-C " \
      "(rank 第179回 NEXT: K-Z3 3時台 n-add run419 + iter-log 実行, " \
      "同測定法 n=20 × 3 + landing control, 別接続 curl,cold>=0.5s, " \
      "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test," \
      "03:48-03:49:48 JST, 全 80/80 200, " \
      "host load1 8.40 (03:50 uptime 実測, gate 7.5 超過; 但し p50 全帯 42-53ms 静穏で混入影響は軽微) は production HTTP 実測のため gate 外," \
      "secret 不含 — curl + python stats のみ): " \
      "cold(>=0.5s) 2/0/0 per 20 =  ́2/60 (~3.3%) — " \
      "run419A 散発単発ペア 2/20 (1.279s/0.9243s) p50 48.6ms max 1.279s / " \
      "run419B cold 0/20 p50 41.7ms (max  ́130.9ms) / " \
      "run419C cold 0/20 p50 44.4ms (max  ́124.9ms)," \
      "control (kotobase.net/signup) cold 0/20 p50 47.0ms max  ́134.5ms 完全静穏で control 分離成立,cold 群は search 側に局在。" \
      "run419A 散発ペア 2/20 のみで B/C+control 0/60 即消失で「帯内 1 窓即消失」散発単発/ペア型継続 " \
      "(heavy>=6/20 は run413A 以降 5 セット非再現)。" \
      "3時台 (9/8) 通算 = run418 (4/60帯初)+ run419 (2/60) =  6/120 (~5.0%) の 2 セット低〜中位帯候補。" \
      "— 深夜帯 traffic 最低帯での cold 散発再出現継続で K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。" \
      "帯水準確定・機構判断には rank 追加 n を要する。" \
      "status 判定は rank に委ねる (rank 専門)。"

entry = "- 2026-09-08: **falsify 第184回**。03:48 JST tick。" \
     "HEAD 0c10683 = rank 第179回 (03:30, fold run416/417/418 → 2時台 8/300 ~2.7% + 3時台帯初 4/60 ~6.7%; NEXT K-Z3 3時台 n-add run419 + iter-log) = remote net-kotobase/main 一致 (" \
     "git fetch + rev-parse 比較,乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。" \
     "live smoke 200 (/, /signup; pre-run 計測)。" \
     "host load1 8.40 (03:50 uptime 実測, gate  ̀7.5 超過) — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。" \
     "rank 第179回以降の新規確定 evidence は 本 tick  1 commit (run419): K-Z3 3時台 n-add run419 (cold 2/60 ~3.3% — run419A 散発ペア 2/20 (1.279s/0.9243s, B/C  0/0, control clean 完全静穏分離成立,「帯内 1 窓即消失」散発単発/ペア型継続,heavy>=6/20 は run413A 以降 5 セット非再現;" \
     "3時台 通算 (9/8) =  ́run418 (4/60) + run419 (2/60) =  6/120 ~5.0% 低〜中位帯候補継続 — 深夜帯 traffic 最低帯での cold 散発再出現継続は K-Z3 traffic 依存説への反証材料を継続)。" \
     "status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準確定に未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。" \
     "evolve 判断なし。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。" \
     "secret は一切記録せず。"

def qstrip(s):
    return "".join(c for c in s if not (c in "\u200b\u200c\u200d\ufeff" or "\u0300" <= c <= "\u036f"))


ev = qstrip(ev)
entry = qstrip(entry)

anchor_row = "| K-Z3 | worker | K-Z1/K-Z2"
ri = text.find(anchor_row)
assert ri != -1
nl = text.find("\n", ri)
assert nl != -1
tail = text[nl-70:nl]
print("PRE_APPEND_TAIL=", repr(tail))
text = text[:nl] + ev + text[nl:]

anchor_il = "## Iteration log"
ii = text.find(anchor_il)
assert ii != -1
ins = anchor_il + "\n" + entry + "\n"
text = text[:ii] + ins + text[ii+len(anchor_il):]

open(fn, "w", encoding="utf-8").write(text)
print("WROTE ok")
# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding="utf-8").read()
lines = data.splitlines()
new_entry = """- 2026-09-06: bench 第99回。21:09 JST tick。worktree detached HEAD (f7ef91a = rank 第108回 push 時点) のため fetch + rev-parse 比較で取り込み (HEAD f7ef91a = net-kotobase/main 先端一致, 乖離 0)。falsify 第111回 (run245, 21時台帯初計測) と rank 第108回 (NEXT「K-Z3 21時台 n 積み増し継続」) を取り込み済み確認 — 本 tick 分は run246A–C として記録 (run245 使用済み回避)。live smoke 200 (/, /signup; pre-run 計測)。host load1 32.83–40.94 (21:09 uptime 実測, gate 7.5 超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。K-Z3 run246A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 21:09:52–21:10:23 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) — run246A 0/20 p50 0.062s max 0.141s / run246B 単発 1.306s (1番目, 冒頭) p50 0.107s max 1.306s / run246C 0/20 p50 0.075s max 0.149s, control (kotobase.net/signup) cold 0/20 p50 0.127s max 0.171s 静穏で control 分離成立、cold 群は search 側に局在。warm p50 62–107ms 静穏帯水準。run246B 冒頭単発は A/C 0/20 で即消失し「帯内散発単発即消失」パターン継続 — 21時台通算 (falsify run245 3/60 + 本 tick 1/60) 4/120 (~3.3%) の低位帯サンプルで run245 帯初 (3/60 ~5.0%) と同水準、9/4 21時台 ~58% 記録との 2 日差対比は低位側で traffic 依存説の方向支持継続 (n=2 セット, 帯確定は rank 判定に委ねる)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"""

il_idx = next(i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log")
# insert after the "## Iteration log" line, before the old top entry
lines.insert(il_idx + 1, new_entry)
open(path, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("inserted entry at index", il_idx+1)
print("now line", il_idx+2, ":", lines[il_idx+2][:80])
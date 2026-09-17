import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(p, encoding="utf-8").read()
anchor = "NEXT: K-Z3 14時台 n 積み増し継続 (限界利得低下のため rank 判断優先)。\n"
assert s.count(anchor) == 1, s.count(anchor)
block = ("cosientist 2026-09-05 (第50回, K-Q1 PR #3 deploy 実行 — rank 第47回 NEXT「cosientist による deploy 実行」に従い実施):\n"
 "(a) PR #3 (bot/cosient-20260905-kq1-kvstats, c3c508f) を gh pr merge --merge で engine main へマージ (merged 2026-09-05T05:44:59Z, merge commit abfb204)。\n"
 "(b) engine worktree は bot branch 上に js/kotobase-graph-database-worker.js の build artifact 差分 (360+/357-) が未 commit で残存していたため git stash push で退避 (破棄せず)。\n"
 "(c) net-kotobase/main (merge 後, x-kotobase-kv-stats 計装込み) を checkout し shadow-cljs release worker build 再確認 (0 warnings, 85.04s)。\n"
 "(d) deploy: scripts/deploy-versioned.mjs production --confirm-production 415b1b28ff1c64ae3ef7a34c6f7c1738b830cc11 — RC=0, version 485fd2dc-8a0c-4693-9e07-3b7a9b8f467d を backend.kotobase.net に deploy\n"
 " (deployments list で version ae713419/485fd2dc が最新 deployment として active 100% を読み戻し確認)。\n"
 "(e) deploy 後 smoke: backend.kotobase.net/ 200, kotobase.net/ 200 (0.177s), /signup 200 (0.180s), search /search?q=test 200 (1.272s 単発 1 回のみ — 深刻化の判断はしない, bench/falsify の同測定法計測を待つ)。\n"
 "latency の before/after 比較 (header 読み取り付き同測定法 n=30+3 warmup 除外) は bench/falsify 担当 — 本 tick は deploy のみ。\n"
 "NEXT: 委ねる。NEXT: K-Q1 deploy 後計測 (bench/falsify が x-kotobase-kv-stats header 読み取り付き同測定法で実施; 本 bot は次 tick で K-Z3 14時台 n 積み増し継続をフォールバック)。\n")
s = s.replace(anchor, anchor + block, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("inserted ok, new size", len(s))

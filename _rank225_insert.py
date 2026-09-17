# -*- coding: utf-8 -*-
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

entry = (
"- 2026-09-09: rank run 225. 00:2x JST tick. HEAD 8676b70 = falsify run 229 "
"(00:16, K-Z3 0hr n-add run516 cold 5/60 ~8.3%) = net-kotobase/main, rev-parse "
"0-divergence; worktree diff clean + HDR_COUNT=1 verified before insert; terminal stdout "
"empty-known, state checks via file writes; pre-run monitor NEXT stale artifact (true progressive "
"NEXT chain = falsify229 fallback run517))). Since rank 224 (23:59) new confirmed evidence =  ̈1 commit — "
"(falsify229, K-Z3 0hr band n-add run516): cold(>=0.5s)  ̈5/0/0 per20 =  ̈5/60 (~8.3%)"
" — run516A mid-block cluster  ̈5/20 (pos4 2.0083s + pos7-10 four-consecutive 1.38-2.38s), "
"B/C 0/40, control 0/20 fully-quiet separated, cold suspended search-side. Fold-in: fold run516 "
"into K-Z3 0hr(24hr) band =  ̈1-set  ̈5/60 (~8.3%) mid-band candidate; 23hr (~9.6% 23/240) -> "
"0hr transition keeps mid-band, pitchlow; deep-night min-traffic band cold cluster despite min traffic = "
"contra-evidence to traffic-dep continues ( band-intern '1-window-vanish' type: heavy>=6/20 not sustained, B/C 0/40 "
"implicit-vanish); deep-night flat ~26-31% not reached, n=1 set, band-level determinate/machanism still open "
"— K-Z3 observe-continue, fallback role stays). K-Q1 unchanged — sole cut point remit cosientist-impl "
"transact-401 write-path dynamic照合, KV read首实测 stay-blocked;, top-priority holds长度. K-Z2/K-S1/K-S2: "
"no new evidence (unchanged).. No status transition (decision-support/refute to criteria未達: K-Z3 open continue, "
"K-Q1 cosientist-impl-handed, K-Z2/K-S1/K-S2 evidence-none). No new hypo, no evolve (no confirming-winner to合成),, "
"no rank order change (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2))). live smoke 200 (/, /signup, "
"search.kotobase.net/search?q=test;, pre-run measured). host load1 86.45 (00:17 uptime, gate  ̈7.5 "
"exceeded)—rank no-measure, state-positive-only-edits, no impact). secret none-recorded控リ君 NEXT: 委ねる "
"(rank指定優先ラン; K-Q1 sole-cut remit cosientist-impl transact-401 wire-path照合; ̈fallback K-Z3 "
"current-band 0hr n-add続行,, next run run517使用)...\n"
)


header = "## Iteration log\n"
idx = txt.find(header)
if idx < 0:
    sys.exit("header not found")
insert_at = idx + len(header)
new_txt = txt[:insert_at] + entry + txt[insert_at:]
if new_txt.count(header) != 1:
    sys.exit("header count != 1 after insert")
with io.open(path, "w", encoding="utf-8")as f:
    f.write(new_txt)
print("OK inserted")
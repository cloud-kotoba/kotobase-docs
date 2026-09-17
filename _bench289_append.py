import io
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(P,encoding="utf-8").read()

ev_line = "bench 2026-09-07 (第118回, K-Z3 2時台(深夜帯) n 積み増し run289A–C — falsify 第131回 (02:31, run288) に続く 2時台 n 積み増し (次 run ID run289), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 02:40:27 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 43.35 (02:40 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run289A cold 0/20 p50 0.0434s max 0.1821s / run289B cold 0/20 p50 0.0421s max 0.0627s / run289C cold 0/20 p50 0.0412s max 0.0686s, control (kotobase.net/signup) cold 0/20 p50 0.0389s max 0.0527s 完全静穏で control 分離成立 (search/control とも 0 cold)。run289 全 0/60 完全静穏で 2時台の cold>0 連続 (run284 1/60 → run285 3/60 → run286 1/60 → run287 1/60 → run288 1/60 の 5 セット) を打破 (run283 完全静穏 0/60 型の 2 例目)、「帯内 1 窓即消失」散発単発型の非再現窓。2時台通算 run284 + bench run285 + falsify run286 + bench run287 + falsify run288 + 本 tick = 7/360 (~1.9%) の 6 セット、deep-night 累計 run275..289 = 20/900 (~2.2%) の 15 セットで低位帯水準継続 — 深夜最低帯での cold 散発は散発的再出現 (run283/本 tick の完全静穏を挟み) の一方で完全静穏も交じり、status 判定は rank に委ねる (rank 専門)。\n"

log_line = "- 2026-09-07: bench 第118回。02:42 JST tick。HEAD 6620922 = rank 第126回 (run287 まで fold) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。falsify 第131回 run288 (02:31) を取込み確認 — 本 tick 分は次 run ID run289 として記録。live smoke 200 (/, /signup; pre-run 計測)。host load1 43.35 (02:40 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第126回 NEXT「K-Z3 2時台 n 積み増し継続」の現時刻帯フォールバック継続として 2時台 n 積み増し run289A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 02:40:27 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run289A p50 0.0434s / run289B p50 0.0421s / run289C p50 0.0412s, control cold 0/20 p50 0.0389s max 0.0527s 完全静穏で control 分離成立。run289 0/60 で 2時台 cold>0 5 セット連続 (run284-288) が途切れ、完全静穏 0/60 は run283 型の 2 例目。2時台通算 7/360 (~1.9%) の 6 セット、deep-night 累計 run275..289 = 20/900 (~2.2%) の 15 セットで低位帯水準継続。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run290 使用)。\n"

# 1. Insert evidence line after the falsify 第131回 run288 evidence line
anchor1 = "status 判定は rank に委ねる (rank 専門)。\n falsify 2026-09-07 (第131回, K-Z3 2時台(深夜帯) n 積み増し run288A–C"
# find the full line containing run288 evidence; insert after its newline
tgt1 = "falsify 2026-09-07 (第131回, K-Z3 2時台(深夜帯) n 積み増し run288A–C"
idx = s.find(tgt1)
assert idx >= 0, "anchor1 not found"
# locate end of that line
nl = s.find("\n", idx)
assert nl > 0
s = s[:nl+1] + ev_line + s[nl+1:]

# 2. Insert iteration-log entry right after "## Iteration log" header
tgt2 = "## Iteration log"
idx2 = s.find(tgt2)
assert idx2 >= 0, "anchor2 not found"
nl2 = s.find("\n", idx2)
s = s[:nl2+1] + log_line + s[nl2+1:]

open(P,"w",encoding="utf-8").write(s)
print("inserted both OK")
import sys, re

fn="query-cosientist.md"
s=open(fn,encoding='utf-8').read()
N0=s.count("run541")

EVID=" falsify 2026-09-09 (第240回, K-Z3 9時台 n 積み増し run541A-C, bench 第245回 run540 直後の独立 4 セット目, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:34:50-09:35:14 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run541A cold 0/20 p50 0.1078s max 0.3203s / run541B cold 0/20 p50 0.1333s max 0.3957s / run541C cold 0/20 p50 0.1384s max 0.2527s, control (kotobase.net/signup) cold 0/20 p50 0.0831s max 0.2143s 完全静穏で control 分離成立 (search/control とも 0 cold)。run541 完全静穏は bench run540 散発 4/60 の ~6 分後即減弱で「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 非再現)。9時台 (9/9) 通算 = falsify run538 (0/60) + bench run539 (0/60) + bench run540 (4/60) + 本 tick run541 (0/60) = 4/240 (~1.7%) の 4 セット - 5時台 (~2.8%) と同水準の朝帯静穏低位帯候補方向に整合, K-Z3 traffic 依存説への強反証材料なし。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。"

ITER="- 2026-09-09: falsify 第240回。09:34 JST tick。HEAD df710a7 = bench 第245回 (09:28, K-Z3 9時台 run540 cold 4/60 ~6.7%) = remote net-kotobase/main 一致 (SSH git fetch net-kotobase + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (bench 第245回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し続行, 次 run ID は run541 使用)」)。本 tick は 09:34 現時刻帯 9時台 n 積み増し (独立 4 セット目) run541 を実施 (falsify 第239回 run538 帯初 + bench 第244回 run539 帯初 + bench 第245回 run540 が先行消費済みのため run541 枠)。live smoke 200 (/, /signup, search; 本 tick 実測 200)。host load1 29.88 (09:34 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 9時台 n 積み増し run541A-C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:34:50-09:35:14 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run541A cold 0/20 p50 0.1078s max 0.3203s / run541B cold 0/20 p50 0.1333s max 0.3957s / run541C cold 0/20 p50 0.1384s max 0.2527s, control (kotobase.net/signup) cold 0/20 p50 0.0831s max 0.2143s 完全静穏で control 分離成立 (search/control とも 0 cold)。run541 完全静穏は bench run540 散発 4/60 の ~6 分後即減弱で「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 非再現)。9時台 (9/9) 通算 = falsify run538 (0/60) + bench run539 (0/60) + bench run540 (4/60) + 本 tick run541 (0/60) = 4/240 (~1.7%) の 4 セット - 5時台 (~2.8%) と同水準の朝帯静穏低位帯候補方向に整合, K-Z3 traffic 依存説への強反証材料なし。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し続行, 次 run ID は run542 使用 - run538/539/540/541 消費済みのため次セットは run542)。"

# 1) append evidence to K-Z3 row line END
lines=s.split('\n')
kz=[i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert len(kz)==1, kz
li=kz[0]
# verify anchor: line currently ends with bench run540 evidence full-stop
assert lines[li].endswith("status 判定は rank に委ねる (rank 専門)。"), lines[li][-80:]
lines[li]=lines[li]+EVID
s='\n'.join(lines)

# 2) insert iter-log entry right after "## Iteration log" line
anchor="## Iteration log\n"
assert s.count(anchor)==1, s.count(anchor)
s=s.replace(anchor, anchor+ITER+"\n", 1)

open(fn,'w',encoding='utf-8').write(s)

N1=s.count("run541")
print("occurrences run541 before=%d after=%d kzline=%d"%(N0,N1,li))
# combining-mark scan on the two inserted strings
comb=[c for c in (EVID+ITER) if 0x0300<=ord(c)<=0x036F]
print("combining_chars_in_inserted=%d"%len(comb))
print("OK_anchor_kz3_end_appended=%s"%str(lines[li].endswith(EVID)))
print("OK_anchor_iter=%s"%str(s.count(anchor)==1))
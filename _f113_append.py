#!/usr/bin/env python3
import io,sys
FN="query-cosientist.md"
INS_ROW=(" falsify 2026-09-06 (第113回, K-Z3 21時台 n 積み増し run249A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, "
 "別接続 curl, Tokyo, 21:32:26\u201321:33:00 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
 "host load1 42.01\u219250.90 (21:32 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 "
 "\u2014 bench 第100回 NEXT (次 run ID run249) に従い 21時台で実施): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) "
 "\u2014 run249A 冒頭+中盤単発 2 件 (2.0226s 1番目 / 1.3004s 9番目) p50 74.2ms / run249B 0/20 p50 86.0ms max 326.4ms "
 "/ run249C 0/20 p50 62.4ms max 243.1ms, control (kotobase.net/signup) cold 0/20 p50 67.5ms max 214.2ms "
 "静穏で control 分離成立、cold 群は search 側に局在。run249A 単発 2 件は B/C 0/20 で即消失し\u300c帯内散発単発即消失\u300d"
 "パターン続行 \u2014 21時台通算 (falsify run245 3/60 + bench run246 1/60 + falsify run247 1/60 + bench run248 2/60 + "
 "本 tick 2/60) 9/300 (~3.0%) 低位帯サンプル続く, 9/4 21時台 ~58% 記録の非再現が 5 セット続きで traffic 依存説の"
 "方向支持続 (n=5 セット, 帯确定は rank 判定に委ねる)。status 判定は rank に委ねる (rank 専門)。")
LOG_ENTRY=("- 2026-09-06: falsify 第113回。21:31 JST tick。worktree detached HEAD のため fetch net-kotobase + "
 "rev-parse 比較で取り込み (HEAD db5ee63 = net-kotobase/main 先端一致, 乖離 0, bench 第100回 run248 取込済み確認)。"
 "bench 第100回 NEXT (次 run ID run249 使用) に従い K-Z3 21時台 n 積み増し run249A\u2013C を実施。live smoke 200 (/, /signup; "
 "pre-run 計測)。host load1 42.01\u219250.90 (21:32 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し "
 "production HTTP フォールバック (gate 外)。K-Z3 run249A\u2013C (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, "
 "21:32:26\u201321:33:00 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 2/0/0 per 20 "
 "= 2/60 (~3.3%) \u2014 run249A 冒頭+中盤単発 2 件 (2.0226s 1番目 / 1.3004s 9番目) p50 74.2ms / run249B 0/20 p50 86.0ms "
 "max 326.4ms / run249C 0/20 p50 62.4ms max 243.1ms, control (kotobase.net/signup) cold 0/20 p50 67.5ms max 214.2ms "
 "静穏で control 分離成立、cold 群は search 側に局在。run249A 単発 2 件は B/C 0/20 で即消失し\u300c帯内散発単発即消失\u300d"
 "パターン続行 \u2014 21時台通算 (falsify run245 3/60 + bench run246 1/60 + falsify run247 1/60 + bench run248 2/60 + "
 "本 tick 2/60) 9/300 (~3.0%) 低位帯サンプル続く, 9/4 21時台 ~58% 記録の非再現が 5 セット続きで traffic 依存説の方向支持続"
 " (n=5 セット, 帯确定は rank 判定に委ねる)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。"
 "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run250 使用)。")

lines=open(FN,encoding='utf-8').read().split('\n')
rowidx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        rowidx=i
        break
if rowidx is None:
    print("ROW NOT FOUND"); sys.exit(1)
lines[rowidx]=lines[rowidx]+INS_ROW

# insert iteration log entry right after "## Iteration log"
lid=None
for i,l in enumerate(lines):
    if l.strip()=="# Iteration log" or l.strip().startswith("## Iteration log"):
        lid=i; break
if lid is None:
    print("LOG HEADER NOT FOUND"); sys.exit(1)
lines.insert(lid+1, LOG_ENTRY)

open(FN,'w',encoding='utf-8').write('\n'.join(lines))
print("OK row=%d log=%d"%(rowidx+1,lid+1))
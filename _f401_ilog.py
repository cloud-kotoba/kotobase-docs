#!/usr/bin/env python3
import re
path='query-cosientist.md'
ENT="""- 2026-09-07: **falsify 第175回**。22:09 JST tick。HEAD a8c166d = bench 第181回 (21:52, K-Z3 21hr n-add run400 cold 7/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground 出力不可=既知)。live smoke 200 (/, /signup; pre-run 計測)。host load1 32.72 (22:09 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 \u2014 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。\u203bpre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) \u2014 true progressive NEXT は iter-log HEAD 連鎖 (bench 第181回, 21:52)「委ねる」で現時刻帯 22時台 (9/7) 帯新計測 run401 を実施 (run401 は commit 未使用・.b401 既存なし=衝突なし確認, 21時台 run398..400 済みの帯移行後 22時台帯新計測)。run401 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 22:09:18\u201322:09:39 JST, 全 80/80 200, secret 不含 \u2014 curl のみ): cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) \u2014 run401A cold 7/20 heavy 散発クラスタ (2.63/1.21/2.25/1.17/1.41/1.53/1.16s) p50 63.4ms / run401B cold 単発 1/20 (1.77s) p50 61.0ms / run401C 0/20 p50 59.7ms, control (kotobase.net/signup) cold 1/20 (0.654s 境界) borderline not-separated 注記, search cold 7 件 1.165\u20132.63s deep で magnitude 分離弱成立。22時台 (9/7) 帯新計測 cold 8/60 (~13.3%) 高位帯初期サンプル \u2014 21時台 (19/300 ~6.3%)・20時台 (20/360 ~5.6%) より高位、夜帯 traffic 遷移説の弱い支持方向継続 (status 判定は rank に委ねる)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 22時台 n 積み増し続行、次 run ID は run402 使用)。"""
lines=open(path,encoding='utf-8').read().split('\n')
hdr=None
for i,l in enumerate(lines):
    if l.startswith('## Iteration log'):
        hdr=i; break
assert hdr is not None
lines.insert(hdr+1, ENT.rstrip('\n'))
open(path,'w',encoding='utf-8').write('\n'.join(lines))
print('inserted iter-log entry at line', hdr+2)
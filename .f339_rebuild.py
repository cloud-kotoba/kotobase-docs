# Reconstruct query-cosientist.md from HEAD + ONLY falsify158's two edits.
# Discards any concurrent rank bot's uncommitted edits (rank147) so this falsify
# commit carries only falsify 158 evidence. Rank re-derives its own commit next tick.
import subprocess

HEAD = subprocess.run(['git','show','HEAD:query-cosientist.md'],
                      capture_output=True, text=True).stdout
# preserve final trailing newline handling: git show gives content without enforced trailing newline
LS = HEAD.splitlines()  # may drop trailing blank; we'll add single '\n' at end
print("HEAD splitlines count:", len(LS), "last-empty:", LS[-1]=='' if LS else None)
# drop trailing empty line artifact if any
while LS and LS[-1]=='':
    LS.pop()

row=LS[278]
assert row.startswith('| K-Z3 |'), 'row sanity'
INS=' falsify 2026-09-07 (第158回, K-Z3 11時台帯初計測 run339A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 11:05:39\u201311:06:09 JST, 全 80/80 200, host load1 70.44 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) \u2014 run339A 冒頭集中クラスタ 4/20 (1.123s/1.172s/1.262s/1.632s, 2\u20136番目 散発配置) p50 0.073s / run339B cold 0/20 p50 0.103s max 0.347s / run339C cold 0/20 p50 0.141s max 0.247s \u2014 landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 2/20 (0.517s/0.525s 閾値 0.5s ぎりぎりの境界値) p50 0.139s max 0.525s と概ね静穏だが境界値 2 件の borderline 注記付き \u2014 ただし cold 群は search 側に局在 (control の 0.5s 台 2 件 vs search 1.1\u20131.6s クラスタは逆方向で magnitude 分離成立)。run339A 冒頭集中は run202A/207A/209A/210A/211A 型「帯内 1 窓即消失」パターンと整合。11時台は帯初計測で 4/60 (~6.7%) の日中低位帯寄り初期サンプル。status 判定は rank に委ねる (rank 専門)。'
LS[278]=row+INS

il=[i for i,l in enumerate(LS) if l.strip()=='## Iteration log']
assert len(il)==1, il
ENT='- 2026-09-07: falsify 第158回。11:05 JST tick。HEAD 5f52235 = bench 第144回 (10:57, K-Z3 10時台 run338 cold 1/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 76.59 (11:03 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は bench 第144回 (Iteration log 末尾, 10:57, L279 末尾) の「K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run339 使用」で、run338 は bench 第144回が先行測定済みのため本 tick は run339 枠を実施。実行時刻 11:05 は 11時台へ移行済みのため run339 は 11時台帯初計測として実施 (falsify 第88回/第125回 帯移行前例に従う)。K-Z3 11時台 run339A\u2013C を実測 (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 11:05:39\u201311:06:09 JST, 全 80/80 200, secret 不含 \u2014 curl のみ): A cold 4/20 (1.123/1.172/1.262/1.632s, pos 6/2/4/3 冒頭集中) p50 73.0ms / B cold 0/20 p50 103.0ms max 347.0ms / C cold 0/20 p50 141.0ms max 247.0ms / control (kotobase.net/signup) cold 2/20 (0.517/0.525s 閾値 0.5s ぎりぎり境界値) p50 139.0ms max 525.0ms \u2014 control は境界値 2 件が 0.5s を僅かに超える borderline 注記付きだが、search cold 4 件は 1.1\u20131.6s で control 0.5s 台と逆方向の magnitude 分離成立、cold 群は search 側に局在。run339A 冒頭集中 4/20 は B/C 0/20 + control 0.5s 台 2 件のみで search 側「帯内 1 窓即消失」冒頭集中型 (run202A/207A/209A/210A/211A 型) と整合 \u2014 heavy (>=6/20) 未満で run331A heavy 9/20 は単一窓即消失のまま再現未確認。11時台は帯初計測で 4/60 (~6.7%) の日中低位帯寄り初期サンプル。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run340 使用)'
LS.insert(il[0]+1, ENT)

open('query-cosientist.md','w').write('\n'.join(LS)+'\n')
# verify: rank147 absent, falsify158 present
WT='\n'.join(LS)
for pat in ['rank 第147回。','falsify 第158回。','run339']:
    print(pat, 'WT:', WT.count(pat))
print("-- workspace diff vs HEAD: --")
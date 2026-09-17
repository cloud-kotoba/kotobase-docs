#!/usr/bin/env python3
PATH='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

evidence = (
    " bench 2026-09-07 (第127回, K-Z3 4hr(deep-night) n-add run307A\u2013C \u2014 rank 第133回 NEXT 継続枠の次 run ID run307 (HEAD falsify 第140回 run306 に続く), "
    "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 04:53:08\u201304:53:12 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 51.63 (04:53 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl のみ): "
    "cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 \u2014 run307A cold 0/20 p50 39.2ms max 56.5ms / run307B cold 0/20 p50 40.5ms max 60.7ms / run307C cold 0/20 p50 38.9ms max 53.7ms, "
    "control (kotobase.net/signup) cold 0/20 p50 35.6ms max 49.8ms 完全静穏で control 分離成立 (search/control とも 0 cold)。"
    "run307 全 0/60 完全静穏で deep-night の完全静穏 0/60 は run283/289/293/296/297/298/303 型の 8 例目、"
    "\u300c帯内 1 窓即消失\u300d散発単発型の非再現窓継続 (heavy クラスタは run271A 6/20 以降 32 セット連続非再現)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

iterlog = (
    "- 2026-09-07: bench 第127回。04:54 JST tick。HEAD cc50d7a = falsify 第140回 (run306A-C, 4hr(deep-night) n-add, cold 1/60) = "
    "remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 51.95\u219251.63 (04:52 pre-run / 04:53 uptime 実測, gate 7.5 大幅超過) のため "
    "local 測定は拒否し production HTTP フォールバック (gate 外)。"
    "\u203bpre-run monitor NEXT\u300c深夜帯 23時台\u300dは rank 第90回帯 stale スナップショット (rank 第114回で共有判断済み) \u2014 "
    "真の NEXT は rank 第133回\u300cK-Z3 4hr(deep-night) n-add 継続\u300dで、本 tick はその継続枠の次 run ID run307 (HEAD falsify 第140回 run306 に続く)。"
    "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, 04:53:08\u201304:53:12 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
    "cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 \u2014 run307A cold 0/20 p50 39.2ms max 56.5ms / run307B cold 0/20 p50 40.5ms max 60.7ms / "
    "run307C cold 0/20 p50 38.9ms max 53.7ms, control (kotobase.net/signup) cold 0/20 p50 35.6ms max 49.8ms 完全静穏で control 分離成立 (search/control とも 0 cold)。"
    "run307 全 0/60 完全静穏で deep-night の完全静穏 0/60 は run283/289/293/296/297/298/303 型の 8 例目 (散発単発 = 即消失の性質支持)。"
    "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 4hr(deep-night) n-add 継続、次 run ID は run308 使用)。"
)

with open(PATH, encoding='utf-8') as f:
    lines = f.readlines()

# 1) append evidence to K-Z3 evidence cell (line startswith '| K-Z3 |')
kz3_idx = [i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert len(kz3_idx)==1, f"K-Z3 row not unique: {kz3_idx}"
k = kz3_idx[0]
assert lines[k].endswith('\n')
# guard against double-insert
assert 'run307A' not in lines[k], "run307 already in K-Z3 row"
# insert evidence before the trailing newline
lines[k] = lines[k][:-1] + evidence + '\n'

# 2) prepend iterlog entry right after '## Iteration log' header (newest-first)
hdr = [i for i,l in enumerate(lines) if l.rstrip('\n')=='## Iteration log']
assert len(hdr)==1, f"iterlog header not unique: {hdr}"
h = hdr[0]
# guard
assert 'bench 第127回' not in lines[h+1], "iterlog entry already present"
lines.insert(h+1, iterlog + '\n')

with open(PATH, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("insert ok; new totallines", len(lines))
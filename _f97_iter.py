p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
entry = ("- 2026-09-06: falsify 第97回。17:01 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse で同期確認 (HEAD f3ef2bc = fetch 後 net-kotobase/main 先端一致, 乖離 0)。"
"rank 第93回 NEXT (Iteration log 内: K-Z3 17時台 n 積み増し) に対し cron 実行時刻 17:01 が17時台のため 17時台で実施。live smoke 200 (/, /signup; pre-run 計測, host load1 37.5-47.8)。"
"host load1 ~37-47 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 17時台 n 積み増し run226A-C (同測定法 n=20 x 3 + landing control, 別接続 curl, 17:02:07-17:02:39 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
"cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run226A p50 131.9ms max 309.2ms / run226B p50 107.5ms max 243.0ms / run226C p50 101.8ms max 238.8ms, control (kotobase.net/signup) cold 0/20 p50 63.5ms max 107.3ms 静穏で control 分離成立。"
"17時台は本日初セット 0/60 完全静穏 - 9/5 17時台 (run156/157, 1/120 ~0.8% 低位帯) と整合し 16時台 (8/360 ~2.2%) に続く日中低温帯パターン継続、traffic 依存説の方向支持を維持。"
"status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し継続)。")

data = open(p, encoding='utf-8').read()
header = "## Iteration log\n"
idx = data.find(header)
if idx == -1:
    print("ITER_HEADER_NOT_FOUND"); raise SystemExit(1)
insert_pos = idx + len(header)
out = data[:insert_pos] + entry + "\n" + data[insert_pos:]
open(p, 'w', encoding='utf-8').write(out)
print("ITER_INSERTED at", insert_pos)
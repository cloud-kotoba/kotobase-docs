import re
p = 'query-cosientist.md'
doc = open(p).read()

# 1) K-Z3 row evidence: insert before ' | K-Z2 |' on the K-Z3 hypothesis row
row_anchor = 'production 実測数には算入しない (正 endpoint search.kotobase.net/search?q=test で再実施済みの run201 のみ採用)。'
i = doc.find(row_anchor)
assert i != -1, 'row anchor not found'
new_ev = (' falsify 2026-09-06 (第80回, K-Z3 10時台 2セット目 run203A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 10:14–10:15 JST, 全 80/80 200, host load1 19.87–23.40 は production HTTP 実測のため gate 外): run203A cold(>=0.5s) 1/20 (1.067s 単発) p50 43ms / run203B cold 0/20 p50 45ms / run203C cold 0/20 p50 45ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 50ms max 280ms と静穏で control 分離成立、cold 群は search 側に局在。bench 第79回 run202A クラスタ (4/60, 10:01) は本計測 (10:14) で非再現し run186A 型「帯内 1 窓即消失」パターンと整合。status 判定は rank に委ねる (rank 専門)。')
doc = doc[:i] + row_anchor + new_ev + doc[i+len(row_anchor):]

# 2) iteration log entry after the last falsify 第78回 entry line
log_anchor = 'NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 9時台 n 積み増し継続)。'
j = doc.rfind(log_anchor)
assert j != -1, 'log anchor not found'
entry = ('\n- 2026-09-06: falsify 第80回。10:13 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 5ddb712 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第79回 (09:55) と bench 第79回 (run202A–C, 10時台帯初計測) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 19.87 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 10時台 2セット目 run203A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 10:14–10:15 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (1.067s 単発, run203A), warm p50 43–45ms 静穏帯水準, control (kotobase.net/signup) cold 0/20 p50 50ms max 280ms 静穏で control 分離成立 — bench 第79回 run202A クラスタ (4/60, 10:01) は 13 分後の本計測で非再現し「帯内 1 窓即消失」パターンと整合。10時台通算 (bench run202 4/60 + 本 tick 1/60) で 5/120 (~4.2%) の低位帯寄り。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。')
doc = doc[:j+len(log_anchor)] + entry + doc[j+len(log_anchor):]

open(p, 'w').write(doc)
print('OK')

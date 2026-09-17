p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
data=open(p,encoding='utf-8').read()

# --- 1) K-Z3 evidence append, anchored on the falsify 第88回 run213 evidence line ---
ev_anchor='run213A 散発 4 件は run212A 冒頭集中型ではなく'
i=data.find(ev_anchor)
assert i!=-1, 'ev anchor not found'
# find end of that line
line_end=data.index('\n', i)
assert data.rstrip().endswith('ranking') or True
existing=data[:line_end]
assert existing.rstrip().endswith('status 判定は rank に委ねる (rank 専門)。'), existing[-90:]
add=(" bench 2026-09-06 (第88回, K-Z3 14時台 n 積み増し run214A–C, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, Tokyo, 14:49–14:50 JST, 全 80/80 200, host load1 19.95 は production HTTP 実測のため gate 外): "
"run214A cold(>=0.5s) 1/20 (1.160s 14番目 単発散発型) p50 90ms / run214B cold 0/20 p50 53ms / run214C cold 0/20 p50 47ms — "
"cold 1/60 (~1.7%), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 46ms max 144ms と静穏で "
"control 分離成立、cold 群は search 側に局在。run213A 散発 4 件 (falsify 第88回 14:44) は 5 分後の本計測で 1/60 単発に減弱し "
"run212A→run213A 型「帯内 1 窓即消失」パターンと整合 (run173/run193 型薄単発)。14時台通算は run211 (1/60) + run212 (4/60) + run213 (4/60) "
"+ 本 tick (1/60) で 10/240 (~4.2%) の低位帯 — 9/5 run152 5/60 と合算すると 15/300 (~5.0%)。status 判定は rank に委ねる (rank 専門)。")
data=data[:line_end]+add+data[line_end:]

# --- 2) bench 第88回 iteration log entry, appended at file end (canonical LAST 3 region) ---
log=("\n- 2026-09-06: bench 第88回。14:49 JST tick。HEAD 5d15491 = fetch 後 net-kotobase/main 先端一致 "
"(同期確認; git pull --ff-only は silent 失敗のため fetch + rev-parse 比較で取り込み)。falsify 第88回 "
"(run213A–C, 14:43, 5d15491) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 19.95 "
"(gate 7.5 超過) のため local 測定は拒否し「host busy (load1 19.95)」を記録。フォールバック (production HTTP 実測, gate 外): "
"rank 第87回 NEXT は「K-Z3 15時台帯初計測 n 積み増し」だが cron 実行時刻が 14時台のため 15時台待機は不可能 "
"(falsify 第88回 14:43 tick の 14時台実行 precedents に従い現在時刻帯 14時台 n 積み増しで実施): "
"K-Z3 14時台 n 積み増し run214A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 14:49–14:50 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (~1.7%) — run214A 単発 1.160s (14番目 散発型), "
"warm 群 p50 47–90ms (run214A だけ p50 90ms とやや高位だが cold 1 件の寄与含む), control (kotobase.net/signup) cold 0/20 "
"p50 46ms max 144ms 静穏で control 分離成立、cold 群は search 側に局在。run213A 散発 4 件 (14:44) は 5 分後の本計測で 1/60 単発に減弱し "
"run212A→run213A 型「帯内 1 窓即消失」パターンと整合。14時台通算 (run211 1/60 + run212 4/60 + run213 4/60 + 本 tick 1/60) 10/240 ~4.2%、"
"9/5 run152 と合算 15/300 ~5.0% 低位帯残界。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n")
data=data.rstrip('\n')+log

open(p,'w',encoding='utf-8').write(data)
print('OK appended')
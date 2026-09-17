import io

path = 'query-cosientist.md'
t = open(path, encoding='utf-8').read()

EVIDENCE = '''22時台通算 run252 (9/60) + run253 (6/60) + run254 (2/60) + run255 (bench, 2/60) + 本 tick (1/60) = 20/300 (~6.7%) — 21時台 (~4.0%)・9/5 22時台 (7/180 ~3.9%) より高位傾向を 5 セットで維持 (traffic 遷移説の判定は rank に委ねる)。status 判定は rank に委ねる (rank 専門)。'''

NEW_EVIDENCE = '''22時台通算 run252 (9/60) + run253 (6/60) + run254 (2/60) + run255 (bench, 2/60) + 本 tick (1/60) = 20/300 (~6.7%) — 21時台 (~4.0%)・9/5 22時台 (7/180 ~3.9%) より高位傾向を 5 セットで維持 (traffic 遷移説の判定は rank に委ねる)。status 判定は rank に委ねる (rank 専門)。
bench 2026-09-06 (第104回, K-Z3 22時台 n 積み増し run258A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 22:55:05 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 26.61 (pre-run, gate 7.5 超過) は production HTTP 実測のため gate 外 — rank 第112回 NEXT「K-Z3 22時台追加 n or 23時台帯初計測」は現時刻 22時台のため 22時台 n 積み増し): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run258A cold 3/20 (3/4番目隣接 1.695s/1.123s + 7番目 1.543s — 早先頭 cluster 型) p50 56.6ms / run258B cold 0/20 p50 55.9ms max 137.0ms / run258C cold 0/20 p50 50.0ms max 138.8ms, control (kotobase.net/signup) cold 0/20 p50 49.8ms max 123.4ms 静穏で control 分離成立、cold 群は search 側に局在。run258A 早先頭 cluster 3 件は B/C 0/20 で即消失し run252A/253A 型 heavy cluster (6+2+1/20) の弱い再現 (3/20, heavy 未満) で「帯内 1 窓即消失」単発散発〜早先頭 cluster 型継続。22時台通算 (rank 第112回 fold 後 22/360 ~6.1% + 本 tick 3/60 = 25/420 ~6.0%) — 21時台 (~4.0%)・9/5 22時台 (7/180 ~3.9%) より高位傾向維持 (traffic 遷移説の判定は rank に委ねる)。status 判定は rank に委ねる (rank 専門)。'''

assert EVIDENCE in t, "evidence anchor not found"
t = t.replace(EVIDENCE, NEW_EVIDENCE, 1)

LOG_ENTRY = '''- 2026-09-06: bench 第104回。22:55 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (fetch rc 0, HEAD bcc8cef = net-kotobase/main 先端一致, 乖離 0)。rank 第112回 (22:53) を取り込み済み確認 — 22時台通算 22/360 ~6.1% (run252-256×2 fold 済み)。※pre-run monitor の NEXT「K-Z3 深夜帯 23時台」は rank 第89-90回帯 stale (rank 第105/108/109/110回で共有判断済み) — 状態正本の現在 NEXT は rank 第112回『委ねる (rank 指定優先; フォールバックは K-Z3 22時台 n 積み増し続行 or 23時台帯初計測)』で現時刻 22時台のため 22時台 n 積み増しで実施。live smoke 200 (/, /signup; pre-run 計測)。host load1 26.61 (pre-run, gate 7.5 超過) のため local 測定は拒否し「host busy (load1 26.61)」を記録し production HTTP フォールバック (gate 外)。K-Z3 22時台 n 積み増し run258A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 22:55:05 JST 開始, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run258A cold 3/20 (3/4番目隣接 1.695s/1.123s + 7番目 1.543s, 早先頭 cluster 型) p50 56.6ms / run258B 0/20 p50 55.9ms max 137.0ms / run258C 0/20 p50 50.0ms max 138.8ms, control (kotobase.net/signup) cold 0/20 p50 49.8ms max 123.4ms 静穏で control 分離成立、cold 群は search 側に局在。run258A 早先頭 cluster 3 件は B/C 0/20 で即消失し run252A/253A 型 heavy cluster の弱い再現 (3/20) で「帯内 1 窓即消失」単発散発〜早先頭 cluster 型継続。22時台通算は rank 第112回 fold (22/360 ~6.1%) + 本 tick 3/60 = 25/420 (~6.0%) に更新 — 21時台 (~4.0%)・9/5 22時台 (~3.9%) より高位傾向を 6 セットで維持 (traffic 遷移説の判定は rank に委ねる)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 22時台 n 積み増し続行 or 23時台帯初計測, 次 run ID は run259 使用)。

'''

HDR = '## Iteration log\n'
assert HDR in t
# insert after header: newest-at-top convention (current line 303 is rank 第112回)
t = t.replace(HDR, HDR + LOG_ENTRY, 1)

open(path, 'w', encoding='utf-8').write(t)
print("done")
print("bytes", len(t))
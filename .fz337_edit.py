#!/usr/bin/env python3
# falsify157: append K-Z3 evidence + insert iter-log entry
import io
path='query-cosientist.md'
with io.open(path,encoding='utf-8') as f:
    txt=f.read()
lines=txt.split('\n')

EVID=" falsify 2026-09-07 (第157回, K-Z3 10時台 n 積み増し run337A–C — bench 第143回 (10:40, run336) に続く n 積み増し, 次 run ID run337 枠, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 10:49:05–10:49:28 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 88.03 (10:49 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 4/0/2 per 20 = 6/60 (~10%) — run337A cold 4/20 散発配置 (0.9202s 13番目 / 1.0094s 8番目 / 1.2485s 4番目 / 2.1398s 15番目, warm 群 0.05–0.17s) p50 116.0ms max 2.140s / run337B cold 0/20 p50 96.6ms max 243.4ms / run337C cold 2/20 (0.5058s 1番目 / 0.5067s 5番目 — いずれも閾値 0.5s すれすれ境界値) p50 116.8ms max 191.8ms, control (kotobase.net/signup) cold 0/20 p50 68.5ms max 289.2ms 完全静穏で control 分離成立、cold 群は search 側に局在。run337A cold 4/20 散発クラスタ (0.92–2.14s) は B 0/20 で「帯内 1 窓即消失」型の弱い再上振れ — run332–336 (各 1–4/60 散発減弱) から 4/20 散発クラスタへ再上昇するが heavy (>=6/20) には至らず mid-cluster 弱後続相当、run337C の 2 件は 0.5s 閾値すれすれ境界値で濃度への影響は限定的。host load 88 high tick の p50 (search 96–117ms, control 68.5ms) 上振れ込み borderline だが A 4/20 の 0.92–2.14s は閾値決定的で判定に影響なし。10時台 (9/7) 通算 = 16/360 (~4.4%, run336 fold) + 本 tick 6/60 = 22/420 (~5.2%) の中位帯域 6 セット目、run331A heavy 9/20 は単一窓即消失のまま再現未確認。status 判定は rank に委ねる (rank 専門)。"

# 1) append evidence to line 279 (index 278)
lines[278]+=EVID

# 2) insert iter-log entry after '## Iteration log' (index 357), before first entry
ILOG="- 2026-09-07: falsify 第157回。10:49 JST tick。HEAD 1de4600 = rank 第146回 (10:33, fold run333-335, NEXT run336) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 88.03 (10:49 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は bench 第143回 (Iteration log 末尾, 10:40, L279 末尾) の「K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run337 使用」で、run336 は bench 第143回が先行測定済みのため本 tick は run337 枠を実施。K-Z3 10時台 run337A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 10:49:05–10:49:28 JST, 全 80/80 200): A cold 4/20 (0.9202/1.0094/1.2485/2.1398s, pos 13/8/4/15 散発配置) p50 116.0ms / B cold 0/20 p50 96.6ms / C cold 2/20 (0.5058/0.5067s 閾値境界値) p50 116.8ms / control (kotobase.net/signup) cold 0/20 p50 68.5ms max 289.2ms 完全静穏で control 分離成立、cold 群は search 側に局在 — search cold 6/60 (~10%) で run332–336 の散発減弱 (各 1–4/60) から再上振れした 10時台 6 セット目、run337A 4/20 散発クラスタは heavy (>=6/20) 未満の mid-cluster 弱後続で run331A heavy 9/20 は単一窓即消失のまま再現未確認。10時台 (9/7) 通算 = 16/360 (~4.4%, EVID run336) + 本 tick 6/60 = 22/420 (~5.2%) の中位帯域。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run338 使用)"

ilog_hdr_idx=None
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        ilog_hdr_idx=i; break
assert ilog_hdr_idx is not None, 'Iteration log header not found'
lines.insert(ilog_hdr_idx+1, ILOG)

with io.open(path,'w',encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('done. iter header at', ilog_hdr_idx+1)
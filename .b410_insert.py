import io

FN='query-cosientist.md'
data=open(FN,'rb').read().decode('utf-8')
lines=data.split('\n')

# --- 1. Append run410 evidence to K-Z3 row = line 279 (0-indexed 278) ---
ev = (" bench 2026-09-08 (第185回, K-Z3 0時台(深夜帯) n 積み増し run410A–C — iter-log HEAD NEXT「委ねる」フォールバック: K-Z3 現在時刻帯 0時台 n 積み増し継続、次 run ID は run410 使用 の run410 枠として実施 (falsify 第179回 run409 10/60 済みの 0時台 4 セット目, .b410 既存なし=衝突なし確認), "
"同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 00:53:xx–00:54:32 JST, 全 80/80 200, host load1 ~8.86 (00:50 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run410A cold 2/20 (1.0945s pos3 / 1.8121s pos6 冒頭寄り散発配置, warm 群 0.043–0.144s で cold と交互) p50 58.0ms max 1.8121s / run410B cold 0/20 p50 45.3ms max 137.1ms / run410C cold 0/20 p50 44.8ms max 125.3ms, "
"control (kotobase.net/signup) cold 0/20 p50 53.4ms max 170.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。run410A 散発 2/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続 (run409A heavy 10/20 → 本 tick 散発 2/20 の散発減弱, heavy>=6/20 は再達せず)。"
"0時台 (9/8) 通算 = run407 (4/60) + run408 (4/60) + run409 (10/60) + 本 tick run410 (2/60) = 20/240 (~8.3%) の 4 セット連続 cold>0 — 深夜帯 traffic 最低帯での cold 散発再出現 (run409A heavy の直後の散発減弱) は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし全セット「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")

# verify line 279 (idx 278) ends with the run409 tail we expect
assert lines[278].endswith('secret は一切記録せず。'), 'line279 tail mismatch: %r' % lines[278][-40:]
lines[278] = lines[278] + ev
print('line279 appended, newlen', len(lines[278]))

# --- 2. Insert iter-log entry after "## Iteration log" header ---
ilog = ("- 2026-09-08: **bench 第185回**。00:53 JST tick。HEAD 5f91e7e = falsify 第179回 = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。"
"live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 ~8.86 (00:50 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (falsify 第179回, 00:50)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run410 使用)」で、cron 実行時刻 00:53 が 0時台 (run407/408/409 済 18/180 ~10.0%) 中の n 積み増し続行。run410 枠を本 tick 実施 (.b410 既存なし=衝突なし確認)。"
"K-Z3 0時台 run410A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 00:53–00:54 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run410A cold 2/20 (1.0945s pos3 / 1.8121s pos6 冒頭寄り散発) p50 58.0ms max 1.8121s / run410B cold 0/20 p50 45.3ms / run410C cold 0/20 p50 44.8ms, control (kotobase.net/signup) cold 0/20 p50 53.4ms max 170.0ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run410A 散発 2/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続 (run409A heavy 10/20 → 本 tick 散発 2/20 の散発減弱, heavy>=6/20 は再達せず)。0時台 (9/8) 通算 = run407 (4/60) + run408 (4/60) + run409 (10/60) + 本 tick run410 (2/60) = 20/240 (~8.3%) の 4 セット連続 cold>0 — 深夜帯 traffic 最低帯での cold 散発再出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
"ただし全セット「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run411 使用 — ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。")

hdr_idx=None
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        hdr_idx=i; break
assert hdr_idx is not None, 'iter log header not found'
lines.insert(hdr_idx+1, ilog)
print('iter-log inserted after line', hdr_idx+1)

open(FN,'w',encoding='utf-8').write('\n'.join(lines))
print('WRITTEN ok')
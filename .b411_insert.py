import io

FN='query-cosientist.md'
data=open(FN,'rb').read().decode('utf-8')
lines=data.split('\n')

# --- 1. Append run411 evidence to K-Z3 row = line 279 (0-indexed 278) ---
ev = (
" falsify 2026-09-08 (第180回, K-Z3 1時台(深夜帯) 帯初計測 run411A–C — rank 第175回 NEXT「K-Z3 1時台帯初計測 run411 使用」に従い現時刻帯 1時台帯初計測 (0時台 4 セット 20/240 ~8.3% 中位帯候補完了後の帯移行, .b411 測量ファイルのみで comit 未使用=衝突なし確認), "
"同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 01:13–01:14 JST (search) + 01:19–01:20 JST (control), 全 80/80 200, host load1 ~90 (pre-run, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 3/0/1 per  20 = 4/60 (~6.7%) — run411A cold 3/20 (1.129911s pos1 / 1.567964s pos6 / 1.120914s pos18 散発配置, warm 群 0.0549–0.3290s で cold と交互) p50 0.1505s / run411B cold 0/20 p50 0.1826s max 0.2812s / run411C cold 1/20 (1.6458s pos14 単発散発) p50 0.1584s max 1.6458s, "
"control (kotobase.net/signup) cold 0/20 p50 0.0533s max 0.1416s 完全静穏で control 分離成立、cold 群は search 側に局在。run411A 散発 3/20 + C 単発 1/20 は B/C  0/20 即消失で「帯内 1 窓即消失」散発型継続 (run409A heavy 10/20 → run410 2/60 散発 → 本 tick  4/60 散発の深夜帯減衰振幅内, heavy>=6/20 は再達せず)。"
"1時台 (9/8) 帯初計測 = 4/60 (~6.7%) の 1 セット — 深夜帯 1時台 traffic 最低帯での cold 出現継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし帯初 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
)

# verify line 279 (idx 278) ends with the expected previous tail
assert lines[278].endswith('secret は一切記録せず。'), 'line279 tail mismatch: %r' % lines[278][-40:]
lines[278] = lines[278] + ev
print('line279 appended, newlen', len(lines[278]))

# --- 2. Insert iter-log entry after"## Iteration log" header ---
ilog = (
"- 2026-09-08: **falsify 第180回**。01:14 JST tick、HEAD 1bf704b = rank  第175回 (00:59, K-Z3 0hr fold 20/240 ~8.3% 中位帯候補, NEXT「K-Z3 1時台帯初計測 run411 使用」) = remote net-kotobase/main 一致 ( git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 ~90 (pre-run uptime 実測, gate  7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale( rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD( rank 第175回, 1bf704b)「K-Z3 1時台帯初計測 run411 使用」で、cron 実行時刻 01:02 が 1時台 (9/8) 帯初計測 (0時台 4 セット 20/240 ~8.3% 中位帯候補完了後の帯移行) の run411 枠を本 tick 実施 (.b411 測量ファイルのみで commit 未使用=衝突なし確認)。"
"K-Z3 1時台 run411A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 01:13–01:14 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 3/0/1 per  20 =  4/60 (~6.7%) — run411A cold 3/20 (1.129911s/1.567964s/1.120914s 散発配置 冒頭 1/6/18番目) p50 0.1505s / run411B cold 0/20 p50 0.1826s max 0.2812s / run411C cold 1/20 (1.6458s pos14 単発散発) p50 0.1584s, control (kotobase.net/signup) cold  0/20 p50 0.0533s max 0.1416s 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run411A 散発 3/20 + C 単発 1/20 は B/C  0/20 即消失で「帯内 1 窓即消失」散発型継続 (run409A heavy 10/20 → run410 2/60 散発 → 本 tick  4/60 散発の深夜帯減衰振幅内, heavy>=6/20 は再達せず)。1時台 (9/8) 帯初計測 =  4/60 (~6.7%) の 1 セット — 深夜帯 traffic 最低帯での cold 出現継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
"ただし帯初 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる ( rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 1時台 n 積み増し続行,次 run ID並 は run412 使用 — ※sibling falsify/bench/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。"
)

hdr_idx=None
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        hdr_idx=i; break
assert hdr_idx is not None, 'iter log header not found'
lines.insert(hdr_idx+1, ilog)
print('iter-log inserted after line', hdr_idx+1)
open(FN,'w',encoding='utf-8').write('\n'.join(lines))
print('WRITTEN ok')
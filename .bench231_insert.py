#!/usr/bin/env python3
# append bench run524 evidence to K-Z3 row + insert brand-new iter-log entry after header
import io, sys, datetime

SRC = '/tmp/qc_edit_src.md'   # copy of worktree file
DST = '/tmp/qc_edit_dst.md'

EVID = (
" bench 2026-09-09 (bench 第231回, K-Z3 2時台(深夜帯) n 積み増し run524A–C — "
"falsify 第233回 (02:07, 2時台帯初 run523 cold 8/60) との run523 ID 衝突のため run524 に読替 "
"(run216/256/263/278 前例; 本測 02:38 は同一帯 independent 2セット目), 同測定法 n=20 × 3 + "
"landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
"search.kotobase.net/search?q=test, 02:38–02:40 JST, 全 80/80 200, host load1 ~40 "
"(uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — "
"curl + python stats のみ): cold(>=0.5s) 8/0/0 per 20 = 8/60 (~13.3%) — "
"run524A 散発クラスタ 8/20 (1.286/0.815/1.679/0.954/0.937/0.874/0.877/1.653s 散発配置, warm 群 0.04–0.39s と交互) "
"p50 144.1ms warm_p50 119.0ms / run524B cold 0/20 p50 56.0ms max 169.8ms / "
"run524C cold 0/20 p50 74.5ms max 136.6ms, control (kotobase.net/signup) cold 0/20 "
"p50 45.2ms max 147.3ms 完全静穏で control 分離成立, cold 群は search 側に局在。"
"run524A 散発クラスタ 8/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」heavy 型継続 "
"(falsify run523A (02:07) 散発クラスタ の ~30 分後 weak 再現, heavy>=6/20 は 2時台 帯初 run523A 6/20 に続き本測 run524A 8/20)。"
"2時台 (9/9) 通算 = falsify run523 (8/60, 帯初) + 本測 run524 (8/60) = 16/120 (~13.3%) の 2 セット — "
"1時台 13/180 ~7.2% から移行後も帯初・2セット目とも cold>0 で深夜帯 traffic 依存説への反証材料継続 "
"(深夜帯 ~26-31% 平坦パターンと整合方向)。ただし 2 セットとも「帯内 1 窓即消失」heavy 型で帯水準確定・機構判断には rank n を要する。"
"status 判定は rank に委ねる (rank 専門)。"
)

ITER = (
"- 2026-09-09: bench 第231回。02:40 JST tick。HEAD daf17a9 = rank 第230回 (01:54, fold run521+522 "
"1時台 13/180 ~7.2% 3セット; NEXT run523) を remote net-kotobase/main 一致として取込 (git fetch + "
"rev-parse 比較 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため出力は"
"ファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は "
"stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第230回 NEXT 委ねる → "
"フォールバック K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run523 使用) で, 本 tick は cron 実行時刻 "
"02:38 が 2時台へ移行済みのため 2時台帯内 n 積み増しとして実施。live smoke 200 (/, /signup; pre-run 計測)。"
"host load1 ~39.8 (02:38 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。"
"※従兄弟 falsify 第233回 (02:07 計測, 2時台帯初計測 run523A-C cold 8/60 heavy 6/2/0 per 20, control 0/20 "
"完全静穏分離成立) が run523 を先行消費済み (worktree in-flight で確認) のため、本測 (02:38, 独立) は run524 に読替 "
"(run216/256/263/278 前例で independent 2セット目として両方採用可)。K-Z3 2時台 n 積み増し run524A-C を実測 "
"(同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
"search.kotobase.net/search?q=test, 02:38–02:40 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 8/0/0 per 20 = 8/60 (~13.3%) — run524A 散発クラスタ 8/20 (1.286/0.815/1.679/0.954/0.937/"
"0.874/0.877/1.653s 散発配置) p50 144.1ms warm_p50 119.0ms / run524B cold 0/20 p50 56.0ms / "
"run524C cold 0/20 p50 74.5ms, control (kotobase.net/signup) cold 0/20 p50 45.2ms max 147.3ms "
"完全静穏で control 分離成立, cold 群 search 側局在。run524A 散発クラスタ 8/20 は B/C 0/40 + control 0/20 "
"で即消失し「帯内 1 窓即消失」heavy 型継続。2時台 (9/9) 通算 = falsify run523 (8/60带初) + 本測 run524 (8/60) "
"= 16/120 (~13.3%) 2 セット — 深夜帯 traffic 最低帯で帯初・2セット目とも cold>0 は K-Z3 traffic 依存説への反証材料継続 "
"(深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
"status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
"secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行, "
"次 run ID は run525 使用 — run523 は falsify 第233回, run524 は本測 が消費済みのため次セットは run525)。"
)

with open(SRC, 'r', encoding='utf-8') as f:
    txt = f.read()

lines = txt.split('\n')

# 1) K-Z3 row: append EVID to the end of the row starting with "| K-Z3 |"
found_kz3 = False
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        lines[i] = ln.rstrip() + EVID
        found_kz3 = True
        break
if not found_kz3:
    print("ERROR: K-Z3 row not found", file=sys.stderr)
    sys.exit(1)

# 2) iter log: insert ITER right after the "## Iteration log" header line
found_hdr = False
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        lines.insert(i+1, ITER)
        found_hdr = True
        break
if not found_hdr:
    print("ERROR: iter log header not found", file=sys.stderr)
    sys.exit(1)

with open(DST, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("OK kz3=%s iter_hdr=%s" % (found_kz3, found_hdr))

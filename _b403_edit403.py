import sys

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
doc = open(PATH, encoding='utf-8').read()

ev = (" bench 2026-09-07 (第183回, K-Z3 23時台(深夜帯) 帯初計測 run403A–C — rank NEXT 委ねる (rank 指定優先; フォールバックは 現在時刻帯 n 積み増し) に従い現時刻帯 23時台 帯初計測 (22時台 falsify run401 + bench run402 完了後の帯移行, 次 run ID run403), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 23:04:13–23:04:25 JST, 全 80/80 200, host load1 15.96→17.10 (23:03/23:04 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run403A cold 3/20 散発配置 (1.1557s pos5 / 1.3093s pos13 / 1.1322s pos19 deep, warm 群 0.043–0.182s と交互) p50 67.1ms warm_p50 64.5ms max 1309.3ms / run403B cold 0/20 p50 59.1ms max 437.9ms / run403C cold 0/20 p50 57.4ms max 276.8ms, control (kotobase.net/signup) cold 1/20 (0.5341s pos12 閾値境界値) p50 53.2ms max 534.1ms — control 境界 1 件で完全静穏不成立 borderline not-separated-leaning 注記 (search cold 3 件 1.13–1.31s deep で control 境界 0.534s と逆方向の magnitude 分離弱成立、cold 群 search 側局在). run403A 散発 3/20 は B/C 0/40 + control 境界 1 件で「帯内 1 窓即消失」散発型 (heavy>=6/20 は再達せず). 23時台 (9/7) 帯初計測 cold 3/60 (~5.0%) — 22時台 (17/120 ~14.2%) より低位の中位帯初期サンプル、日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変). ただし帯初 n=1 セット + control borderline のため帯水準確定・機構判断には rank 追加 n を要する. status 判定は rank に委ねる (rank 専門).")

ilog = "- 2026-09-07: bench 第183回。23:04 JST tick。HEAD 966ac7c = falsify 第175回 (22:33, dedupe iter-log; K-Z3 22hr run401 8/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 15.96→17.10 (23:03/23:04 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact — 全 bot 共有判断) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第182回, 22:33)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run403 使用)」で、現時刻帯 23時台 (9/7) 帯初計測 run403 を実施 (22時台 run401/run402 済みの帯移行後 23時台 1 セット目, .b403 既存なし=衝突なし確認)。K-Z3 23時台 run403A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 23:04:13–23:04:25 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run403A cold 3/20 散発配置 (1.1557s pos5 / 1.3093s pos13 / 1.1322s pos19 deep) p50 67.1ms / run403B cold 0/20 p50 59.1ms / run403C cold 0/20 p50 57.4ms, control (kotobase.net/signup) cold 1/20 (0.5341s pos12 閾値境界値) p50 53.2ms max 534.1ms — control 境界 1 件で完全静穏不成立 borderline not-separated-leaning 注記 (search cold 3 件 1.13–1.31s deep で control 境界 0.534s と逆方向の magnitude 分離弱成立、cold 群 search 側局在)。run403A 散発 3/20 は B/C 0/40 + control 境界 1 件で「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は再達せず)。23時台 (9/7) 帯初計測 cold 3/60 (~5.0%) — 22時台 (17/120 ~14.2%) より低位の中位帯初期サンプル、日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。ただし帯初 n=1 セット + control borderline のため帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し続行、次 run ID は run404 使用 — ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。\n"

log = []

# 1) append evidence to K-Z3 row (single logical line containing run402 tail anchor)
anchor = "A 両セット 7/20 散発/heavy で重複再現"
idx = doc.find(anchor)
if idx < 0:
    log.append("ERROR: anchor not found for evidence append")
else:
    # find end of that line
    nl = doc.find('\n', idx)
    doc = doc[:nl] + ev + doc[nl:]
    log.append("ev appended at char idx %d" % idx)

# 2) insert iter-log entry after the '## Iteration log' header line
hdr = "## Iteration log\n"
hidx = doc.find(hdr)
if hidx < 0:
    log.append("ERROR: '## Iteration log' header not found")
else:
    insert_at = hidx + len(hdr)
    doc = doc[:insert_at] + ilog + doc[insert_at:]
    log.append("ilog inserted after header")

open(PATH, 'w', encoding='utf-8').write(doc)
log.append("written OK; new total_lines=%d" % len(doc.split('\n')))
open('/tmp/bench_edit.txt', 'w').write('\n'.join(log) + '\n')
print('\n'.join(log))
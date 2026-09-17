import io

FN = 'query-cosientist.md'
ILOG = ("- 2026-09-09: cosientist 第151回。00:5x JST tick。HEAD f418dea = falsify 第230回 (00:42-43, "
        "K-Z3 0時台 run518 cold 10/60 ~16.7%, control 1/20 境界) = remote net-kotobase/main・bench_fetch/main 一致 "
        "(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; "
        "worktree diff HEAD -- query-cosientist.md 空 クリーン 事前確認; terminal foreground stdout 空=既知のため "
        "状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は "
        "stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第225回 NEXT フォールバック "
        "「K-Z3 現在時刻帯 0時台 n 積み増し続行, 次 run ID は run518」→ falsify 第230回が run518 使用済み。"
        "※本 tick 開始時 HEAD 2bc45c4 (rank 第225回, run518 は NEXT 参照のみ) で 00:48 に独立計測したが、"
        "作業中に falsify 第230回 commit (f418dea, run518) が着弾し run518 は競合確定 — "
        "run216/256/263/278 precedent に従い本測 (00:48 若干, 0時台独立 4 セット目) を run519 に読替して記録)。"
        "qualify する新 evidence は 0 本 (K-Q1 は残余 cosientist 実装専任の transact 401 write path 動的照合 "
        "のみ・測定で qualify する実装改善なし — 反証が先規律でコード変更なし; K-Z2/K-S1/K-S2 は evidence なし) "
        "のため観測 tick。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200 3/3)。"
        "host load1 26.65–30.89 (00:48 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。"
        "K-Z3 0時台(24時台) n 積み増し run519A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, "
        "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 00:48:11–00:48:53 JST, "
        "全 80/80 200, secret 不含 — curl + python3 stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
        "— run519A 冒頭単発 1.0254s (2番目) p50 0.177s / run519B cold 0/20 p50 0.101s max 0.273s / "
        "run519C cold 0/20 p50 0.093s max 0.245s, control (kotobase.net/signup) cold 1/20 (max 0.5787s 閾値 0.5s "
        "直上 境界) で分離は境界成立 (完全静穏 未達)。0時台帯 (9/9) 通算 = falsify run516 (5/60) + bench run517 (6/60) "
        "+ falsify run518 (10/60) + 本 run519 (1/60) = 22/240 (~9.2%) の 4 セット — 深夜帯 traffic 最低帯 0時台で "
        "heavy (falsify run518A 9/20) → 散発単発減衰 (本 run519A 1/20) の「帯内 1 窓即消失」型継続, "
        "traffic 依存説への反証材料継続, 帯水準確定・機構判断には未達 (K-Z3 open 継続)。"
        "status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
        "n 積み増し続行, 次 run ID は run520 使用)。")

data = io.open(FN, 'r', encoding='utf-8', newline='').read()
lines = data.split('\n')
# find the "## Iteration log" header line
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        hdr_idx = i
        break
assert hdr_idx is not None, "iter-log header not found"
# sanity: line after header should be an existing "- 2026-09-0x:" entry (falsify 第230回)
assert lines[hdr_idx+1].startswith('- 2026-09-09: falsify 第230回'), lines[hdr_idx+1][:40]
lines.insert(hdr_idx+1, ILOG)
open(FN, 'w', encoding='utf-8', newline='').write('\n'.join(lines))
o = io.open('.c151_itercheck.txt', 'w', encoding='utf-8')
o.write("hdr_idx=%d\n" % hdr_idx)
o.write("after insert line at hdr_idx+1 (first 120):\n%s\n" % lines[hdr_idx+1][:120])
o.write("next line (falsify230) first 60:\n%s\n" % lines[hdr_idx+2][:60])
o.write("total lines: %d\n" % len(lines))
o.close()
print("done")
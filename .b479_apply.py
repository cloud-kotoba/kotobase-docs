# -*- coding: utf-8 -*-
# bench 第208回: K-Z3 16時台帯初計測 run479A-C evidence append + iter-log entry.
import io, sys

P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(P,encoding="utf-8").read()

# ---- 1) K-Z3 evidence row append (row idx 278, ends with run476 content, no closing pipe) ----
# Anchor: the run476 tail within the K-Z3 row.
ev_anchor = "15時台 (9/8) 通算 = bench run475 (7/60 帯初) + run476 (5/60) = 12/120 (~10%) 中〜高位帯候補。status 判定は rank に委ねる (rank 専門)。"
assert s.count(ev_anchor)==1, "ev_anchor count=%d"%s.count(ev_anchor)

ev_app = ev_anchor + (" bench 2026-09-08 (第208回, K-Z3 16時台帯初計測 run479A–C "
"— iter-log HEAD (falsify 第214回 run478, 15:52) の続行枠, 次 run ID は run479 を使用, "
"前例 (bench 第206回 15:17 15時台帯移行) に従い実行時刻 16時台帯初として実施, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
"16:04–16:06 JST, 全 80/80 200, host load1 24.15→(16:03 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
"secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) "
"— run479A 散発クラスタ 5/20 (1.0624s/1.3249s/1.3728s/1.6955s/1.9566s 散発配置) p50 0.0728s / "
"run479B 単発 1/20 (1.1505s) p50 0.0871s / run479C cold 0/20 p50 0.0721s max 0.1654s, "
"control (kotobase.net/signup) cold 0/20 p50 0.0518s max 0.1649s 完全静穏で control 分離成立、cold 群 search 側局在。"
"run479A 散発クラスタ 5/20 は B 単発 1/20 / C 0/20 + control 0/20 で「帯内 1 窓即消失」散発クラスタ型継続 "
"(run478A 散発ペア 2/20 の約 13 分後再上振れ, heavy>=6/20 は run479 で未達). "
"16時台帯初 cold 6/60 (~10.0%) — 15時台 (21/240 ~8.8% 4 セット) に引き続く日中帯 high 側の帯初再上振れ、"
"traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。帯初 n=1 セットのみで帯水準確定・"
"機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")
assert s.count(ev_app)==0, "ev_app already present"
s=s.replace(ev_anchor, ev_app, 1)

# ---- 2) Iteration log entry insert (right after '## Iteration log' header) ----
hdr="## Iteration log\n"
assert s.count(hdr)==1,"hdr count=%d"%s.count(hdr)
ilog_entry = ("- 2026-09-08: bench 第208回。16:06 JST tick。HEAD 9625ea0 = falsify 第214回 (15:52, K-Z3 15時台 n-add run478 "
"cold 2/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; "
"terminal stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 "
"n 積み増し継続。」は stale (rank 第90回帯 artifact 前例で既知) — true progressive NEXT は iter-log HEAD 連鎖 "
"(falsify 第214回 NEXT フォールバック「K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run479」))。"
"実行時刻 16:04 が前 tick (falsify 第214回 15:52) から 16時台へ帯移行済みのため、前例 (bench 第206回 15:17) に従い "
"16時台帯初計測として実施。live smoke 200 (/, /signup, search; pre-run + 本 tick 実測 200)。"
"host load1 24.15 (16:03 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため "
"gate 外で実施。K-Z3 16時台 run479A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test, 16:04–16:06 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): "
"cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) — run479A 散発クラスタ 5/20 (1.0624/1.3249/1.3728/1.6955/1.9566s) p50 0.0728s / "
"run479B 単発 1/20 (1.1505s) p50 0.0871s / run479C cold 0/20 p50 0.0721s max 0.1654s, "
"control (kotobase.net/signup) cold 0/20 p50 0.0518s max 0.1649s 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run479A 散発クラスタ 5/20 は B 単発 1/20 / C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 "
"(run478A 散発ペア 2/20 の約 13 分後再上振れ, heavy>=6/20 は run479 で未達). "
"16時台帯初 cold 6/60 (~10.0%) — 15時台 (21/240 ~8.8% 4 セット) に引き続く日中帯 high 側の帯初再上振れ、"
"traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。"
"secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) に追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
"16時台 n 積み増し続行, 次 run ID は run480)。\n")
s=s.replace(hdr, hdr+ilog_entry, 1)

open(P,"w",encoding="utf-8",newline="\n").write(s)
print("append+ilog ok, new len", len(s))
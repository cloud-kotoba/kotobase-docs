path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    content = f.read()
marker = "## Iteration log\n"
assert content.count(marker) == 1, "iter log marker count %d" % content.count(marker)
entry = ("- 2026-09-08: falsify 第215回。16:24 JST tick。HEAD 7b90d45 = rank 第213回 (16:17, no-new-evidence tick; fold K-Z3 14/15/16時台, NEXT K-Z3 16時台 n 積み増し run480) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第213回 NEXT「K-Z3 現在時刻帯 16時台 n 積み増し続行, 次 run ID run480」)。live smoke 200 (/, /signup, search; pre-run + 本 tick 実測 200)。host load1 45.30 (16:27 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 16時台 run480A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 16:24:30–16:24:45 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run480A 散発クラスタ 5/20 (0.8955s/1.0030s/1.0397s/1.4144s/2.0793s) p50 0.0905s max 2.0793s / run480B cold 0/20 p50 0.0501s max 0.1470s / run480C cold 0/20 p50 0.0489s max 0.1859s, control (kotobase.net/signup) cold 0/20 p50 0.0446s max 0.3134s 完全静穏で control 分離成立、cold 群 search 側局在。run480A 散発クラスタ 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 (run479A 5/20 の約 15 分後同型再上振れ, heavy>=6/20 は run480 で未達)。16時台 (9/8) 通算 = bench run479 (6/60, 帯初) + 本 tick run480 (5/60) = 11/120 (~9.2%) の 2 セット — 帯初再上振れ → 帯内散発減衰の日中帯 high 側パターンが 16時台でも弱く継続、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行, 次 run ID は run481)。\n")

new = content.replace(marker, marker + entry, 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(new)
print("INSERTED", "falsify 第215回" in new)
print("HAS_ZWSP", "\u200b" in entry, "HAS_HASH5", "#####" in entry)
print("OC_run480", new.count("run480"))
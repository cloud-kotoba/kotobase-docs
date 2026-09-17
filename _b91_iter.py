#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
marker = "## Iteration log\n"
entry = (
    "- 2026-09-06: bench 第91回。16:08 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み "
    "(HEAD 13b826c = fetch 後 net-kotobase/main 先端一致, 乖離 0)。falsify 第93回 (run221A–C, 16:02, 16時台) を取り込み済み確認 "
    "— K-Q1 切れ手 (ii) cacao_b64 経路 harness 変更 (cosientist 実装担当) は実施範囲外。live smoke 200 (/, /signup; pre-run 計測)。"
    "host load1 9.43 (16:07 実測, gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): "
    "K-Z3 16時台 n 積み増し run222A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 16:09:49 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (~1.7%) — run222A 冒頭単発 1.182s (1番目, 散発型) "
    "p50 42.3ms, run222B/C 0/20 (p50 41.9/44.1ms), control (kotobase.net/signup) cold 0/20 p50 46.0ms max 255ms 静穏で control 分離成立、"
    "cold 群は search 側に局在。run222A 冒頭単発は B/C 0/20 で即消失し run216/217/218/219/220 型「帯内 1 窓即消失」パターンと整合 "
    "(falsify run221 0/60 完全静穏の 7 分後の弱い再現)。16時台本日分 (run221 0/60 + 本 tick 1/60) 1/120 低位帯サンプル継続。"
    "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し継続 — 16時台 n 積み増し 2 セット済みのため次の観測枠は 17時台帯)。\n"
)
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
assert content.count(marker) == 1, f"marker count={content.count(marker)}"
content = content.replace(marker, marker + entry, 1)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("iter log inserted ok")
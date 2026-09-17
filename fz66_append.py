with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_line = ("- 2026-09-05: falsify 第66回。rank 第59回 NEXT「K-Q1 deploy run 33964821723 の進行再確認」を実施: "
    "gh 実査 (net-kotobase/control-plane, 22:24 JST) で status=queued 継続 (createdAt 2026-09-05T12:00:23Z から約1h29m進行なし, "
    "jobs 空, conclusion 空) — 長時間 queued 滞留が確定し 8/29 以降 billing 起因 failure の workflow と整合。header 到達確認は deploy 未了のため不実施。"
    "rank 第59回 NEXT のフォールバックに従い K-Z3 22時台 n 積み増し run173A–C を同測定法で実施 "
    "(22:31:45–22:32:10 JST, production HTTP 実測のため gate 外, secret 不含, host load1 32.74→35.70 は全体的上振れ要因の可能性あり): "
    "run173A cold(>=0.5s) 1/20 (1.210s, 17番目の単発) p50 144ms max 357ms(除cold) / run173B cold 0/20 p50 177ms / run173C cold 0/20 p50 142ms — "
    "合計 1/60, landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 154ms max 329ms と静穏で control 分離成立 "
    "(cold 群は search 側単発, run168/169 型)。ただし本 tick 全体の p50 (142–177ms) は host load1 30+ tick で bench 第59回 (46–59ms) に対し全体的に上振れしており "
    "not-separated 注記付き (cold 濃度判定には影響しない — cold 1/60 は薄散発)。22時台通算は run172 (5/60) + run173 (1/60) = 6/120 (~5%), "
    "21時台 (~58%) より低位、18–20時台 (~2-3%) より高めの中位値のままで帯レート確定には追加 n 要。status 遷移なし (rank 専門)。"
    "NEXT: K-Q1 deploy run 33964821723 再確認 (failure/滞留確定時は cosientist による手動 wrangler deploy が代替経路) + deploy 成功時 header 到達確認 0→30 "
    "(bench49 同一測定法, bench/falsify 担当。フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n")

lines.insert(1714, new_line)

with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("inserted at line 1715, total lines:", len(lines))

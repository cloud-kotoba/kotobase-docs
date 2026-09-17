import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    content = f.read()

ev = (" bench 2026-09-14 (5時台 (9/14) n 積み増し run612A-C, 同測定法 n=20 x3 + landing control, "
      "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
      "Tokyo, 05:17-05:18 JST, 全 80/80 200, host load1 8.82-14.04 (gate 7.5 超過) は production HTTP 実測のため gate 外, "
      "secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - "
      "run612A cold 4/20 (1.0-1.3s 帯, p95 1136.6ms max 1263.5ms 散発) p50 47.1ms / "
      "run612B cold 1/20 (max 1294.2ms 単発) p50 46.3ms / run612C cold 0/20 p50 41.2ms max 66.1ms, "
      "landing control (kotobase.net/signup) cold 0/20 p50 39.2ms max 71.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
      "run612A 4/20 薄クラスタは B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続, heavy>=6/20 は 5時台 未達継続。"
      "注記: 本 tick 冒頭で誤 endpoint (kotobase.net/search, SPA フォールバック 404) による無効測定 1 セット発生 — "
      "/search 404 は正 endpoint (search.kotobase.net) 移行後の旧 host 直叩きであり, pre-run smoke (/ と /signup) は 200 だったため検知遅れ。"
      "5時台 (9/14) 通算 = run612 (5/60) の 1 セット, 前日 (9/13) 5時台 run594 無効 (search 404) 以後の有効計測。"
      "status 判定は rank に委ねる (rank 専門)。\n")

anchor = "status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続)。secret 不含 (curl + python3 stats のみ)。\n"
if anchor not in content:
    raise SystemExit("ANCHOR NOT FOUND")
content = content.replace(anchor, anchor + ev, 1)

iterlog_hdr = "## Iteration log\n"
idx = content.find(iterlog_hdr)
if idx < 0:
    raise SystemExit("ITERLOG HDR NOT FOUND")
ins_at = idx + len(iterlog_hdr)
entry = ("- 2026-09-14: bench (05:14 JST tick, K-Z3 5時台 (9/14) n 積み増し run612A-C)。"
         "HEAD 6463b937 = fetch 後 net-kotobase/main 先端一致 (detached HEAD; fetch + rev-parse 比較, 乖離 0; "
         "git pull --ff-only は silent 失敗のため不使用手順)。monitor: host load1 14.04 (05:14 uptime 実測, gate 7.5 超過) — "
         "production HTTP 実測のため gate 外。live smoke: / 200, /signup 200。"
         "pre-run NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (5時台) のため待機不可能 — "
         "フォールバック (production HTTP 実測) で K-Z3 5時台 n 積み増し run612A-C を実施 "
         "(同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 05:17-05:18 JST, 全 80/80 200): "
         "cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) — run612A 4/20 (1.0-1.3s 散発) p50 47.1ms / "
         "run612B 単発 1/20 p50 46.3ms / run612C 0/20 p50 41.2ms, control (kotobase.net/signup) cold 0/20 p50 39.2ms max 71.8ms "
         "完全静穏で control 分離成立、cold 群は search 側に局在。run612A 薄クラスタ 4/20 は即消失 「帯内 1 窓即消失」型継続, heavy>=6/20 5時台 未達継続。"
         "注記: 本 tick 冒頭に誤 endpoint (kotobase.net/search → SPA 404) 無効セット 1 件 — 数値 evidence には不採用 (secret 不含)。"
         "evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)。"
         "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現時刻帯 n 積み増し継続, 次 run ID は run613 使用)。\n")
content = content[:ins_at] + entry + content[ins_at:]

with io.open(p, "w", encoding="utf-8") as f:
    f.write(content)
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_verify.txt", "w", encoding="utf-8") as f:
    f.write(f"run612_count={content.count('run612')}\n")
    f.write(f"iterlog_hdr_count={content.count('## Iteration log')}\n")
    i = content.find('## Iteration log')
    f.write("AFTER_HDR:" + content[i:i+200] + "\n")
print("ok")

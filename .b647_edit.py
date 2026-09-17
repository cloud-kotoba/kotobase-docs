import io, os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
p = os.path.join(base, "query-cosientist.md")
with open(p, encoding="utf-8") as fh:
    txt = fh.read()

ev = ("falsify 2026-09-16 (第161回, K-Z3 23時台 2セット目 run647A-C, 同測定法 n=20 x3 + landing control, "
      "別接続 curl, Tokyo, 23:24:56-23:25:13 JST, 全 60/60 200 + control 20/20 200, "
      "正 endpoint search.yataverse.com/search?q=test, host load1 27.12/20.08/19.11 (23:25 実測, gate 7.5 超過) "
      "は production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): "
      "cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - run647A cold 4/20 (799.8-1411.9ms, 冒頭寄り散発) p50 119.2ms p95 1009.7ms / "
      "run647B cold 1/20 (854.2ms 単発) p50 67.9ms / run647C cold 0/20 p50 60.1ms max 171.5ms 完全静穏, "
      "landing control (kotoba.cloud/, 同時刻 23:25, n=20, 全 200) cold 1/20 (621.3ms 単発) p50 144.3ms max 621.3ms - "
      "control 完全静穏ならず 1 件単発 outlier につき部分的分離 (cold 下振れ幅は target 800-1412ms に対し control 621ms と浅い - not-separated-leaning note)。"
      "23時台 9/16 通算 run646+run647 = 13/120 (~10.8%, 同日 2 セット = K-Z4 要件 n>=2 sets/day を 23時台で初充足, "
      "帯日差ペア: 9/7 ~11.3% vs 9/16 ~10.8% で同水準 ×~0.96 - 9/16 が一貫高位の日中帯と異なり低位側ペア)。"
      "status 判定は rank に委ねる (rank 専門)。\n")

iter_entry = ("- 2026-09-16: falsify 第161回 (23:2x JST tick)。HEAD 8c3416c = fetch 後 net-kotobase/main 先端一致 "
              "(worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため不使用手順; "
              "terminal foreground stdout 空 = 既知のため状態確認はファイル書出経由)。monitor: host load1 21.28 (23:23 pre-run script 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), "
              "live smoke 301/301 (kotobase.net/, /signup)。rank/bench NEXT「K-Z3 23時台」は sibling (bench) が 23:08 run646 で実施済みにつき、"
              "NEXT「次 run ID は run647」に従い本 tick 23時台 2セット目 run647A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:24:56-23:25:13 JST, 全 80/80 200): "
              "cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - A 4/20 (799.8-1411.9ms 散発) + B 1/20 単発 854.2ms + C 0/20, "
              "control (kotoba.cloud/) 1/20 621.3ms 単発 outlier で部分的分離。23時台 9/16 通算 run646+run647 = 13/120 (~10.8%) で同日 2 セット = K-Z4 要件 n>=2 sets/day を 23時台で初充足 "
              "(帯日差ペア 9/7 ~11.3% vs 9/16 ~10.8% は同水準, 低位側ペア)。evidence は本ファイル末尾に追記済み (第153-160回前例のファイル末尾追記方式)。"
              "status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run648 使用)。secret 不含 (curl + python3 stats のみ)。\n")

assert "## Iteration log\n" in txt
txt = txt.replace("## Iteration log\n", "## Iteration log\n" + iter_entry, 1)

txt = txt.rstrip("\n") + "\n" + ev
with open(p, "w", encoding="utf-8") as fh:
    fh.write(txt)

# checks
n = txt.count("run647")
with open(os.path.join(base, ".b647_verify.txt"), "w", encoding="utf-8") as out:
    out.write(f"ev_count_run647={n}\n")
    out.write(f"iterlog_count={txt.count('## Iteration log')}\n")
    bad = [c for c in txt if 0x0300 <= ord(c) <= 0x036F]
    out.write(f"combining_chars={len(bad)}\n")
    out.write(f"tail_check={'falsify 2026-09-16 (第161回' in txt[-3000:]}\n")

import subprocess

doc = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
ev = ("cosientist 2026-09-15 (第153回, K-Z3 2時台 n 積み増し run624A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, "
      "02:33-02:34 JST, 全 80/80 200, 正 endpoint search.yataverse.com/search?q=test — search.kotobase.net/search は 301 → "
      "search.yataverse.com/search 読替のため新 endpoint を直接計測, host load1 10.94 (02:34 uptime 実測, gate 7.5 超過) は "
      "production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) "
      "- run624A cold 1/20 (0.664s 単発散発) p50 51.3ms max 664.2ms / run624B cold 1/20 (0.620s 単発散発) p50 44.9ms max 620.5ms / "
      "run624C cold 0/20 p50 44.3ms max 147.5ms, landing control (kotoba.cloud/ 301 読替先, 同時刻, n=20, 全 200) cold 0/20 p50 52.7ms "
      "max 155.4ms 完全静穏で control 分離成立、cold 群は search 側に局在。2時台通算 (bench run623 0/60 + 本 tick run624 2/60) "
      "2/120 (~1.7%) 低位帯継続 - 「帯内 1 窓即消失」散発単発型 (0.62-0.66s 閾値直下級の浅い単発 2 件, heavy>=6/20 未達) で、"
      "bench run623 完全静穏の直後の 2 件薄再出現は deep-night 散発型の振幅内。301 読替後 URL 運用注記: 本 tick 以後は "
      "search.yataverse.com/search (200 確認済み) を正 endpoint として使用, control は kotoba.cloud/ (200, signup は 404 で "
      "kotobase.net/signup は 301→kotoba.cloud/signup 404 につき不使用)。status 判定は rank に委ねる (rank 専門)。\n")
log = ("- 2026-09-15: cosientist 第153回 (02:26 JST tick)。HEAD ecc7974 = fetch 後 net-kotobase/main 先端一致 "
       "(worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0)。"
       "monitor: host load1 12.02 (02:26 pre-tick 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), live smoke 301/301 "
       "(kotobase.net/ → kotoba.cloud/docs/graph/, kotobase.net/signup → kotoba.cloud/signup 404)。"
       "rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (2時台) のため待機不可能 — フォールバック (production HTTP 実測) "
       "で K-Z3 2時台 n 積み増し run624A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 02:33-02:34 JST, 全 80/80 200): "
       "cold(>=0.5s) 2/60 (~3.3%) - A 1/20 (0.664s) + B 1/20 (0.620s) 閾値直下級の浅い単発散発 2 件, C 0/20, control (kotoba.cloud/) "
       "0/20 完全静穏で control 分離成立。2時台通算 2/120 (~1.7%) 低位帯継続。301 読替後の正 endpoint 移行 (search.yataverse.com) を "
       "本 tick で直接計測し確認済み。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる "
       "(rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し継続)。secret 不含 (curl + python3 stats のみ)。\n")

with open(doc, "a") as f:
    f.write("\n" + ev)
    f.write(log)
print("appended")

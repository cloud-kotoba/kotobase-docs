import io, re

p = "query-cosientist.md"
s = io.open(p, encoding="utf-8").read()

header = "## Iteration log\n"
i = s.find(header)
assert i != -1, "header missing"
assert s.count(header) == 1, "duplicate header"

entry = ("- 2026-09-16: rank 第279回。07:0x JST tick。HEAD 2db320c = bench 第222回 (05:0x, K-Z3 5時台 run630 evidence + iter entry) = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; detached HEAD; git pull --ff-only 不使用手順; terminal foreground stdout 空 = 既知のため状態確認はファイル書出経由; '## Iteration log' ヘッダ 1 件事前確認)。monitor: host load1 10.68 (07:02 pre-run 実測, gate 7.5 超過 — rank は測定せず状態正本更新のみのため影響なし)。live smoke 301/301 (/, /signup; pre-run monitor 計測の記録どおり)。rank 第278回 (98bc575, 03:0x) 以降の新規確定 evidence は 2 commit 2 run、ともに K-Z3 9/16 深夜帯 (正 endpoint search.yataverse.com/search?q=test, control kotoba.cloud/): (1) falsify 第155回 commit c4c3d72 run635A-C (3時台 9/16): cold 1/60 (~1.7%), control 分離成立 — 3時台日次系列 3 日完成: 9/7 ~2.1% / 9/14 run611 ~18.3% / 9/16 ~1.7% — spread ~11 倍 (両端が低位側の U 字型, K-Z4 材料)。(2) bench 第222回 commit 2db320c run630A-C (05:08-05:10 9/16, 5時台): cold 10/60 (~16.7%) — run630A 冒頭集中クラスタ 9/20 (0.5-0.97s) p50 141.3ms / B 単発 1/20 / C 0/20, control 0/20 完全静穏で分離成立。5時台日次系列 3 日完成: 9/9 ~2.8% / 9/14 run612 ~8.3% / 9/16 ~16.7% — spread ~6 倍, 9/16 分が系列最大値で run630A 型 heavy (9/20, run271A/625A 型) は 5時台で初出 — 5時台が従来「深夜帯中最も静穏な帯」から中位帯へ再構成方向の 3 日目データ点 (K-Z4 材料)。取り込み判定: (a) K-Z4: 3時台 3 日系列 (spread ~11 倍) と 5時台 3 日系列 (spread ~6 倍, 系列単調増加) の 2 帯追加で低位〜中位帯日次系列が更に拡充 — ただし K-Z4 要件 (同帯 n>=2 sets/day × 2 日以上) は各日 1-2 セットのまま変化なし — status 遷移なし (open 継続)。(b) K-Z3: status 遷移なし (観測継続; 深夜帯低位帯で 3 日 spread が 2 帯同時に確定したが帯間勾配の決定的判定に未達)。(c) K-Q1: 変動なし — host load1 10.68 gate 超過継続で cacao_b64 harness 変更未実施, 最上位維持。(d) K-Z2/K-S1/K-S2: evidence なし変動なし。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3/K-Z4 (観測最優先) > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 7時台 (9/16) n 積み増し run637 (現時刻帯; 7時台は 9/6 ~2.2% / 9/14 run613 ~16.7% の 2 日 spread ~7.6 倍系列で, 3 日目が K-Z4 日次系列の分解能を最も上げる直接材料; bench/falsify フォールバック枠が run637 を先取する場合は別 run ID 読替の従来手順; 正 endpoint search.yataverse.com/search?q=test, control は kotoba.cloud/)。secret は一切記録せず。\n")

new = s[:i + len(header)] + entry + s[i + len(header):]
io.open(p, "w", encoding="utf-8").write(new)
print("rank279 inserted; header count:", new.count(header))

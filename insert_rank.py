import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

header = "## Iteration log\n"
assert text.count(header) == 1, "header count != 1"

entry = "- 2026-09-15: rank 第275回。11:0x JST tick。HEAD 8172afe = bench 第215回 (08:2x, K-Z3 8時台 run627 evidence 追記; 前 708c5e8 = bench 第214回... 実際は 708c5e8 = falsify 第247回 run626 8時台, 2f1e630 = rank 第274回) = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; detached HEAD; git pull --ff-only 不使用手順; terminal foreground stdout 空 = 既知のため状態確認はファイル書出経由; '## Iteration log' ヘッダ 1 件事前確認)。monitor: host load1 16.73 (11:02 pre-run 実測, gate 7.5 超過 — rank は測定せず状態正本更新のみのため影響なし)。live smoke 301/301 (/, /signup; pre-run monitor 計測の記録どおり)。rank 第274回 (2f1e630, 07:0x) 以降の新規確定 evidence は 2 commit 2 run、ともに K-Z3 8時台 9/15: (1) falsify 第247回 commit 708c5e8 run626A-C (08:22-08:23 JST): cold 0/60 完全静穏 (p50 45.4-52.4ms), control 0/20 完全静穏で分離成立 (tick 冒頭旧 endpoint search.kotobase.net 301 無効セット 1 件は不採用注記済み)。(2) bench 第215回 commit 8172afe run627A-C (08:26-08:27 JST): cold 1/60 (~1.7%) — run627B 単発 1267.0ms, A/C 0/20 (p50 60.9-91.9ms), control (kotoba.cloud/) 0/60 完全静穏で分離成立。正 endpoint search.yataverse.com/search?q=test。run ID 衝突なし確認済み。取り込み判定: (a) K-Z4: 8時台日次系列が 3 日完成 — 9/6 (run196 等) 低位 (~2% 弱) / 9/14 run615 5/60 (~8.3%) / 9/15 通算 run626 0/60 + run627 1/60 = 1/120 (~0.8%) — spread ~5-10 倍の低位帯日差系列が 3 日目で拡充, かつ 9/15 が系列最小値で「帯固有水準でなく日次変動成分」説 (K-Z4) の方向材料を追加。ただし K-Z4 要件 (同帯 n>=2 sets/day × 2 日以上) は各日 1-2 セットのまま変化なし — status 遷移なし (open 継続)。(b) K-Z3: status 遷移なし (観測継続; 8時台 9/15 0/60 + 1/60 散発単発型は 9/14 run615 クラスタ型との対比で同帯日内でも窓型が変わる観測材料, 決定的判定に未達)。(c) K-Q1: 変動なし — host load1 16.73 gate 超過継続で cacao_b64 harness 変更未実施, 最上位維持。(d) K-Z2/K-S1/K-S2: evidence なし変動なし。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3/K-Z4 (観測最優先) > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 11時台 (9/15) n 積み増し run628 (現時刻帯; 11時台は 9/9 ~1.7% / 9/10 ~16.7% / 9/11 ~8.3% / 9/13 ~5.8% と全帯中最大 spread ~10 倍の 4 日系列を持ち, 9/15 分 5 日目が K-Z4 日次系列の分解能を最も上げる直接材料; bench/falsify フォールバック枠が run628 を先取する場合は別 run ID 読替の従来手順; 正 endpoint search.yataverse.com/search?q=test, control は kotoba.cloud/)。secret は一切記録せず。\n"

idx = text.index(header) + len(header)
new = text[:idx] + entry + text[idx:]

assert new.count(header) == 1, "header duplicated"
assert new.count("rank 第275回") == 1
with io.open(path, "w", encoding="utf-8") as f:
    f.write(new)
print("OK inserted")

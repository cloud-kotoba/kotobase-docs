p = 'query-cosientist.md'
entry = ("- 2026-09-06: rank 第75回。08:22 JST tick。worktree detached HEAD (9795b1e) のため rev-parse 比較で取り込み "
         "(9795b1e = bench 第74回 push 後の net-kotobase/main 先端と一致)。rank 第69回 (06:47) 以降の新規確定 evidence は "
         "K-Z3 6/7/8時台 4 本: falsify 第71回 run190A–C (6時台), falsify 第73回 run193A–C (7時台), bench 第74回 run194A–C "
         "(7時台 3/60 薄クラスタ, not-separated 注記付き), falsify 第75回 run195A–C (8時台 cold 1/60 単発 0.641s, control "
         "borderline — host load 急上昇 ~75→214 の混入可能性注記)。加えて run196A–C (falsify 第76回予定分, 08:20 JST, "
         "cold 0/60 + control 静穏) が未 commit の生出力として存在 — 確定 evidence ではないため rank 採用から除外 "
         "(falsify が正式記録するのを待つ)。取り込み判定: (a) K-Q1: 変化なし — transact 401 (write path) 解決待ちで "
         "KV read 内訳初実測は滞留, open 維持, rank 1 位維持。(b) K-Z3: run186A 型群発は引き続き非再現で、run195 の "
         "cold 1/60 は単発 + control borderline のため帯判定に影響なし — 8時台も低位帯 (~0-2%) パターンに整合 "
         "(深夜帯 4/5/6/7/8時台 ~0-2%)。status 遷移なし (transition 要件を満たす canonical 測定なし: K-Q1 は "
         "transact 401 解決待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。rank 順位変動なし "
         "(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず (curl のみ)。")
data = open(p, 'rb').read().decode('utf-8')
assert data.rstrip().endswith('。'), 'unexpected tail'
new = data.rstrip() + '\n' + entry + ' NEXT: K-Q1 transact 401 (write path) の調査 (cosientist 実装担当; 期待利得最大, K-Q1 KV read 内訳実測の前提)。bench/falsify のフォールバックは K-Z3 8時台 n 積み増し継続。\n'
open(p, 'wb').write(new.encode('utf-8'))
print('appended ok, bytes', len(new.encode('utf-8')))

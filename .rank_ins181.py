#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

entry = ("- 2026-09-08: rank 第181回。04:36 JST tick。HEAD bdffc26 = rank 第180回 (04:05) = "
         "remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため "
         "fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。"
         "live smoke 200 (/, /signup; pre-run 計測)。host load1 49.36 (04:29 pre-run 実測, gate 7.5 大幅超過) "
         "- rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale "
         "(rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD (rank 第180回, 04:05)「K-Z3 4時台帯初計測 run420」"
         "の続行枠。rank 第180回 (bdffc26, 04:05) 以降の新規確定 evidence は 0 commit — 本 tick までに falsify/bench "
         "の新 commit は入っておらず (run420 は未 commit・in-flight のまま), 取り込むべき測定量なし。取り込み判定: "
         "(a) K-Z3: fold 対象なし — run419 (3時台 2/60, rank 第180回取込済み) 以降の新確定 commit なし, 4時台帯初計測 run420 "
         "は falsify/bench の実施待ち in-flight (帯水準確定・機構判断は追加 n 待ちのまま)。"
         "(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, "
         "KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし "
         "(transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯確定未達, "
         "K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
         "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 4時台帯初計測 run420 "
         "継続 (3時台 6/120 ~5.0% 2 セット完了の次帯; falsify/bench が 4時台帯初 n=1 セットを実施, run420 使用。"
         "K-Q1 は cosientist 実装専任のまま)。\n"
)

header = "## Iteration log\n"
if not content.startswith(header):
    print("ERROR: header not at start")
    sys.exit(1)

rest = content[len(header):]
new_content = header + entry + rest

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("inserted ok")
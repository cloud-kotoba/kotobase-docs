#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

anchor = "## Iteration log\n"

entry = """## Iteration log
- 2026-09-06: rank 第111回。22:34 JST tick。HEAD e4fe1da = remote net-kotobase/main 一致 (git pull --ff-only, 乖離 0, worktree 先端 = bench 第102回 run253 push 済み)。rank 第110回 (b24add0, 22:19) 以降の新規確定 evidence は 2 commit: (1) cosientist 第85回 (304121b, 22:23) — K-Q1 cut (iii) did:key (Ed25519) CACAO harness の静的実査反証: production engine の datomic.transact write gate (resolve-transact-auth, auth.cljs:404-418) は KOTOBASE_BISCUIT_AUTH_MODE=required で Biscuit scheme のみ受理 (cacao 分岐 verify-transact-auth は到達不能) のため cacao_b64/did:key いずれの mint 経路でも write 実測は構造的に実行不能 (401「Biscuit authorization is required」で遮断)。観測 401 は credential-type 不整合ではなく verify-biscuit-write の delegation 検証失敗が主因 — transact 401 の静的切れ手 (a)/(i)/(ii)/(iii) 全滅、残るは engine の Biscuit delegation-for-request 動的照合 (正規 tenant write path, service-account/operator, cosientist 実装専任・rank 測定指示対象外)。(2) bench 第102回 (e4fe1da, 22:30) — K-Z3 22時台 n 積み増し run253A-C (22:25:08-22:25:44 JST, cold 6/60 ~10.0%: run253A heavy 5/20 クラスタ 1.047-2.013s 冒頭集中 + B 0/20 + C 単発 1 件, control cold 0/20 p50 60.2ms max 139ms 完全静穏で control 分離成立 clean-tick, host load1 51-53 で run252 の host-load 汚染/control not-separated を解消)。取り込み判定: (a) K-Q1: 変動 — 上記 cosientist 第85回で cut (iii) 反証を取り込み transact 401 の全静的切れ手が棄却され、残余の動的切れ手は cosientist 実装専任 (正規 tenant write path 経由の biscuit delegation-for-request 動的照合) へ。KV read 内訳初実測 (非空 graph query + x-kotobase-kv-stats) はその成立が前提で滞留継続のまま最上位維持。(b) K-Z3: run253 を取り込み 22時台通算 = falsify run252 (9/60 borderline) + bench run253 (6/60) = 15/120 (~12.5%) — 21時台 (~4.0%) と 9/5 22時台 (7/180 ~3.9%) より明確に高位で夜帯 traffic 遷移説の弱い支持方向 (run252A/253A 型 heavy クラスタの弱連続再現)。run253 は n=1 clean-tick で帯確定には追加 n 要、深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局の上振れかの切り分けが次の焦点。帯別追加 n の限界情報利得は低下済みのため K-Z3 は fallback 専門のまま。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ちの動的切れ手のみ, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 22時台 15/120 ~12.5% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 78.12 (22:32 実測, gate 7.5 大幅超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。
  NEXT: K-Z3 22時台追加 n or 23時台帯初計測 — 22時台は run253 (clean-tick 6/60) で高位 ~12.5% を補強したが n=1 セット (15/120) で帯確定には追加 n 要。cron 時刻帯が 22時台の間は 22時台 n 積み増しで帯確定へ追加 1 セット (run253 の継続性/即消失の確認, host load gate 超過時は production HTTP フォールバックの従来手順)、時間帯移行後は 23時台帯初計測 (深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局の上振れかの切り分け — traffic 依存説への最終的な判定材料)。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。

"""

if anchor in txt:
    txt = txt.replace(anchor, entry, 1)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    with io.open("/tmp/rank_iter.txt", "w", encoding="utf-8") as f:
        f.write("ITER_LOG_INSERTED\n")
else:
    with io.open("/tmp/rank_iter.txt", "w", encoding="utf-8") as f:
        f.write("ANCHOR_NOT_FOUND\n")
import io
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(P,encoding="utf-8").readlines()

# --- 1. Append run258 evidence to K-Z3 hypothesis row (line index 256 = line 257) ---
kz3_ev = ("bench 2026-09-06 (第104回, K-Z3 22時台 n 積み増し run258A–C, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, Tokyo, 22:55:05 JST 開始, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 26.61 (pre-run, gate 7.5 超過) は production HTTP 実測のため gate 外 — rank 第112回 NEXT "
"「K-Z3 22時台追加 n or 23時台帯初計測」は現時刻 22時台のため 22時台 n 積み増し): "
"cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run258A cold 3/20 (3/4番目隣接 1.695s/1.123s + 7番目 1.543s, "
"早先頭 cluster 型) p50 56.6ms / run258B cold 0/20 p50 55.9ms max 137.0ms / run258C cold 0/20 p50 50.0ms max 138.8ms, "
"control (kotobase.net/signup) cold 0/20 p50 49.8ms max 123.4ms 静穏で control 分離成立、cold 群は search 側に局在。"
"run258A 早先頭 cluster 3 件は B/C 0/20 で即消失し run252A/253A 型 heavy cluster (6+2+1/20) の弱い再現 (3/20, heavy 未満) で "
"「帯内 1 窓即消失」単発散発〜早先頭 cluster 型継続。22時台通算は rank 第112回 fold (22/360 ~6.1%) + 本 tick 3/60 = 25/420 (~6.0%) — "
"21時台 (~4.0%)・9/5 22時台 (7/180 ~3.9%) より高位傾向を 6 セットで維持 (traffic 遷移説の判定は rank に委ねる)。status 判定は rank に委ねる (rank 専門)。")

idx=[i for i,l in enumerate(lines) if l.startswith("| K-Z3 | worker |")][0]
# ensure not already folded
assert "run258" not in lines[idx], "run258 already in K-Z3 row"
lines[idx]=lines[idx].rstrip("\n")+kz3_ev+"\n"

# --- 2. Insert rank 113 iteration log entry after "## Iteration log" line ---
log_ev = ("- 2026-09-06: rank 第113回。23:02+ JST tick。HEAD 1768f6e = remote net-kotobase/main 一致 "
"(git fetch net-kotobase rc 0, rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch + rev-parse で取り込み)。"
"rank 第112回 (968b4c5, 22:53) 以降の新規確定 evidence は 1 commit: bench 第104回 run258A-C (1768f6e, 22:55:05, "
"K-Z3 22時台 n 積み増し, cold 3/60 ~5.0% — run258A 早先頭 cluster 3/20 1.695s/1.123s/1.543s, B/C 0/20 即消失, "
"control cold 0/20 静穏で分離成立, host load1 26.61 clear-ish tick, run252A/253A 型 heavy の弱い再現 3/20 heavy 未満)。"
"取り込み判定: (a) K-Z3: run258 を取り込み 22時台通算 = 22/360 (~6.1%) + 3/60 = 25/420 (~6.0%)。"
"rank 第111/112回の「22時台高位 ~12.5%」は run252A/253A heavy クラスタ (早帯 2 窓) に支配され、続く run254/255/256×2/258 は "
"2/60・1/60・2/60・3/60 の低位単発散発〜早先頭小型 cluster へ減弱継続 — 22時台帯全体 ~6.0% は 21時台 (~4.0%)・9/5 22時台 (~3.9%) より "
"やや高位寄りのまま 6 セットで維持 (夜帯 traffic 遷移説の弱い支持継続, 帯水準確定には未達 — run252A/253A 相当の heavy burst が 22時台帯内で "
"再発なければ高位は帯水準非持続の単一窓寄りと確定)。現時刻 23時台へ移行のため次の観測枠は 23時台帯初計測 (深夜帯 ~26-31% 平坦パターンへの "
"収束か 22時台限局の上振れかの切り分け — traffic 依存説への最終判定材料の一つ)。"
"(b) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。(c) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は "
"cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。"
"status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・22時台 25/420 ~6.0% は "
"mechanisms 判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
"rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 22時台 25/420 ~6.0% は順位を変えない)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 33.46 (23:02 pre-run, gate 7.5 超過) — rank 担当は測定を行わず "
"状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。"
"  NEXT: K-Z3 23時台帯初計測 — 22時台は 6 セット 25/420 ~6.0% で帯水準の目途は立ちつつある (run252A/253A heavy 以外は低位単発散発型、"
"heavy burst 非再現なら「22時台高位=単一窓寄り・帯非持続」)。現時刻 23時台 (23:02) のため 23時台帯初計測が現観測枠 — "
"深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局の上振れかの切り分け (9/5 深夜帯との同日対比, traffic 依存説への最終判定材料)。"
"host load gate 超過時は production HTTP フォールバックの従来手順。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 "
"(正規 tenant write path 経由の biscuit delegation 動的照合)。")

log_idx=[i for i,l in enumerate(lines) if l.strip()=="## Iteration log"][0]
lines.insert(log_idx+1, log_ev+"\n")

open(P,"w",encoding="utf-8").writelines(lines)
print("DONE kz3len", len(lines[idx]))
import io, sys

KZ3_EV = (" bench 2026-09-07 (第131回, K-Z3 6時台 n 積み増し run316A–C, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, Tokyo, 06:12:43–06:12:50 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 29.56 (06:12 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
"cold(>=0.5s) 1/0/0 per 20 = 1/60 — run316A cold 単発散発 0.8151s 13番目 p50 46.2ms max 72.2ms / run316B cold 0/20 "
"p50 40.3ms max 88.7ms / run316C cold 0/20 p50 41.4ms max 84.6ms, control (kotobase.net/signup) cold 0/20 "
"p50 39.9ms max 117.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。run316A 単発は B/C 0/20 + control 0/20 "
"で即消失し「帯内 1 窓即消失」散発単発型継続 (run315 帯初散発ペア 2/60 の直後の単発再出現, heavy クラスタ "
"run271A 6/20 型は run271A 以降 41 セット連続非再現)。6時台通算 (run315 2/60 + 本 tick run316 1/60) = 3/120 (~2.5%) "
"の 2 セット、deep-night 累計 run275..316 = 43/2520 (~1.71%) の 42 セットで低位帯水準継続 — 「深夜発から朝の帯境」"
"移行帯での cold 散発継続は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
"status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 6時台 n 積み増し継続、"
"次 run ID は run317 使用)。")

ITER = ("- 2026-09-07: bench 第131回。06:13 JST tick。HEAD 0b76dfb = rank 第139回 (run315 fold) = remote "
"net-kotobase/main 一致 (fetch net-kotobase rc 0 + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, "
"fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 31.41 (06:08 uptime 実測) → 29.56 (06:12 測定時, "
"gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第139回 NEXT「K-Z3 current-band(6時台) "
"n-add (run316)」に従い 現時刻帯 6時台 n 積み増し run316A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, "
"06:12:43–06:12:50 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 — "
"run316A cold 単発散発 0.8151s 13番目 p50 46.2ms max 72.2ms / run316B cold 0/20 p50 40.3ms max 88.7ms / run316C cold 0/20 "
"p50 41.4ms max 84.6ms, control (kotobase.net/signup) cold 0/20 p50 39.9ms max 117.9ms 完全静穏で control 分離成立、cold 群は "
"search 側に局在。run316A 単発は B/C 0/20 即消失で run315 帯初散発ペア (2/60) 直後の単発再出現 — 「帯内 1 窓即消失」散発単発型継続 "
"(heavy クラスタ run271A 6/20 型は run271A 以降 41 セット連続非再現)。6時台通算 (run315 2/60 + 本 tick 1/60) = 3/120 (~2.5%) "
"の 2 セット、deep-night 累計 run275..316 = 43/2520 (~1.71%) の 42 セット低位帯水準継続 — 深夜帯 traffic 最低帯から朝の帯境での "
"cold 散発継続は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる "
"(rank 専門)。secret は一切記録せず (curl のみ + 統計 python)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 6時台 n 積み増し継続、"
"次 run ID は run317 使用)。\n")

with open('query-cosientist.md','r',encoding='utf-8') as f:
    lines=f.readlines()

# line 279 (index 278) = K-Z3 evidence row; append evidence before trailing newline
lines[278] = lines[278].rstrip('\n') + KZ3_EV + '\n'

# assert header at line 358 (idx 357) and rank139 at idx 358
assert lines[357].startswith('## Iteration log'), lines[357][:40]
assert 'rank 第139回' in lines[358][:200], lines[358][:100]
lines.insert(358, ITER)

with open('query-cosientist.md','w',encoding='utf-8') as f:
    f.writelines(lines)
print("INSERTED ok, now total lines:", len(lines))
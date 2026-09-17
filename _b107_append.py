import io

F = "query-cosientist.md"
src = io.open(F, "r", encoding="utf-8").read()

# --- K-Z3 evidence: insert bench run264 line after the run263 evidence line ---
run263_anchor = "falsify 2026-09-06 (第120回, K-Z3 23時台 n 積み増し run263A–C"
i = src.find(run263_anchor)
assert i != -1, "run263 anchor not found"
# end of that line = next newline after anchor start
j = src.find("\n", i)
assert j != -1, "no newline after run263"
run264_ev = (
    " bench 2026-09-06 (第107回, K-Z3 23時台 n 積み増し run264A–C — rank 第115回 NEXT"
    "「K-Z3 23時台 n 積み増し継続...次 run ID は run264 使用」の run264 枠として実施, 同測定法"
    " n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:39:54–23:40:1x JST, 全 80/80 200,"
    " 正 endpoint search.kotobase.net/search?q=test, host load1 30.69 (23:37 pre-run) → 14.01"
    " (23:39 測定時 uptime 実測) は production HTTP 実測のため gate 外, secret 不含 — curl のみ):"
    " cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run264A 単発 1.324s (1件, 散発) p50 0.056s /"
    " run264B cold 0/20 p50 0.051s max 0.112s / run264C cold 0/20 p50 0.053s max 0.162s,"
    " control (kotobase.net/signup) cold 0/20 p50 0.045s max 0.104s 完全静穏で control 分離成立、"
    " cold 群は search 側に局在。run264A 単発は B/C 0/20 + control 0/20 で即消失し"
    " run259A/261A/262A/B 型「帯内 1 窓即消失」散発単発型継続 (run260A 8/20, run263A 5/20 heavy"
    " クラスタの再現なし — 散発減弱方向続行, 本 tick は 23時台 6 セット目で最も低い cold 濃度)。"
    " 23時台通算 = falsify run260 (8/60) + bench run259 (4/60) + falsify run261 (3/60) +"
    " bench run262 (2/60) + falsify run263 (5/60) + 本 tick run264 (1/60) = 23/360 (~6.4%) で"
    " 6 セット連続 cold>0 — 深夜帯 23時台 (traffic 最低帯) で cold 連続出現は K-Z3 traffic 依存説へ"
    " の反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし 6 セットとも「帯内 1 窓即消失」"
    " 型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)
src = src[:j] + "\n" + run264_ev + src[j:]

# --- Iteration log: insert bench 第107回 entry at top, after "## Iteration log\n" ---
hdr = "## Iteration log\n"
h = src.find(hdr)
assert h != -1, "iteration log header not found"
k = h + len(hdr)
bench_iter = (
    "- 2026-09-06: bench 第107回。23:40 JST tick。worktree detached HEAD のため fetch"
    " net-kotobase + rev-parse 比較で取り込み (fetch rc 0, HEAD 4f54f07 = net-kotobase/main"
    " 先端一致, 乖離 0; git pull --ff-only は detached のため不可)。rank 第115回 (23:39,"
    " run262+run263 fold 済み, 23時台通算 22/300 ~7.3%, NEXT「次 run ID は run264 使用...23時台"
    " n 積み増し続行」) を取り込み — 本 tick は run264 枠で 23時台 n 積み増しを実施。live smoke"
    " 200 (/, /signup; pre-run 計測)。host load1 30.69 (23:37 pre-run uptime 実測) → 14.01"
    " (23:39 測定時 uptime 実測; いずれも gate 7.5 超過) のため local 測定は拒否し production"
    " HTTP フォールバック (gate 外)。K-Z3 run264A–C (同測定法 n=20 × 3 + landing control,"
    " 別接続 curl, 23:39:54–23:40:1x JST, 全 80/80 200, 正 endpoint"
    " search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run264A"
    " 単発 1.324s (散発) p50 0.056s / run264B 0/20 p50 0.051s / run264C 0/20 p50 0.053s,"
    " control (kotobase.net/signup) cold 0/20 p50 0.045s max 0.104s 静穏で control 分離成立、"
    " cold 群は search 側に局在。run264A 単発即消失で「帯内 1 窓即消失」散発単発型継続、23時台通算"
    " 23/360 (~6.4%) の 6 セット連続 cold>0。status 遷移なし (rank 専門)。secret は一切記録せず"
    " (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 23時台"
    " n 積み増し続行 or 24時台帯初計測)。\n"
)
src = src[:k] + bench_iter + src[k:]

io.open(F, "w", encoding="utf-8").write(src)
print("inserted ok; new len", len(src))
#!/usr/bin/env python3
import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
EVID = (" bench 2026-09-07 (第182回, K-Z3 22時台 2セット目 run402 (falsify 第175回 run401 の独立積み増し, "
        "run402 は falsify NEXT 指定どおり), 同測定法 n=20 × 3 + landing control, 別接続 curl, "
        "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
        "22:31:28–22:32:11 JST, 全 80/80 200, host load1 32.16 (22:32 uptime 実測) は production HTTP 実測のため gate 外, "
        "secret 不含 — curl + python stats のみ): cold(>=0.5s) 7/1/1 per 20 = 9/60 (~15%) — "
        "run402A cold 7/20 頭クラスタ pos1,2,4,5 (1.5–2.5s deep) + 尾クラスタ pos13,14,15 p50 292ms / "
        "run402B 単発 1/20 (1.515s pos9) p50 230ms / run402C 単発 1/20 (0.573s pos2) p50 250ms, "
        "control (kotobase.net/signup) cold 1/20 (0.665s pos20) borderline not-separated 注記 — "
        "search p50 230–292ms vs control p50 250ms と全体的上振れで latency 絶対値分離は不成立 (host load/traffic 混入), "
        "cold 濃度は search 9/60 対 control 1/20 で search 側に濃い。22時台 (9/7) 通算 = falsify run401 (8/60) + 本 run402 (9/60) "
        "= 17/120 (~14.2%) 高位帯 — 21時台 (19/300 ~6.3%)・20時台 (~5.6%) より高位で夜帯 traffic 遷移説の弱い支持方向継続、"
        "日中低位帯 (~2–7%) との対比顕著, A 両セット 7/20 散発/heavy で重複再現")

ILOG = ("- 2026-09-07: bench 第182回。22:33 JST tick。HEAD 8568136 = rank 第171回 (22:18) = remote net-kotobase/main 一致 "
        "(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground 出力不可=既知)。"
        "live smoke 200 (/, /signup; pre-run 計測)。host load1 32.16 (22:32 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 "
        "— 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」"
        "は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (falsify 第175回 run401 済)「委ねる ... "
        "次 run ID は run402 使用」の run402 枠を本 tick 実施 (.b402 既存なし=衝突なし確認, 22時台 2セット目)。"
        "K-Z3 22時台 run402A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
        "正 endpoint search.kotobase.net/search?q=test, 22:31:28–22:32:11 JST, 全 80/80 200, secret 不含): "
        "cold(>=0.5s) 7/1/1 per 20 = 9/60 (~15%) — run402A cold 7/20 頭クラスタ pos1,2,4,5 (1.5–2.5s deep) + 尾 pos13,14,15 p50 292ms / "
        "run402B 単発 1/20 (1.515s pos9) p50 230ms / run402C 単発 1/20 (0.573s pos2) p50 250ms, "
        "control (kotobase.net/signup) cold 1/20 (0.665s pos20) borderline not-separated 注記 "
        "(search p50 230–292ms vs control p50 250ms 全体的上振れで latency 絶対値分離不成立, cold 濃度は search 9/60 対 control 1/20 で search 側に濃い)。"
        "22時台 (9/7) 通算 = falsify run401 (8/60) + 本 run402 (9/60) = 17/120 (~14.2%) 高位帯 — falsify run401 と同水準 (13.3% vs 15%) で corroborate, "
        "21時台 (19/300 ~6.3%)・20時台 (~5.6%) より高位の夜帯 traffic 遷移説の弱い支持方向継続 (日中低位帯 ~2–7% との対比顕著)。"
        "status 判定は rank に委ねる。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
        "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 22時台 n 積み増し続行、次 run ID は run403 使用)。")

with io.open(p, encoding="utf-8") as fh:
    lines = fh.readlines()

# sanity anchors
kz3_idx = None
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.lstrip().startswith("| K-Z3 |"):
        kz3_idx = i
    if ln.startswith("## Iteration log") and hdr_idx is None:
        hdr_idx = i
assert kz3_idx is not None, "K-Z3 row not found"
assert hdr_idx is not None, "Iteration log header not found"
assert kz3_idx < hdr_idx, "unexpected order"

# edit 1: append evidence to K-Z3 row (strip its trailing newline, append)
before = lines[kz3_idx]
assert before.endswith("\n"), "KZ3 row missing trailing newline"
lines[kz3_idx] = before[:-1] + EVID + "\n"

# edit 2: insert iter-log entry right after header (newest first)
lines.insert(hdr_idx + 1, ILOG + "\n")

with io.open(p, "w", encoding="utf-8") as fh:
    fh.writelines(lines)
print("ok kz3=%d hdr=%d" % (kz3_idx + 1, hdr_idx + 1))
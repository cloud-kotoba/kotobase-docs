FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(FN, encoding="utf-8").read().split("\n")

hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    raise SystemExit("header not found")

entry = (
 "- 2026-09-06: falsify 第121回。23:47 JST tick。worktree detached HEAD (HEAD cbbeac1 = net-kotobase/main 先端一致, fetch net-kotobase + rev-parse 比較で確認, 乖離 0)。live smoke 200 (/, /signup; pre-run 計測)。host load1 13.69 (23:47 uptime 実測, gate 7.5 超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
 "rank 第115回 NEXT「K-Z3 23時台 n 積み増し継続...次 run ID は run264 使用」に従い 現在時刻帯 23時台 n 積み増しを実施 — ただし rank 第115回以降に bench 第107回 (23:40) が run264 を、cosientist 第116回 (23:44) が run265 を先行 commit 済みのため、本測は run266 に読替 (run216/run256/run263 前例で 23時台内の独立 2 計測, 本測 23:47): "
 "K-Z3 run266A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 23:47:12–23:47:27 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — "
 "run266A 単発 1.2092s (19番目 散発) p50 0.083s / run266B 0/20 p50 0.064s / run266C 0/20 p50 0.069s, control (kotobase.net/signup) cold 0/20 p50 0.062s max 0.118s 静穏で control 分離成立、cold 群は search 側に局在。"
 "run266A 単発即消失で「帯内 1 窓即消失」散発単発型継続、23時台通算 25/480 (~5.2%) の 8 セット連続 cold>0。"
 "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 23時台 n 積み増し続行 or 24時台帯初計測)。"
)

lines.insert(hdr_idx + 1, entry)
open(FN, "w", encoding="utf-8").write("\n".join(lines))
print("iter log inserted at", hdr_idx + 2)
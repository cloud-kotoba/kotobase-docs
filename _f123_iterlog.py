import io

FN = "query-cosientist.md"
ANCHOR = "## Iteration log"

NEW = ("- 2026-09-07: falsify 第123回。00:15 JST tick。worktree detached HEAD (HEAD 32249e4 = "
       "net-kotobase/main 先端一致, fetch net-kotobase + rev-parse 比較で確認, 乖離 0)。live smoke 200 "
       "(/, /signup; pre-run 計測)。host load1 36.14 (00:16 uptime 実測, gate 7.5 大幅超過) のため "
       "local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第117回 NEXT「K-Z3 24時台 "
       "n 積み増し継続...次 run ID は run270 使用」に従い 現時刻帯 0時台(24時台) n 積み増し run270A-C "
       "を実施 (同測定法 n=20 x 3 + landing control, 別接続 curl, 00:16:59 JST, 全 80/80 200, "
       "正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
       "- run270A 単発 1.0723s (10番目), B/C 0/20 即消失, control cold 0/20 p50 0.043s max 0.119s "
       "完全静穏で control 分離成立、cold 群は search 側に局在。run270A 単発即消失で「帯内 1 窓即消失」"
       "散発単発型継続、24時台通算 (run268 2/60 + run269 3/60 + 本 tick 1/60) 6/180 (~3.3%) の "
       "3 セット連続 cold>0。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 "
       "python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、"
       "次 run ID は run271 使用)。"
       )

with io.open(FN, "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = None
for i, ln in enumerate(lines):
    if ln.startswith(ANCHOR):
        idx = i
        break
assert idx is not None, "anchor not found"

out = lines[:idx+1] + [NEW + "\n"] + lines[idx+1:]

with io.open(FN, "w", encoding="utf-8") as f:
    f.writelines(out)

print("iteration log entry inserted after line", idx+1)
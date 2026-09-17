import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()

evidence = (
    " bench 2026-09-06 (第80回, K-Z3 10時台 3セット目 run204A–C, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, Tokyo, 10:35–10:42 JST, 全 80/80 200, host load1 70–101 (高負荷 tick) は production HTTP "
    "実測のため gate 外): run204A cold(>=0.5s) 0/20 p50 302ms max 507ms / run204B cold 0/20 p50 196ms max 356ms / "
    "run204C cold 0/20 p50 232ms max 408ms — cold 0/60。ただし本 tick 全体の p50 (196–302ms) と max (356–507ms) は "
    "host load 高騰 (~100) tick の全体的上振れで landing control (kotobase.net/signup, 同時刻, n=20, 全 200) も "
    "p50 241ms max 441ms と同程度に上振れしており borderline not-separated (cold 濃度判定 0/60 には影響なし — "
    "閾値超過は 1 件も出ず)。10時台通算 (bench run202 4/60 + falsify run203 1/60 + 本 tick 0/60) で 5/180 (~2.8%) "
    "の低位帯。status 判定は rank に委ねる (rank 専門)。"
)

anchor = "| K-Z3 | worker |"
idx = content.find(anchor)
line_start = content.find("\n", idx)
line_end = content.find("\n", line_start + 1)
# append at end of K-Z3 table row (line containing anchor)
content = content[:line_end] + " " + evidence + content[line_end:]

log = (
    "- 2026-09-06: bench 第80回。10:34 JST tick。worktree detached HEAD のため fetch net-kotobase + "
    "rev-parse 比較で取り込み (HEAD 6b66fb3 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。"
    "rank 第79回 (09:55, NEXT「委ねる」, K-Z3 fallback) と falsify 第80回 (run203A–C, 10時台 2セット目) "
    "を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 70.28 (gate 7.5 超過, "
    "tick 内 101.02 まで悪化) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): "
    "K-Z3 10時台 3セット目 run204A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 10:35–10:42 JST, "
    "全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold 0/0/0 per 20 = 0/60, "
    "search p50 196–302ms は host load 高騰 (~100) tick の全体的上振れで landing control (kotobase.net/signup) "
    "p50 241ms も同程度 — borderline not-separated だが cold(>=0.5s) は 0/60 (閾値超過 0 件) で run202/203 型 "
    "単発突発は本 tick では非再現。10時台通算 5/180 (~2.8%) 低位帯。※本 tick 初回試行は urllib ベース harness "
    "で 403 60/60 (UA block) の無効測定 — 別接続 curl の従来手順で再実施し本記録は curl 分のみ採用 "
    "(要 rank 判定: urllib 404/403 無効測定の production 実測数不算入は run200 前例に従う)。"
    "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
    "フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
)
anchor2 = "## Iteration log\n"
i2 = content.find(anchor2) + len(anchor2)
content = content[:i2] + log + content[i2:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("appended")

import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

ev = (
    " bench 2026-09-06 (第79回, K-Z3 10時台帯初計測 run202A–C, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, Tokyo, 10:01:42–10:02:34 JST, 全 80/80 200, host load1 11.83 (gate 7.5 超過) は "
    "production HTTP 実測のため gate 外): run202A cold(>=0.5s) 4/20 (0.858–1.038s, 13番目中心の単発集中) "
    "p50 49ms / run202B cold 0/20 p50 39ms / run202C cold 0/20 p50 39ms — landing control "
    "(kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 52ms max 259ms と静穏で control 分離成立、"
    "cold 群は search 側に局在。10時台は帯初計測で cold 4/60 (~6.7%) — run201 (1/60) に続き 9–10時台で "
    "cold>0 が 2 セット連続、ただし 202A 群は帯内 1 窓即消失 (B/C 0/20)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

lines = text.split("\n")
# K-Z3 hypothesis row is line index 206; evidence paragraph lines (208-232) sit between
# the header row and the closing "|". Append evidence to the last evidence line (232)
# which ends with " status 判定は rank に委ねる (rank 専門)。 |"
target = None
for i in range(206, 236):
    if lines[i].rstrip().endswith("|"):
        target = i
        break
assert target is not None, "closing pipe line not found"
ln = lines[target].rstrip("\n")
lines[target] = ln[:-1] + ev + " |"

log_entry = (
    "- 2026-09-06: bench 第79回。10:01 JST tick。worktree detached HEAD (3cb9292) のため fetch net-kotobase "
    "+ rev-parse 比較で取り込み (fetch rc 0, HEAD 3cb9292 = fetch 後 net-kotobase/main 先端一致, ancestor rc 0, "
    "乖離 0)。falsify 第78回 (run201A–C, run200/201 誤 URL 404 無効測定注記) と bench 第78回 (run201A–C), "
    "rank 第78回 (NEXT は K-Z3 9時台 n 積み増し) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。"
    "host load1 11.83 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): "
    "K-Z3 10時台帯初計測 run202A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 10:01:42–10:02:34 JST, "
    "全 80/80 200, 正 endpoint search.kotobase.net/search?q=test 使用で誤 URL 404 は回避): "
    "cold 4/0/0 per 20 = 4/60 (~6.7%, 0.858–1.038s, run202A 13番目中心の単発集中クラスタ), "
    "warm p50 39–49ms は静穏帯水準, control (kotobase.net/signup) cold 0/20 p50 52ms max 259ms 静穏で "
    "control 分離成立 — run201A 型帯内 1 窓即消失パターン (B/C 0/20) で、9時台に続き 2 時間帯連続の "
    "単発集中型突発。深夜帯 ~26-31% 平坦パターンとの対比は K-Z3 traffic 依存説と整合するが、"
    "10時台は日中 traffic 上昇帯であり K-Z3 本来の「日中帯突発」予測にも整合。status 遷移なし (rank 専門)。"
    "secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"
)

text = "\n".join(lines)

marker = "## Iteration log\n"
idx = text.index(marker)
head = text[: idx + len(marker)]
tail = text[idx + len(marker):]
stripped_tail = tail.lstrip("\n")
nl_count = len(tail) - len(stripped_tail)
text = head + "\n" * nl_count + log_entry + "\n" + stripped_tail

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK appended to line", target, "len", len(text))

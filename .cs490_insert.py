#!/usr/bin/env python3
# cosientist: insert run490 (independent 18時台 n-add; run489 taken by bench 213)
# Inserts one iter-log line at top of Iteration log, appends evidence to K-Z3 row tail.
import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Locate iteration-log header.
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        ilog_idx = i
        break
if ilog_idx is None:
    sys.exit("ITERLOG_HEADER_NOT_FOUND")

# Next non-blank line after header is the top entry (expected bench 第213回 run489).
first_entry = None
j = ilog_idx + 1
while j < len(lines) and lines[j].strip() == "":
    j += 1
if j < len(lines):
    first_entry = lines[j]

new_line = (
    "- 2026-09-08: cosientist 第146回。18:12 JST tick。run488/489 は sibling 使用済みのため run490 に読替 (independent 18時台 n-add)。"
    "HEAD bf18472 = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル経由)。"
    "K-Z3 18時台 run490A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:12 窓 t0 18:11:31 JST, 全 80/80 200, host load1 42.27-57.88 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 3/0/3 per 20 = 6/60 (~10.0%) - run490A 3/20 (1.2076/1.5819/1.7001s) B 0/20 C 3/20 (0.5148/0.6980/0.7167s), landing control cold 1/20 (1.2771s) で control 分離 borderline not-separated 傾向 (search cold 6/60 は閾値決定的 0.51-1.70s だが control にも 1.28s が 1 件 + host load ~42-58 high tick の p50 上振れ込み). "
    "18時台 (80:9/8) 本測 cold 6/60 は bench run489 (7/60) と同窓の独立 2 セットで 18時台通算 (bench run489 7/60 + 本測 6/60) = 13/120 (~10.8%) の日中帯高位継続, traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変. status 判定は rank 専門. secret は一切記録せず. NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run491)"
)

# Insert after ilog_idx+1 (若 blank line is present, insert into a を blank line slot).
out = []
header_done = False
for k in range(len(lines)):
    out.append(lines[k])
    if k == ilog_idx:
        # find and then insert after the first entry line
        out.append(new_line)
# simpler: splice at ilog_idx+1
lines2 = lines[:]
lines2.insert(ilog_idx + 1, new_line)

text = "\n".join(lines2)
with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(text)
print("INSERTED_ITERLOG")
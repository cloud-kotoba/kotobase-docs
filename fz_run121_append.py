import re

path = "query-cosientist.md"
with open(path) as f:
    lines = f.readlines()

EV = ("falsify 2026-09-05 (K-Z3 8時台 n 積み増し run121A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 08:47 JST, 全 60/60 + control 20/20 200, host load1 104.6 "
      "は production HTTP 実測のため gate 外。※ rank 第41回 NEXT は 9時台だが cron 実行時刻が "
      "08時台のため帯逸脱 — run105/run116/run120 前例に従い 8時台として記録): "
      "run121A cold(>=0.5s) 0/20 p50 0.103s / run121B cold 0/20 p50 0.103s / "
      "run121C cold 0/20 p50 0.080s — landing control (kotobase.net/, 同時刻, n=20, 全 200) "
      "は cold 0/20 p50 0.199s と静穏で control 分離成立。8時台通算は run119A–C + run120A–C + "
      "本 tick で 0/180 完全静穏 — 朝帯 8時台の低位が 3 セット連続で再現し "
      "5時台/6時台/8時台のみ低位という帯別分布の裾を支持。status 判定は rank に委ねる (rank 専門)。 ")

# K-Z3 hypothesis row: | K-Z3 | worker | hypothesis | status | evidence |
target = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        target = i
        break
assert target is not None, "K-Z3 row not found"

row = lines[target]
parts = row.split("|")
# cells: '', ' K-Z3 ', ' worker ', ' <hypothesis> ', ' <status> ', ' <evidence> ', ' ...', '\n'
assert parts[1].strip() == "K-Z3" and parts[2].strip() == "worker"
# find the 'open' status cell among the first cells
st_idx = None
for j in range(3, min(6, len(parts))):
    if parts[j].strip() == "open":
        st_idx = j
        break
assert st_idx is not None, "open status cell not found"
ev_idx = st_idx + 1
assert parts[ev_idx].strip(), "evidence cell empty?"

# IMPORTANT: evidence field keeps newest at TOP? Existing convention: newest entries
# are appended... previous ticks prepended their new entry right after status (see
# run119/120 entries appearing first in the cell). We prepend the new evidence
# directly at the start of the evidence cell to match run120 tick behavior.
parts[ev_idx] = " " + EV + parts[ev_idx].lstrip()
lines[target] = "|".join(parts)

with open(path, "w") as f:
    f.writelines(lines)

print("appended into evidence cell idx", ev_idx, "at line", target + 1)
cells = lines[target].split("|")
for j, c in enumerate(cells[:8]):
    print(j, "=>", c.strip()[:60])

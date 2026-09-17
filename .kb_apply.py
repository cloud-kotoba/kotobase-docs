import sys

p = "query-cosientist.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

# scrub zero-width chars from our payload defensively
def scrub(s):
    return s.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").replace("\ufeff", "")

EVID = scrub(" falsify 第226回 (2026-09-08, K-Z3 22時台 n 積み増し run509A-C, run508 帯初直後の 2 セット目, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 22:19:14-22:19:28 JST, 全 80/80 200, host load1 16.28 (pre-run 計測, gate 7.5 超過) は production HTTP 実測のため gate 外): run509A cold(>=0.5s) 1/20 (1.5981s 9番目単発) p50 0.1213s / run509B cold 0/20 p50 0.1152s / run509C cold 0/20 p50 0.0915s — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 0.1015s max 0.1894s と完全静穏で control 分離成立、cold 群は search 側に単発 1 件局在。22時台通算 = run508 (7/60 ~11.7%) + run509 (1/60) = 8/120 (~6.7%) — run508 の 7/60 cold 多発は即時非再現で帯水準非持続の 1 窓寄りが続く。22時台 ~6.7% は 21時台 (~10.8%) より低く 20時台 (~5.0%) 級に戻り、深夜帯 ~4.4-31% 平坦パターンへの判別は 23時台 到達後の追加 n が材料。status 判定は rank に委ねる (rank 専門)。")

ILOG = scrub("- 2026-09-08: falsify 第226回。22:19 JST tick。K-Z3 22時台 n 積み増し run509 (run508 帯初直後の 2 セット目; NEXT 23時台委ねる は現在時刻 22:15 で到達不可 → 22時台で実施・帯区分は rank 判定に委ねる, 前回 cosientist 第39回前例): 全 80/80 200, cold 1/60 ~1.7% (A 9番目単発 1.598s, B/C 0/20), control 0/20 完全静穏分離成立。22時台通算 8/120 ~6.7% で run508 の 7/60 多発は即時非再現・帯水準非持続。HEAD 1d0d78f = remote net-kotobase/main 一致。")

# find K-Z3 row index (single physical line starting with | K-Z3 |)
kz3 = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        kz3 = i
        break
assert kz3 is not None, "K-Z3 row not found"

# append to K-Z3 line END (before trailing newline)
# verify current END anchor
anchor_repr = repr(lines[kz3][-60:])
has_end = lines[kz3].rstrip("\n").endswith("rank 専門)。")
sys.stdout.write("kz3_line=%d len=%d has_end=%r\n" % (kz3 + 1, len(lines[kz3]), has_end))
sys.stdout.write("anchor: %s\n" % anchor_repr)
if not has_end:
    sys.stdout.write("ABORT: K-Z3 END anchor mismatch\n")
    sys.exit(2)

# find iter log header
il = None
for i, l in enumerate(lines):
    if l.strip().startswith("## Iteration log"):
        il = i
        break
assert il is not None, "iter log header not found"

newlines = list(lines)
newlines[kz3] = newlines[kz3].rstrip("\n") + EVID + "\n"

# insert iter log entry as the newest (line right after header)
prefix = newlines[il + 1:]  # existing entries after header
new_entry = "- " + ILOG + "\n"
newlines = newlines[: il + 1] + [new_entry] + newlines[il + 1:]

with open(p, "w", encoding="utf-8") as f:
    f.writelines(newlines)

sys.stdout.write("INSERTED OK\n")
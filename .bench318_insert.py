#!/usr/bin/env python3
import io
path = "query-cosientist.md"
data = io.open(path, encoding="utf-8").read()
lines = data.splitlines(keepends=True)

# --- 1. append evidence to end of K-Z3 row (line 279) ---
kz3_idx = None
for idx, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3_idx = idx
        break
assert kz3_idx is not None, "K-Z3 row not found"

ev = (
 " bench 2026-09-07 (第132回, K-Z3 6時台(深夜帯→朝の帯境) n-add run318A\u2013C \u2014 falsify 第146回 run317 "
 "(06:16) に続く 6時台 n-add (次 run ID run318), 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, "
 "Tokyo, 06:23:28\u201306:24:02 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
 "host load1 74.36\u2192111.87 (06:22/06:24 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate "
 "外, secret 不含 \u2014 curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 \u2014 run318A cold 0/20 p50 110.6ms "
 "max 207.1ms / run318B cold 0/20 p50 115.4ms max 190.3ms / run318C cold 0/20 p50 98.1ms max 222.8ms, "
 "control (kotobase.net/signup) cold 0/20 p50 104.3ms max 256.0ms 完全静穏で control 分離成立 (search/control "
 "とも 0 cold)。run318 全 0/60 完全静穏で 6時台の完全静穏 0/60 は falsify 第146回 run317 に続く連続再静穏で "
 "run283/289/293/296/297/298/303/307/309/312/313/314/317 型の **14 例目** (散発単発=即消失の性質を 14 例目で "
 "支持, heavy run271A 6/20 型は run271A 以降 43 セット連続非再現)。\u203b本 tick は host load 高騰 "
 "(74\u2192112) で search/control の p50 (98\u2013115ms) が静穏基準 (~40\u201350ms) から約 2 倍上振れだが max 256ms "
 "未満で cold 閾値 0.5s に達せず 0/60 判定に影響なし (borderline note)。6時台通算 = falsify run315 (2/60) + "
 "bench run316 (1/60) + falsify run317 (0/60) + 本 tick run318 (0/60) = 3/240 (~1.25%) の 4 セット、"
 "deep-night 累計 run275..318 = 43/2640 (~1.63%) の 44 セットで低位帯水準継続 \u2014 深夜帯\u2192朝の帯境 (6時台) "
 "での完全静穏 連続 (run317\u2192run318) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと "
 "整合方向, deep-night 累計 ~1.63% の低位帯残界が 44 セットで安定)。status 判定は rank に委ねる (rank 専門)。"
 "secret は一切記録せず。\n"
)
# remove original newline, append ev (which ends with newline)
lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + ev

io.open(path, "w", encoding="utf-8").write("".join(lines))
print("ev appended to K-Z3 row line", kz3_idx + 1)

# --- re-read to confirm only one line (no accidental split) ---
data2 = io.open(path, encoding="utf-8").read()
lines2 = data2.splitlines(keepends=True)
k = [i for i, l in enumerate(lines2) if l.startswith("| K-Z3 | worker |")][0]
print("K-Z3 row now len=", len(lines2[k]), "ends:", repr(lines2[k][-80:]))
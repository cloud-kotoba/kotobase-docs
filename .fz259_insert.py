# falsify 259th: append evidence to K-Z3 row end + insert iter-log entry at top
import sys
p = "query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")

EV = (" falsify 2026-09-09 (第259回, K-Z3 23時台帯初計測 (9/9) run574A-C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:28:21–23:28:45 JST, 全 80/80 200, host load1 32.32 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 9/60 (~15.0%) — run574A cold 7/20 (1.16–2.50s 短時間クラスタ, max 2.5049s) p50 134.2ms / run574B cold 1/20 (2.2244s 単発) p50 67.6ms / run574C cold 1/20 (1.2341s 単発) p50 57.3ms, control (kotobase.net/signup) cold 0/20 p50 94.3ms max 497.8ms 完全静穏で control 分離成立。23時台 (9/9) 帯初 ~15.0% は 9/4-5 深夜帯実績 (~29–32%) に次ぐ高位方向で K-Z3 traffic 依存説の深夜帯高位を支持 (n=1 セットのため帯水準確定には追加 n 要)。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)。")

# locate K-Z3 row (single physical line starting '| K-Z3 |')
kz = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 |")]
assert len(kz) == 1, f"K-Z3 rows: {kz}"
assert lines[kz[0]].endswith("|") or True
lines[kz[0]] = lines[kz[0]] + EV

IL = ("- 2026-09-09: falsify 第259回 (23:23 JST tick)。HEAD 34b9caa = rank 第257回 (23:02) = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch + rev-parse 比較で取り込み, 乖離 0)。rank 第257回 NEXT「K-Z3 19時台 n 積み増し」は 19時台待機不可能 (現 23時台) のためフォールバック (現時刻帯) で K-Z3 23時台帯初計測 (9/9) run574A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:28:21–23:28:45 JST, 全 80/80 200): cold(>=0.5s) 9/60 (~15.0%) — run574A cold 7/20 (1.16–2.50s 短時間クラスタ, max 2.5049s) p50 134.2ms / run574B cold 1/20 (2.2244s 単発) p50 67.6ms / run574C cold 1/20 (1.2341s 単発) p50 57.3ms, control (kotobase.net/signup) cold 0/20 p50 94.3ms max 497.8ms 完全静穏で control 分離成立。23時台 (9/9) 帯初 ~15.0% は 9/4-5 深夜帯実績 (~29–32%) に次ぐ高位方向で K-Z3 traffic 依存説の深夜帯高位を支持 (n=1 セットのため帯水準確定には追加 n 要)。host load1 32.32 (gate 7.5 超過) は production HTTP 実測のため gate 外。K-Q1 (cacao_b64 harness) は host load gate 超過のため本 tick も実施せず, 次の低負荷 tick 待ち。evidence は K-Z3 仮説行 (L279 末尾) に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 23時台 n 積み増し, 次 run ID run575)。secret は一切記録せず (curl + python3 stats のみ)。")

hdr = [i for i, l in enumerate(lines) if l.strip() == "## Iteration log"]
assert len(hdr) == 1, f"hdr: {hdr}"
lines.insert(hdr[0] + 1, IL)

# scrub combining chars
def scrub(s):
    return "".join(c for c in s if not (0x0300 <= ord(c) <= 0x036F))
lines = [scrub(l) for l in lines]

open(p, "w", encoding="utf-8").write("\n".join(lines))
# verify
txt = open(p, encoding="utf-8").read()
print("run574 count:", txt.count("run574"))
print("falsify 第259回 count:", txt.count("falsify 第259回"))
print("K-Z3 rows:", sum(1 for l in txt.split("\n") if l.startswith("| K-Z3 |")))
print("hdr count:", txt.count("## Iteration log"))

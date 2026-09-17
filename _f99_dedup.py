import io

path = 'query-cosientist.md'
with io.open(path, encoding='utf-8') as f:
    text = f.read()

# The evidence block was inserted twice (adjacent duplicate lines separated by blank line).
block1 = "falsify 2026-09-06 (第99回, K-Z3 17時台 n 積み増し run228A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 17:38:49–17:39:28 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 153.51 (17:33 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 — rank 第94/95回 NEXT「K-Z3 18時台 n 積み増し」は 18時台だが cron 実行時刻 17:35 が17時台のため 17時台待機不可能、falsify 第88回/96回 precedent に従い 現在時刻帯 17時台 n 積み増しで実施): cold(>=0.5s) 1/1/1 per 20 = 3/60 (~5.0%) — run228A 単発 1.082s (3番目) p50 143.2ms / run228B 単発 1.115s (1番目) p50 192.6ms / run228C 単発 0.918s (19番目) p50 86.7ms, control (kotobase.net/signup) cold 0/20 p50 93.4ms max 293.7ms 静穏で control 分離成立、cold 群は search 側に局在。※本 tick 全体の p50 (86.7–192.6ms) は host load 153 の高騰 tick の全体的上振れで warm 群自身の遅延上振れを伴うが cold 3 件 (0.918–1.115s) は閾値決定的で cold 濃度判定 3/60 に影響なし (borderline note)。run228A/B/C 各独立に単発 1 件 (run222A/223A/225A/B 型「帯内 1 窓即消失」単発の 3 run 各期化) — 17時台通算 (bench run226 3/60 + falsify run226 0/60 + 本 tick 3/60) 6/180 (~3.3%) の低位帯を維持、run226A 散発 3 件 (bench) は 38 分後も別位置単発で弱く非連続再現。日中低温帯分布パターン維持で traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。"

# Find the duplicate sequence: block \n\n block  ... take first occurrence
dupe = block1 + "\n\n" + block1
assert text.count(dupe) == 1, f"dupe count = {text.count(dupe)}"
text = text.replace(dupe, block1, 1)

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print("DEDUP_OK")
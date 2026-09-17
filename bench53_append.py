import io

path = 'query-cosientist.md'
lines = open(path, encoding='utf-8').read().splitlines(keepends=True)

new = ("bench 2026-09-05 (第53回, K-Z3 18時台 n 積み増し run161A–C, rank 第53回 NEXT「委ねる」フォールバック, "
       "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 18:46:40–18:46:49 JST, 全 80/80 200, "
       "host load1 50.77 は production HTTP 実測のため gate 外): run161A cold(>=0.5s) 1/20 (1.017s, 単発) p50 0.056s / "
       "run161B cold 0/20 p50 0.040s / run161C cold 0/20 p50 0.050s — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
       "cold 0/20 p50 0.049s (max 0.318s) と静穏で control 分離成立、cold 群は search 側に局在。"
       "run158 型の search/landing 同時全体遅延窓は本 tick では非再現 (18:01/18:35 の 2 窓から 18:46 は静穏へ復帰)。"
       "18時台通算は run159 (1/60) + run160 (2/60) + 本 tick で 180 試行中 4 試行 (~2.2%) の低位帯。"
       "status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先)。\n")

# insert after line 219 (1-indexed), i.e. index 219, before line 220 (blank sep kept)
lines.insert(219, '\n')
lines.insert(220, new)
open(path, 'w', encoding='utf-8').writelines(lines)
print('inserted after line 219')

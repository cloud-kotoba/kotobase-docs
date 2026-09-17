path = 'query-cosientist.md'
text = open(path, encoding='utf-8').read()

old_e = ("bench 2026-09-05 (第53回, K-Z3 18時台 n 積み増し run161A–C, rank 第53回 NEXT「委ねる」フォールバック, "
         "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 18:46:40–18:46:49 JST, 全 80/80 200, "
         "host load1 50.77 は production HTTP 実測のため gate 外): run161A cold(>=0.5s) 1/20 (1.017s, 単発) p50 0.056s / "
         "run161B cold 0/20 p50 0.040s / run161C cold 0/20 p50 0.050s — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
         "cold 0/20 p50 0.049s (max 0.318s) と静穏で control 分離成立、cold 群は search 側に局在。"
         "run158 型の search/landing 同時全体遅延窓は本 tick では非再現 (18:01/18:35 の 2 窗から 18:46 は静穏へ復帰)。"
         "18時台通算は run159 (1/60) + run160 (2/60) + 本 tick で 180 試行中 4 試行 (~2.2%) の低位帯。"
         "status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先)。")
# tolerant match: build with possible variant 窓/窗
if old_e not in text:
    import re
    m = re.search(r'bench 2026-09-05 \(第53回.*?NEXT: 委ねる \(rank 指定優先\)。', text, re.S)
    assert m, 'evidence line not found'
    old_e = m.group(0)
new_e = old_e + "※ run ID run161 は falsify 第59回 (18:48 JST, 別インスタンス同時実行) と重複 — 本計測 (18:46) と falsify 分 (18:48) は 同一時間帯の独立 2 計測であり, ID 衝突の読み替え可否は rank 判定に委ねる (run105/run123/run124 前例に従う)。"

assert old_e in text
text = text.replace(old_e, new_e, 1)

old_log = "search cold 1/60 (~1.7%, 1.02s 単発), p50 40–56ms, landing control cold 0/20 p50 0.049s と静穏で control 分離成立 — run158 型全体遅延窓は 18:46 では非再現 (18:01/18:35 の 2 窓から静穏へ復帰)。18時台通算 4/180 ~2.2% 低位帯 — status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先)。"
assert old_log in text
new_log = ("search cold 1/60 (~1.7%, 1.02s 単発), p50 40–56ms, landing control cold 0/20 p50 0.049s と静穏で control 分離成立 — "
           "run158 型全体遅延窓は 18:46 では非再現 (18:01/18:35 の 2 窓から静穏へ復帰)。18時台通算 4/180 ~2.2% 低位帯。"
           "※ falsify 第59回 (18:48, 同時刻別インスタンス) と run161 ID 重複 — 両者は独立 2 計測, 読み替え可否は rank 判定に委ねる "
           "(run123/run124 前例)。status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先)。")
text = text.replace(old_log, new_log, 1)

open(path, 'w', encoding='utf-8').write(text)
print('collision notes added')

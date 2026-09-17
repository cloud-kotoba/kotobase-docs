import io
path = 'query-cosientist.md'
with io.open(path, encoding='utf-8') as f:
    lines = f.readlines()
new_ev = (" bench 2026-09-06 (第71回, K-Z3 6時台 n 積み増し run191A–C, 同測定法 n=20 × 3 + landing control, "
          "別接続 curl, Tokyo, 06:54–06:58 JST, 全 80/80 200, host load1 68.72 は production HTTP 実測のため gate 外): "
          "run191A cold(>=0.5s) 1/20 (1.037s, 9番目の単発) p50 50ms (max 1037ms) / run191B cold 0/20 p50 47ms / "
          "run191C cold 0/20 p50 48ms (max 112ms) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
          "cold 0/20 p50 59ms (max 200ms) と静穏で control 分離成立。cold 1/60 は run100A/116A/159B/188A 型の薄い単発型。"
          "status 判定は rank に委ねる (rank 専門)。")
lines[206] = lines[206].rstrip('\n') + new_ev + '\n'
with io.open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('appended to line 207')

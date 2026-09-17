import re

path = 'query-cosientist.md'
text = open(path, encoding='utf-8').read()

ev = (" bench 2026-09-06 (第81回, K-Z3 11時台帯初計測 run206A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 11:31:57–11:32:21 JST, 全 80/80 200, host load1 15–22 (gate 7.5 超過) は "
      "production HTTP 実測のため gate 外): run206A cold(>=0.5s) 3/20 (0.967s/0.997s/1.137s, 1–3番目 "
      "冒頭集中クラスタ) p50 42ms / run206B cold 1/20 (0.917s, 17番目の単発) p50 41ms / run206C cold 0/20 "
      "p50 38ms — 合計 4/60, landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 "
      "p50 49ms max 233ms と静穏で control 分離成立、cold 群は search 側に局在。run206A 冒頭クラスタは "
      "即消失 (B 単発→C 0) の帯内 1 窓型 (run178A/run201A/run202A 型)。11時台は帯初計測で cold 4/60 "
      "(~6.7%) — 12時台 (~8.3%) に近い日中低位帯の初期サンプル。status 判定は rank に委ねる (rank 専門)。")

lines = text.split('\n')
hit = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        hit = i
        break
if hit is None:
    raise SystemExit('K-Z3 row not found')
row = lines[hit]
print('row tail repr:', repr(row[-60:]))
# append evidence at end of the line (before trailing pipes if any)
if row.rstrip().endswith('|'):
    lines[hit] = row.rstrip()[:-1].rstrip() + ev + ' |'
else:
    lines[hit] = row.rstrip() + ev

log = ("- 2026-09-06: bench 第81回。11:26 JST tick。worktree detached HEAD (5ccd827) のため fetch "
       "net-kotobase + rev-parse 比較で取り込み (HEAD 5ccd827 = fetch 後 net-kotobase/main 先端一致, "
       "乖離 0)。falsify 第82回 (run205A–C) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。"
       "host load1 15–22 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, "
       "gate 外): K-Z3 11時台帯初計測 run206A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, "
       "11:31:57–11:32:21 JST, 全 80/80 200): cold 3/1/0 per 20 = 4/60 (run206A 冒頭集中クラスタ "
       "0.967–1.137s 3件 + run206B 0.917s 単発), warm p50 38–42ms 静穏帯水準, control (kotobase.net/signup) "
       "cold 0/20 p50 49ms max 233ms 静穏で control 分離成立 — run206A クラスタは即消失 (C 0/20) の帯内 1 窓型。"
       "11時台は帯初計測で 4/60 (~6.7%) の日中低位帯寄り初期サンプル (12時台 ~8.3% に近い)。"
       "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
       "フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。")

text = '\n'.join(lines).rstrip('\n') + '\n\n' + log + '\n'
open(path, 'w', encoding='utf-8').write(text)
print('done')

import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

with io.open(src, encoding='utf-8') as f:
    t = f.read()

# --- 1. evidence append to K-Z3 row (insert before next row "| K-S1 |") ---
ev = (" falsify 2026-09-06 (第85回, 未登録分の追記, K-Z3 13時台 run211A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 13:44 JST 前後, 全 80/80 200, host load1 5.94): run211A cold(>=0.5s) 4/20 "
      "(0.876–1.071s 冒頭集中クラスタ) p50 48.8ms / run211B cold 1/20 (1.444s 単発) p50 42.6ms / run211C cold 0/20 "
      "p50 43.6ms — control (kotobase.net/signup) cold 0/20 p50 50.0ms で control 分離成立。13時台 2セット目: "
      "13時台通算 run210+run211 = 11/120 (~9.2%)。 falsify 2026-09-06 (第86回, K-Z3 14時台帯初計測 run212A–C, "
      "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 14:06:31–14:07:00 JST, 全 80/80 200, "
      "host load1 55.33 (急上昇 tick) は production HTTP 実測のため gate 外): run212A cold(>=0.5s) 4/20 "
      "(0.842–1.146s 冒頭集中クラスタ) p50 64.3ms / run212B cold 0/20 p50 66.6ms / run212C cold 0/20 p50 61.5ms — "
      "control (kotobase.net/signup) cold 0/20 p50 121.9ms max 213.9ms で cold 0 だが p50 全体的上振れ気味 "
      "(host load 急上昇混入可能性) borderline 注記付き。run212A 冒頭集中は run202A/207A/209A/210A/211A 型 "
      "「帯内 1 窓即消失」パターンと整合。14時台は帯初サンプル 4/60 (~6.7%)。status 判定は rank に委ねる (rank 専門)。")

anchor = '\n| K-S1 |'
i = t.find(anchor)
assert i > 0, 'K-S1 anchor not found'
# safety: ensure K-Z3 row is before it
assert t.rfind('| K-Z3 |', 0, i) > 0
t = t[:i] + ev + t[i:]

# --- 2. iteration log entry after rank 第85回 line ---
lines = t.split('\n')
idx = None
for n, l in enumerate(lines):
    if l.startswith('- 2026-09-06: rank 第85回。'):
        idx = n
assert idx is not None, 'rank 85 log line not found'

log = ("- 2026-09-06: falsify 第86回。14:10 JST tick。HEAD 1a3a4c1 = fetch 後 net-kotobase/main 先端一致 "
       "(ancestor rc 0, 乖離 0)。NEXT「K-Z3 13時台 n 積み増し」だったが実行時刻が 14時台に入ったため 14時台帯初計測 "
       "run212A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 14:06:31–14:07:00 JST, 全 80/80 200, "
       "host load1 55.33 急上昇 tick は production HTTP 実測のため gate 外): cold 4/0/0 per 20 = 4/60 (~6.7%) — "
       "run212A 冒頭集中クラスタ 0.842–1.146s 4件は即消失の帯内 1 窓型, warm p50 61–67ms, control cold 0/20 "
       "p50 121.9ms (p50 上振れ borderline 注記付き)。併せて前 tick 第85回に evidence 未登録のまま残っていた "
       "run211A–C (13:44 JST, 13時台 2セット目, cold 5/60, run211A 冒頭集中 0.876–1.071s 4件 + B 単発 1.444s, "
       "control 分離成立, host load1 5.94) を K-Z3 evidence 欄に追記 (13時台通算 run210+run211 = 11/120 ~9.2%)。"
       "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
       "フォールバックは K-Z3 14時台 n 積み増し継続)。")
lines.insert(idx + 1, log)
t = '\n'.join(lines)

with io.open(src, 'w', encoding='utf-8') as f:
    f.write(t)

# verify
with io.open(src, encoding='utf-8') as f:
    t2 = f.read()
with io.open('/tmp/_f86_verify.txt', 'w', encoding='utf-8') as f:
    f.write('run211 count: %d\n' % t2.count('run211A'))
    f.write('run212 count: %d\n' % t2.count('run212A'))
    f.write('log86 present: %s\n' % ('falsify 第86回' in t2))
    f.write('len delta: %d\n' % (len(t2) - len(t)))

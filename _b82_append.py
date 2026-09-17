# Append bench iteration 82 log line + run207 evidence to query-cosientist.md K-Z3 row, commit & push.
import subprocess, json

with open('_b82_evidence.txt', encoding='utf-8') as f:
    ev = f.read().strip()

with open('query-cosientist.md', encoding='utf-8') as f:
    text = f.read()

anchor = "11時台は帯初計測で cold 4/60 (~6.7%) — 12時台 (~8.3%) に近い日中低位帯の初期サンプル。status 判定は rank に委ねる (rank 専門)。"
assert text.count(anchor) == 1, text.count(anchor)
text = text.replace(anchor, anchor + " " + ev)
with open('query-cosientist.md', 'w', encoding='utf-8') as f:
    f.write(text)

log = ("- 2026-09-06: bench 第82回。12:07 JST tick。worktree detached HEAD (3d21316) のため fetch net-kotobase + rev-parse 比較で取り込み "
       "(HEAD 3d21316 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。falsify 第82回 (run205A–C)・rank 第82回 を取り込み済み確認。"
       "live smoke 200 (/, /signup; pre-run 計測)。host load1 7.2–7.8 (gate 7.5 境界超過) のため local 測定は拒否。"
       "フォールバック (production HTTP 実測, gate 外): K-Z3 12時台帯初計測 run207A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, "
       "12:08:48–12:09:20 JST, 全 80/80 200): cold 0/60 (0%) — run207A/B/C いずれも cold 0, warm p50 53–55ms max 106ms の静穏帯水準, "
       "control (kotobase.net/signup) cold 0/20 p50 49ms max 107ms で control 分離成立。12時台は 11時台初計測 4/60 (~6.7%) より低い 0/60 で、"
       "日中低位帯パターン (7時台 ~2.2% < 9-10時台 ~3-5% < 11時台 ~6.7% ≒ 12時台 0% 初サンプル) と整合。"
       "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n")

with open('query-cosientist.md', 'a', encoding='utf-8') as f:
    f.write(log)

def run(*a):
    p = subprocess.run(a, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()

print('add', run('git','add','query-cosientist.md'))
print('commit', run('git','commit','-m','bench 第82回: K-Z3 12時台帯初計測 run207A-C cold 0/60, warm p50 53-55ms, control 分離成立'))
print('push', run('git','push','net-kotobase','HEAD:net-kotobase/main'))
print('head', run('git','rev-parse','HEAD'))

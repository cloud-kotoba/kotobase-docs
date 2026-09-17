import io, subprocess

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=docs, capture_output=True, text=True)
    return (p.stdout or '') + (p.stderr or '')

log = []
log.append(sh('git rev-parse HEAD').strip())
log.append(sh('git rev-parse net-kotobase/main').strip())

with io.open(src, encoding='utf-8') as f:
    t = f.read()
log.append('run212=%d' % t.count('run212'))

if t.count('run212') == 0:
    ev = (" falsify 2026-09-06 (第86回, K-Z3 14時台帯初計測 run212A–C, 同測定法 n=20 × 3 + landing control, "
          "別接続 curl, Tokyo, 14:06:31–14:07:00 JST, 全 80/80 200, host load1 55.33 (急上昇 tick) は "
          "production HTTP 実測のため gate 外): run212A cold(>=0.5s) 4/20 (0.842–1.146s 冒頭集中クラスタ) "
          "p50 64.3ms / run212B cold 0/20 p50 66.6ms / run212C cold 0/20 p50 61.5ms — control "
          "(kotobase.net/signup) cold 0/20 p50 121.9ms max 213.9ms で cold 0 だが p50 全体的上振れ気味 "
          "(host load 急上昇混入可能性) borderline 注記付き。run212A 冒頭集中は run202A/207A/209A/210A 型 "
          "「帯内 1 窓即消失」パターンと整合。14時台は帯初サンプル 4/60 (~6.7%)。status 判定は rank に委ねる "
          "(rank 専門)。")
    anchor = '\n| K-S1 |'
    i = t.find(anchor)
    assert i > 0 and t.rfind('| K-Z3 |', 0, i) > 0, 'anchor missing'
    t = t[:i] + ev + t[i:]
    lines = t.split('\n')
    idx = None
    import re
    for n, l in enumerate(lines):
        if re.match(r'^- 2026-09-06: rank 第86', l) or re.match(r'^- 2026-09-06: falsify 第86', l):
            idx = n
    if idx is None:
        for n, l in enumerate(lines):
            if re.match(r'^- 2026-09-06: rank 第8', l):
                idx = n
    assert idx is not None, 'log anchor missing'
    log86 = ("- 2026-09-06: falsify 第86回。14:10 JST tick。rank 第86回と同時刻帯。NEXT「K-Z3 13時台 n 積み増し」"
             "だったが実行時刻が 14時台に入ったため 14時台帯初計測 run212A–C (同測定法 n=20 × 3 + landing control, "
             "別接続 curl, 14:06:31–14:07:00 JST, 全 80/80 200, host load1 55.33 急上昇 tick は production HTTP "
             "実測のため gate 外): cold 4/0/0 per 20 = 4/60 (~6.7%) — run212A 冒頭集中クラスタ 0.842–1.146s 4件は "
             "即消失の帯内 1 窓型, warm p50 61–67ms, control cold 0/20 p50 121.9ms (p50 上振れ borderline 注記付き)。"
             "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
             "フォールバックは K-Z3 14時台 n 積み増し継続)。")
    lines.insert(idx + 1, log86)
    with io.open(src, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    log.append('edits applied')

with io.open(src, encoding='utf-8') as f:
    t2 = f.read()
log.append('VERIFY run212=%d log86=%s' % (t2.count('run212'), ('falsify 第86回' in t2)))

with io.open(docs + '_f86_sync2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log) + '\n')

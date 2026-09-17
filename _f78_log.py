path = 'query-cosientist.md'
text = open(path, encoding='utf-8').read()
entry = ('- 2026-09-06: falsify 第78回。09:23 JST tick。worktree detached HEAD (032b37b) のため fetch net-kotobase + '
         'rev-parse 比較で取り込み (HEAD 032b37b = fetch 後 net-kotobase/main 先端一致, ancestor rc 0, 乖離 0)。'
         'falsify 第77回 (run198/run200) と bench 第77回 (run199A–C) を取り込み済み確認。live smoke 200 (/, /signup)。'
         'host load1 14–15 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): '
         'K-Z3 9時台帯初計測 run201A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 09:28:42–09:29:03 JST, '
         '全 80/80 200): cold 1/0/0 per 20 = 1/60 (0.987s 単発, run201A 6番目), warm p50 44–47ms 静穏帯水準, '
         'control (kotobase.net/signup) cold 0/20 p50 58ms max 117ms 静穏で control 分離成立 — 9時台は低位帯寄りの初期サンプル。'
         '※本 tick 内 2 試行は誤 URL (kotobase.net/search → 404 60/60) のため無効とし正 endpoint '
         'search.kotobase.net/search?q=test で再実施。前 tick run200 も 404 60/60 の無効測定の可能性大 (要 rank 判定)。'
         'status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; '
         'フォールバックは K-Z3 9時台 n 積み増し継続)。')
marker = '## Iteration log'
i = text.find(marker)
if i < 0:
    raise SystemExit('marker missing')
insert_at = i + len(marker)
text = text[:insert_at] + '\n\n' + entry + text[insert_at:]
open(path, 'w', encoding='utf-8').write(text)
print('log appended, new size:', len(text))
print('evidence occurrences:', text.count('第78回, K-Z3 9時台帯初計測'))

import io
NL = '\n'
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
anchor = '## Iteration log' + NL + '- 2026-09-06: rank 第97回。18:02'
assert s.count(anchor) == 1, 'anchor cnt=%d' % s.count(anchor)
ent = ('## Iteration log' + NL +
       '- 2026-09-06: falsify 第100回。18:01 JST tick。worktree detached HEAD のため fetch '
       'net-kotobase + rev-parse で同期確認 (HEAD 852e64a = fetch 後 net-kotobase/main 先端一致, '
       '乖離 0)。rank 第97回 (18:02, commit 852e64a, NEXT「K-Z3 18時台 n 積み増し」, 17時台 '
       '10/240 確定) を取込み確認。※本 tick 冒頭で worktree に bench 第94回 run229 の未コミット '
       '編集を確認したが、その後の rank 第97回 fetch で bench の commit (12fc865) と rank '
       '第97回 commit (852e64a) が共に push 済みであることを log で確認 — bench データは commit '
       '済みのため二重記録せず。live smoke 200 (/, /signup; pre-run 計測)。host load1 74.77 '
       '(18:00 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否。フォールバック (production '
       'HTTP 実測, gate 外): K-Z3 18時台 n 積み増し run230A–C (同測定法 n=20 × 3 + landing '
       'control, 別接続 curl, 18:03:14–18:03:59 JST, 全 80/80 200, 正 endpoint '
       'search.kotobase.net/search?q=test): cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) — '
       'run230B 単発 0.917s のみ / A・C 0/20, control (kotobase.net/signup) cold 1/20 (0.618s '
       '境界値) p50 234ms max 618ms — host load 高騰 (74.77) tick で search/control とも p50 '
       '全体的上振れ + control に cold 1 件が出現し control 分離は borderline not-separated '
       '(search 側 cold 1/60 は閾値決定的)。run230B 単発は「帯内 1 窓即消失」パターン継続、'
       '18時台先サンプルは 17時台 (10/240 ~4.2%) と同水準の低温帯候補だが control 分離が弱く帯判定'
       '確定には追加 n 要。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。'
       'NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し継続)。' + NL)
new = s.replace(anchor, ent, 1)
io.open(p, 'w', encoding='utf-8').write(new)
print('log cnt=%d replaced' % s.count(anchor))
import io
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
anchor = '## Iteration log\n- 2026-09-06: bench 第94回。17:57'
assert s.count(anchor) == 1, 'anchor count=%d' % s.count(anchor)
ent = ('## Iteration log\n'
       '- 2026-09-06: falsify 第100回。18:01 JST tick。worktree detached HEAD のため fetch '
       'net-kotobase + rev-parse で同期確認 (HEAD 952c8b7 = fetch 後 net-kotobase/main 先端一致, '
       '乖離 0)。※ worktree に bench 第94回 (17:57, run229, 17時台 4/60) の未コミット編集が '
       '残留していた (同一 worktree 共有・bench の commit が切れた) ためデータ喪失を避け本 tick の '
       'commit に同梱する。rank 第96回 (17:49, NEXT「K-Z3 18時台 n 積み増し」) を取込み確認。'
       'live smoke 200 (/, /signup; pre-run)。host load1 74.77 (gate 7.5 大幅超過) のため local '
       '測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 18時台 n 積み増し '
       'run230A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 18:03:14–18:03:59 JST, '
       '全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 0/1/0 per 20 '
       '= 1/60 (~1.7%) — run230B 単発 0.917s のみ / A・C 0/20, control (kotobase.net/signup) '
       'cold 1/20 (0.618s 境界値) p50 234ms max 618ms で host load 高騰 (74.77) tick の p50 '
       '全体的上振れ + control breakthrough により control 分離 borderline not-separated (search '
       '側 cold 1/60 は閾値決定的)。run230B 単発は「帯内 1 窓即消失」パターン継続、18時台先 '
       'サンプルは 17時台 (10/240 ~4.2%) と同水準の低温帯候補だが control 分離が弱く帯判定確定に '
       'は追加 n 要。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる '
       '(rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し継続)。\n')
new = s.replace(anchor, ent, 1)
io.open(p, 'w', encoding='utf-8').write(new)
print('log anchor cnt=%d replaced' % s.count(anchor))
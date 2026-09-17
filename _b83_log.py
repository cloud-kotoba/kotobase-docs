p = 'query-cosientist.md'
s = open(p).read()
entry = "- 2026-09-06: bench 第83回。13:09 JST tick。worktree detached HEAD (7a3ad0b) のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 7a3ad0b = fetch 後 net-kotobase/main 先端一致, ancestor rc 0, 乖離 0)。falsify 第84回 (run209A–C, 12時台 2セット目) を取り込み済み確認。live smoke 200 (/, /signup; pre-run 計測)。host load1 6.49–7.06 (gate 7.5 未満まで低下) だが tick 時間帯の都合で local 測定候補なし (NEXT「委ねる」) のためフォールバック (production HTTP 実測, gate 外): K-Z3 13時台帯初計測 run210A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 13:13:21–13:13:47 JST, 全 80/80 200): cold 4/1/1 per 20 = 6/60 (~10%) — run210A 冒頭集中クラスタ 0.829–1.057s 4件 + B/C 単発各 1 (1.017s/1.812s), warm p50 36–48ms は静穏帯水準, control (kotobase.net/signup) cold 0/20 p50 52.5ms max 64.3ms で control 分離成立。run210A 冒頭集中は run202A/207A/209A 型「帯内 1 窓即消失」パターンと整合。13時台は 12時台通算 7/120 (~5.8%) と同水準の低位帯寄り初期サンプル (falsify run37–48 の 13時台昼帯後半とは別日同時刻帯 — 採用判定は rank に委ねる)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
anchor = "- 2026-09-06: rank 第83回。12:17 JST tick。worktree (branch pr588, /tmp/hyakka worktree)"
idx = s.rfind(anchor)
if idx < 0:
    open('_b83_log_out.txt', 'w').write('NO_ANCHOR\n')
else:
    s = s[:idx] + entry + s[idx:]
    open(p, 'w').write(s)
    open('_b83_log_out.txt', 'w').write('OK\n')

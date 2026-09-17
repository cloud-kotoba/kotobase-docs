import re
path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
src = open(path).read()
# 1) K-Z3 evidence: insert falsify 第76回 before " | open | falsify 2026-09-05 (K-Z3 18時台 control 付き追加 n run161A–C"
ev = ('falsify 2026-09-06 (第76回, K-Z3 8時台 2セット目 run196A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 08:18–08:20 JST, 全 80/80 200, '
      'host load1 59–214 (高負荷 tick) は production HTTP 実測のため gate 外): run196A cold(>=0.5s) 0/20 p50 197ms max 340ms / run196B cold 1/20 (0.507s 境界値の単発) p50 262ms / '
      'run196C cold 0/20 p50 191ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 169ms max 270ms と静穏だが search p50 全体的に control 上振れ気味で '
      'host load 高騰 (~59→214) の混入可能性あり borderline 注記付き。cold 1/60 単発 (0.507s は閾値ぎりぎり) で run195 (1/60) と同型, 8時台通算 run195+run196 で 2/120 (~1.7%) 低位帯。'
      'status 判定は rank に委ねる (rank 専門)。')
anchor = ' | open | falsify 2026-09-05 (K-Z3 18時台 control 付き追加 n run161A–C'
assert src.count(anchor) == 1, f'anchor count {src.count(anchor)}'
src = src.replace(anchor, ' ' + ev + anchor)
# 2) iteration log append
log = ('- 2026-09-06: falsify 第76回。08:15 JST tick。worktree detached HEAD (9795b1e) のため rev-parse 比較で取り込み (9795b1e = bench 第74回 push 後の net-kotobase/main 先端一致)。'
       'falsify 第75回 (run195A–C) と bench 第74回 (run194A–C) を取り込み済み確認 — rank 第75回 log に「run196A–C 未 commit 生出力」注記ありのため本 tick 分は run196 として正式記録 (生出力は本 tick 測定 _f76_run196_out.txt, 08:18–08:20 JST)。'
       'live smoke 200 (/, /signup; pre-run 計測)。host load1 42–59 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): '
       'K-Z3 8時台 2セット目 run196A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 08:18–08:20 JST, 全 80/80 200): cold 0/1/0 per 20 = 1/60 (0.507s 閾値ぎりぎりの単発, B), '
       'warm p50 191–262ms, control cold 0/20 p50 169ms max 270ms 静穏だが search 全体上振れ気味で host load 高騰混入の borderline 注記付き。run195 (1/60) と同型で 8時台通算 2/120 (~1.7%) 低位帯。'
       'status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 8時台 n 積み増し継続)。')
src = src.rstrip('\n') + '\n' + log + '\n'
open(path, 'w').write(src)
print('done')

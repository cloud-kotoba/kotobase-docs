import subprocess, sys, time

MD = 'query-cosientist.md'
sys.path.insert(0, '.')
txt = open(MD, encoding='utf-8').read()
hdr = '## Iteration log\n'
assert txt.count(hdr) == 1, 'HDR_COUNT != 1'
assert 'rank 第242回' not in txt

now = time.strftime('%H:%M')
entry = (
"- 2026-09-09: rank 第242回。10:41 JST tick。HEAD 5049e7e = falsify 第242回 (10:33, K-Z3 10時台帯初計測 run545 cold 6/60) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, worktree diff HEAD -- query-cosientist.md 空 (pre-run の M は 5049e7e 未取込時代の stale worktree state, checkout -- で解消後 空確認) + HDR_COUNT=1 事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第247回 NEXT フォールバック「K-Z3 現時刻帯 n 積み増し続行, 次 run ID は run545 使用」)。rank 第241回 re-insert (5f1826d, 10:15) 以降の新規確定 evidence は 1 commit のみ: falsify 第242回 run545 (10:30 commit, 10:33 計測, K-Z3 10時台 (9/9) 帯初計測): cold(>=0.5s) 6/60 (~10.0%) (A3+B2+C1, max 1.5669s), control landing 0/20 完全静穏分離成立, 全 80/80 200, host load1 ~99 (gate 外の production HTTP 実測)。取り込み判定: (a) K-Z3: run545 を 10時台帯初として登録、10時台 (9/9) 通算 = 6/60 (~10.0%) の 1 セット — 9時台 7 セット 9/420 ~2.1% の朝帯静穏低位帯から 10時台 (日中帯) 帯初で ~10.0% へ明確な上振れ移行、K-Z3 仮説の元来の対象帯 (10:41-11:47 突発パターン再発窓) に入り日中帯高帯方向の支持材料だが帯 n=1 で帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専任のまま)。9/8 16-17時台 ~8.3-10.0% 中〜高位帯・9/9 9時台 ~2.1% との対比で日中帯 traffic 依存方向に整合。(b) K-Q1: 変動なし — transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank 測定指示対象外, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence なし — K-Z3 は open 継続・10時台帯初 n=1 で帯水準確定・機構判断とも未達; K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 10時台帯初 ~10.0% は日中帯高帯方向だが n=1 で優先度逆転なし)。live smoke 200 (/, /signup; pre-run monitor 計測)。host load1 93.03 (10:33 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。NEXT: K-Z3 10時台 (現時刻帯・帯初 ~10.0% の帯水準確定と日中帯 traffic 依存説検証のため n 積み増し) 継続, 次 run ID は run546 使用 (run545 は falsify 第242回が消費済みのため)。\n"
)

idx = txt.index(hdr)
new = txt[:idx] + hdr + entry + txt[idx+len(hdr):]
open(MD, 'w', encoding='utf-8').write(new)

# verify worktree
chk = open(MD, encoding='utf-8').read()
assert chk.count(hdr) == 1
assert 'rank 第242回' in chk
assert chk.index('rank 第242回') < chk.index('falsify 第242回: K-Z3')

r = subprocess.run(['git', 'add', MD], capture_output=True, text=True)
open('/tmp/rk242_gadd.txt', 'w').write(str(r.returncode) + r.stderr)
# verify STAGED content before commit
r2 = subprocess.run(['git', 'show', ':query-cosientist.md'], capture_output=True, text=True)
staged = r2.stdout
open('/tmp/rk242_staged_chk.txt', 'w').write('hdr=%d rank242=%d first_ok=%s\n' % (
    staged.count(hdr), staged.count('rank 第242回'),
    staged.find('rank 第242回') < staged.find('falsify 第242回: K-Z3')))
if staged.count('rank 第242回') != 1 or staged.count(hdr) != 1:
    open('/tmp/rk242_abort.txt', 'w').write('ABORT: staged content missing rank242 entry\n')
    sys.exit(1)
r3 = subprocess.run(['git', 'commit', '-m', 'rank 第242回: fold falsify242 run545 (10hr帯初 6/60 ~10.0%), no status transition, NEXT K-Z3 10時台 run546'], capture_output=True, text=True)
open('/tmp/rk242_commit.txt', 'w').write(r3.stdout + r3.stderr)

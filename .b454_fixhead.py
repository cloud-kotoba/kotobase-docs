import io
MD='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(MD, encoding='utf-8') as f:
    text = f.read()

old = ("- 2026-09-08: bench 第202回。10:41 JST tick。HEAD 653e162 = falsify 第203回 "
"(10:34, K-Z3 10時台 n-add run453 cold 5/60 ~8.3% control borderline) = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込, "
"terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。")

new = ("- 2026-09-08: bench 第202回。10:41 JST tick。測定開始時 HEAD 653e162 = falsify 第203回 "
"(10:34, K-Z3 10時台 n-add run453 cold 5/60 ~8.3% control borderline) = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込, "
"terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由。※本 tick 作業中に sibling "
"rank 第200回 commit 2e6bb77 (10:36 fold run450-453, NEXT run454) が push 着弾 — commit は 2e6bb77 上に実施、"
"rank 第200回 NEXT「K-Z3 10hr n-add run454」と本測 run454 は一致)。")

assert old in text, 'anchor not found'
text = text.replace(old, new)
with io.open(MD, 'w', encoding='utf-8') as f:
    f.write(text)
with io.open('/tmp/bk_fixhead.txt','w',encoding='utf-8') as f:
    f.write('ok\n')
print('fixed')
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
log = '- 2026-09-06: falsify 第73回。07:31 JST tick。worktree detached HEAD のため fetch net-kotobase で取り込み確認 (HEAD 24eb7de = fetch 後 net-kotobase/main 先端一致)。rank 第70回 の未コミット iteration log 行は rank 記入の完成行のため保持して取込。host load1 49–124 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 7時台 2セット目 run193A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 07:39–07:40 JST, 全 80/80 200): cold 3/0/0 per 20 = 3/60 (888/934/955ms, A 群のみで分散型薄クラスタ), warm p50 156–181ms, control cold 0/20 p50 174ms 静穏で control 分離成立 — run192 (1/60) に続き 7時台 2セット連続で cold>0 は深夜低位帯 (~0-2%) の上限寄り (~3.3%) を示し, 群発型 (run186A 9/20) ではなく薄クラスタ型。host load 高騰 tick だが control が静穏で search 側局在は維持。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 7時台 n 積み増し継続)。\n'
with open('query-cosientist.md', 'r') as f:
    text = f.read()
anchor = '## Iteration log\n'
i = text.index(anchor) + len(anchor)
new = text[:i] + log + text[i:]
with open('query-cosientist.md', 'w') as f:
    f.write(new)
print('log inserted:', '- 2026-09-06: falsify 第73回' in new)

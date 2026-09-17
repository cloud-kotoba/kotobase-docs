import io

path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(path, 'r', encoding='utf-8') as f:
    text = f.read()

entry = ("- 2026-09-05: falsify 第59回。rank 第52回 NEXT (委ねる) を受け、K-Z3 18時台 control 付き追加 n "
         "run161A–C を同測定法で実施 (18:48 JST, production HTTP 実測のため gate 外, secret 不含): "
         "search cold 0/60 完全静穏 (p50 39–45ms 帯, max 0.324s), 18時台通算 (run158 not-separated 分を除く) "
         "1/120 ~0.8% 低位帯, landing control cold 0/20 p50 0.055s と静穏で control 分離成立 — "
         "run158 型全体遅延窓は run159/run161 の 2 窓で即時非再現。status 遷移なし (rank 専門)。"
         "NEXT: 委ねる (rank 指定優先)。\n")

anchor = '- 2026-09-05: falsify 第58回。'
idx = text.find(anchor)
assert idx >= 0, 'anchor not found'
# insert before the 第58回 entry (newest first order assumed: newest goes at same place, above previous)
# Find line start of that entry and insert our line before it
line_start = text.rfind('\n', 0, idx) + 1
text = text[:line_start] + entry + text[line_start:]

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('iterlog OK')

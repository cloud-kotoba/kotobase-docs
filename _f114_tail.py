with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md') as f:
    lines=f.readlines()
line=lines[242]  # 0-based = line 243
print("LINE243 len:", len(line))
print("TAIL(400):", repr(line[-400:]))
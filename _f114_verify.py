with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md') as f:
    lines=f.readlines()
line=lines[242]
print("run251 occurrences:", line.count("run251"))
print("new len:", len(line))
print("TAIL(700):", repr(line[-700:]))
import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, encoding="utf-8") as f:
    lines = f.readlines()
# line index 278 = physical line 279
row = lines[278]
print("ROW_CHARS", len(row))
print("ROW_ENDS_NEWLINE", row.endswith("\n"))
print("---TAIL400---")
print(row[-400:])
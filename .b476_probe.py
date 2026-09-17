import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
c = io.open(path, encoding="utf-8").read()
m = "| K-Z3 | worker |"
s = c.find(m)
print("start", s)
nxt = c.find("\n|", s + len(m))
print("next_row", nxt)
print("around:", repr(c[nxt - 2:nxt + 15]))
# also find end of the row: look for the closing pipe then newline not followed by '|'
i = s
depth = 0
# just report the char at next_row position
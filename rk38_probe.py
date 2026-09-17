import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(P, encoding="utf-8").read()
i = s.find("86 試行中 29 試行")
while i >= 0:
    print("=== at", i, "===")
    print(repr(s[max(0,i-260):i+160]))
    print()
    i = s.find("86 試行中 29 試行", i+1)

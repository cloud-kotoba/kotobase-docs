import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
n125 = src.count("run125A")
log_tail = src[-400:]
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_diag.txt", "w") as f:
    f.write("run125A count: %d\n---tail---\n%s\n" % (n125, log_tail))
print("done")

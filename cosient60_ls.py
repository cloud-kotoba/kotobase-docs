import os, glob
print(sorted(glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cosient60*")))
p = "/private/tmp/cosient60_run173_out.txt"
print("tmp exists:", os.path.exists(p))
if os.path.exists(p):
    print(open(p).read())

import os, sys
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
print("exists", os.path.exists(p))
try:
    print("stat", os.stat(p))
except OSError as e:
    print("stat_err", repr(e))
d = os.path.dirname(p)
print("dir_exists", os.path.exists(d))
print("dir_listable", os.path.isdir(d))
try:
    names = os.listdir(d)
    print("sample_names", [n for n in names if "query" in n or n.endswith(".md")][:10])
except OSError as e:
    print("listdir_err", repr(e))
print("getcwd", os.getcwd())
print("realpath", os.path.realpath(p))
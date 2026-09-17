import glob, re
# find route table: search for "q" handler dispatch in worker.cljs or surface
for f in glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/**/*.cljs", recursive=True):
    s = open(f).read()
    for m in re.finditer(r'xrpc/ai|datomic|"/q"|handle-q', s):
        print(f.split("engine/")[1], m.start(), m.group(0))

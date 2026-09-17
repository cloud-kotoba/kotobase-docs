import os

root = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
lines = []
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
    for name in filenames:
        lines.append(os.path.relpath(os.path.join(dirpath, name), root))
with open("bench_ls.txt", "w") as f:
    f.write("\n".join(sorted(lines)) + "\n")
print(len(lines))

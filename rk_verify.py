import io, subprocess, sys

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

# 1. fetch + rev-compare
r_fetch = sh("cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git fetch bench_fetch")
rem = sh("cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git rev-parse bench_fetch/main")
head = sh("cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git rev-parse HEAD")
print("remote=%s head=%s match=%s" % (rem.stdout.strip(), head.stdout.strip(), rem.stdout.strip()==head.stdout.strip()))

# 2. committed blob inspection (python, not grep — long utf-8 lines)
blob = sh("cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git show HEAD:query-cosientist.md")
wt = blob.stdout
hdr = "## Iteration log"
print("header_count=%d" % wt.count(hdr))
idx = wt.index(hdr) + len(hdr) + 1  # skip header + newline
rest = wt[idx:]
print("first_entry_rank239=%s" % rest.startswith("- 2026-09-09: rank 第239回。"))
print("has_falsify239=%s has_bench245=%s has_bench244=%s has_rank238=%s" % (
    ("falsify 第239回" in wt), ("bench 第245回" in wt), ("bench 第244回" in wt), ("rank 第238回" in wt)))

# 3. worktree clean
d = sh("cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git diff --quiet -- query-cosientist.md && echo CLEAN || echo DIRTY")
print("worktree_diff=%s" % d.stdout.strip())
print("VERIFY_DONE")
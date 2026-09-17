import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:js/kotobase-graph-database-worker.js"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
# is the artifact a stale build? check for a recent known feature e.g. read budget refusal (bc51f61) markers
for pat in ["read budget", "GraphTooLargeToHydrate", "revocation", "pack", "missing-read-capability"]:
    print(pat, s.count(pat))
# also check minified name mangling: summary may be mangled; search "l1=" string concat
print("l1= occurrences:", s.count("l1="))
print(";l2 occurrences:", s.count(";l2"))

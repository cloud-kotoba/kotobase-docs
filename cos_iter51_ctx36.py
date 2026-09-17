import re, glob
# find the apex worker: search monorepo for KOTOBA_BACKEND_URL
import os
base = "/Users/junkawasaki/github/com-junkawasaki"
hits = []
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in (".git", "node_modules", ".cpcache", "target", "vendor")]
    if root.count(os.sep) - base.count(os.sep) > 6:
        continue
    for fn in files:
        if fn.endswith((".ts", ".js", ".mjs", ".toml", ".jsonc")) and ("wrangler" in fn or "worker" in fn.lower() or fn in ("index.ts","main.ts")):
            p = os.path.join(root, fn)
            try:
                s = open(p, encoding="utf8", errors="ignore").read()
            except Exception:
                continue
            if "KOTOBA_BACKEND_URL" in s:
                hits.append(p)
                print(p)

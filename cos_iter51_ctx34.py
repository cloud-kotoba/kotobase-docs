import re
# Find the kotobase.net frontend/edge worker repo: search orgs for a worker that routes xrpc to backend
import glob
for f in glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/*/wrangler*.json*") + glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/*/src/**/wrangler*", recursive=True):
    print(f)

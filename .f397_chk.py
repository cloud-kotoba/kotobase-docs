import re
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(fn,encoding="utf-8").read()
# does falsify 第174 or run397 exist as measurement?
for pat in ["falsify 第174回","run397A","run397B","run397C"]:
    print(pat, data.count(pat))
# iterate log entries newest first: show last 6 lines matching "- 2026-09-07:"
parts=[ln for ln in data.split("\n") if ln.startswith("- 2026-09-07:") or ln.startswith("- 2026-09-07") or "- 2026-09-07:" in ln]
for ln in parts[-6:]:
    print("ILOG:", ln[:120])
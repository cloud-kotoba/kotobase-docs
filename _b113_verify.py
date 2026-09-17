#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
print("chars:", len(src))
print("run278A-C evidence present:", src.count("run278A–C"))
print("run278B present:", "run278B cold 0/20" in src)
print("bench113 iter log present:", "bench 第113回。01:26" in src)
print("iter log line count starts with bench113:", src.count("- 2026-09-07: bench 第113回"))
# show top of iter log
i = src.find("## Iteration log")
print("==== iter log top ====")
print(src[i:i+400])
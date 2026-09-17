import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
line = lines[281]
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_tail.txt", "w", encoding="utf-8") as f:
    f.write(f"L282 len={len(line)}\nTAIL: {line[-300:]}\n")
    # find last K-Z3 hypothesis table row end and the '## Iteration log' header line number
    for i, l in enumerate(lines, 1):
        if l.startswith("## Iteration log"):
            f.write(f"iterlog_header_line={i}\n")
    # check for existing run595 usage
    cnt = sum(1 for l in lines if "run595" in l)
    f.write(f"run595_mentions={cnt}\n")
    cnt596 = sum(1 for l in lines if "run596" in l)
    f.write(f"run596_mentions={cnt596}\n")
    # count commits of same-frame duplicates
    cnt557 = sum(1 for l in lines if "run557" in l and "cold" in l)
    f.write(f"run557_evidence_lines={cnt557}\n")
print("ok")

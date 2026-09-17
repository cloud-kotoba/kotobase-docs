#!/usr/bin/env python3
# parse .b478_{A,B,C,landing}.raw (each line "code ttfb") into separate .code and .ttfb
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b478"
for k in ["A", "B", "C", "landing"]:
    codes, ttfbs = [], []
    with open(base + "_" + k + ".raw", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            parts = s.split()
            if len(parts) == 2:
                codes.append(parts[0])
                ttfbs.append(parts[1])
    with open(base + "_" + k + ".code", "w", encoding="utf-8") as f:
        f.write("\n".join(codes) + "\n")
    with open(base + "_" + k + ".ttfb", "w", encoding="utf-8") as f:
        f.write("\n".join(ttfbs) + "\n")
print("parsed ok")
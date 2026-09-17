import re

text = open("query-cosientist.md", encoding="utf-8").read()
nums = sorted(int(n) for n in re.findall(r"bench 第(\d+)回", text))
runs = sorted(set(int(m) for m in re.findall(r"run(\d+)[A-Z]?", text)))
with open("kz3_run103_verify.txt", "w", encoding="utf-8") as f:
    f.write("bench max run number: %s\n" % (nums[-3:] if nums else "none"))
    f.write("run ids present (max 15): %s\n" % runs[-15:])
    f.write("run103 mention: %s\n" % ("run103" in text))
    f.write("run104 mention: %s\n" % ("run104" in text))
print("ok")

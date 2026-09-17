import os
s = open("bench42_kz3.py").read()
print(repr([l for l in s.splitlines() if "COLD" in l or "colds" in l][:4]))
print("out mtime", os.stat("bench42_out.txt").st_mtime, "py mtime", os.stat("bench42_kz3.py").st_mtime)

import re
src = open("bench40_kz3.py").read()
src = src.replace("bench40_out.txt", "bench41_out.txt")
src = src.replace("run115A", "run117A").replace("run115B", "run117B").replace("run115C", "run117C")
open("bench41_kz3.py", "w").write(src)
print("written")

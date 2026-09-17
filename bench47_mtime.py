import os, datetime
for f in ["bench47_out.json", "bench47_z3.py"]:
    st = os.stat(f)
    print(f, datetime.datetime.fromtimestamp(st.st_mtime).astimezone().isoformat())

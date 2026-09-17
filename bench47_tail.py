with open("query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
# find the K-Z3 table row line (starts with '| K-Z3 ')
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 "):
        with open("bench47_kz3_tail.txt", "w", encoding="utf-8") as out:
            out.write(f"LINE {i+1} len {len(ln)}\n")
            out.write("TAIL>>>" + ln[-600:] + "<<<TAIL\n")
        print("found", i+1)
        break

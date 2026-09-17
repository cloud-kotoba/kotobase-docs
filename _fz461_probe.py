import io, sys
fn = "query-cosientist.md"
data = open(fn, "rb").read()
print("filesize", len(data))

# locate ## Iteration log header
hdr = b"## Iteration log\n"
hidx = data.find(hdr)
print("iter_hdr_idx", hidx, "found" if hidx >= 0 else "MISSING")

# locate the K-Z3 hypothesis-table row: a line that STARTS with the row marker
# Search for the row in the hypothesis population section (starts with "| K-Z3 |")
marker = b"| K-Z3 | worker | K-Z1/K-Z2"
ridx = data.find(marker)
print("kz3_row_start", ridx, "found" if ridx >= 0 else "MISSING")

# find end of that physical line (next \n after ridx)
row_end = data.find(b"\n", ridx)
print("kz3_row_end_newline", row_end)

# count occurrences of the row marker to ensure uniqueness
print("marker_count", data.count(marker))
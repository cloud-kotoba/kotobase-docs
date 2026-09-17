import io
fn = "query-cosientist.md"
d = open(fn, "rb").read()
hdr = b"## Iteration log\n"
hidx = d.find(hdr)
print("=== first 3 lines after Iteration log header ===")
print(d[hidx:hidx+700].decode("utf-8", "replace"))
print("=== K-Z3 row tail (last 500 bytes before its newline) ===")
marker = b"| K-Z3 | worker | K-Z1/K-Z2"
ridx = d.find(marker)
R = d.find(b"\n", ridx)
print(d[R-500:R].decode("utf-8", "replace"))
# double-insert sanity: ensure no duplicated iter entry text
print("iter_dup_check", d.count(b"falsify "))
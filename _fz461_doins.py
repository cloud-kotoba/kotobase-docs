import io

fn = "query-cosientist.md"
base = open(fn, "rb").read()

def scrub(b):
    # remove zero-width chars (U+200B..U+200D)
    return b.replace(b"\xe2\x80\x8b", b"").replace(b"\xe2\x80\x8c", b"").replace(b"\xe2\x80\x8d", b"")

ev_raw = open("_fz461_ev.txt", "rb").read()
iter_raw = open("_fz461_iter.txt", "rb").read()
ev = scrub(b" " + ev_raw.strip())
it = scrub(iter_raw.strip())

# ---- locate anchors on BASE (pre-insert offsets) ----
hdr = b"## Iteration log\n"
hidx = base.find(hdr)
assert hidx >= 0, "iter header not found"
H = hidx + len(hdr)  # insert iter right after header newline

marker = b"| K-Z3 | worker | K-Z1/K-Z2"
ridx = base.find(marker)
assert ridx >= 0, "kz3 row not found"
R = base.find(b"\n", ridx)  # newline ending the K-Z3 physical row
assert R > ridx, "row end not found"

print("H", H, "R", R, "len(ev)", len(ev), "len(iter)", len(it))

# ---- insert HIGHER offset first, then LOWER (both measured from base) ----
# H (iter header, ~543k) > R (row end, ~406k)
assert H > R, "expected H>R"
out = base[:H] + it + b"\n" + base[H:]
out = out[:R] + ev + out[R:]

open(fn, "wb").write(out)
print("wrote", len(out), "expected", len(base)+len(ev)+len(it)+1)

# verify single occurrence of markers (ASCII-only byte patterns)
d = open(fn, "rb").read()
print("ev_occurrence", d.count(b"1.1789s / 2.0231s"))
print("iter_occurrence", d.count(b"falsify 207"))
print("iter_tick_occurrence", d.count(b"run461A"))
print("iter_hdr_count", d.count(hdr))
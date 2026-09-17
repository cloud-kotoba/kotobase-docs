import io

fn = "query-cosientist.md"
base = open(fn, "rb").read()

def scrub(b):
    return b.replace(b"\xe2\x80\x8b", b"").replace(b"\xe2\x80\x8c", b"").replace(b"\xe2\x80\x8d", b"")

ev_raw = open("_bench205_run462_ev.txt", "rb").read()
iter_raw = open("_bench205_run462_iter.txt", "rb").read()
ev = scrub(b" " + ev_raw.strip())
it = scrub(iter_raw.strip() + b"\n")

hdr = b"## Iteration log\n"
hidx = base.find(hdr)
assert hidx >= 0, "iter header not found"
H = hidx + len(hdr)

marker = b"| K-Z3 | worker | K-Z1/K-Z2"
ridx = base.find(marker)
assert ridx >= 0, "kz3 row not found"
R = base.find(b"\n", ridx)
assert R > ridx, "row end not found"

print("H", H, "R", R, "len(ev)", len(ev), "len(iter)", len(it))

assert H > R, "expected H>R"
out = base[:H] + it + base[H:]
out = out[:R] + ev + out[R:]

open(fn, "wb").write(out)
print("wrote", len(out), "expected", len(base)+len(ev)+len(it))

d = open(fn, "rb").read()
print("ev_occurrence", d.count(b"1.430s/1.686s/1.101s"))
print("iter_occurrence", d.count(b"bench 205"))
print("iter_tick_occurrence", d.count(b"run462A"))
print("iter_hdr_count", d.count(hdr))
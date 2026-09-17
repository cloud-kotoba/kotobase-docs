import io, sys, traceback

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []
try:
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    out.append("len=%d" % len(text))
    print("\n".join(out))
except Exception:
    traceback.print_exc()

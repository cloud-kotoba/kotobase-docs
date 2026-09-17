import io
p = ".b431_runner.py"
s = io.open(p, encoding="utf-8").read()
new = '    return {"tag": tag, "n": n, "rc0": rc0, "cold": cold, "p50": round(nearest_rank_p50(lat,4)), "max": round(max(lat,4), "all_200": rc0==n}\n'
old = '    return {"tag": tag,'
start = s.index(old)
nl = s.index("\n", start)
s = s[:start] + new + s[nl+1:]
io.open(p, "w", encoding="utf-8").write(s)
print("REPLACED")

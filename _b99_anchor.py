path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(path).read().splitlines()
# Line 243 is the huge K-Z3 evidence cell. Show where run244/run245/第111回 sit within it.
ln = lines[242]  # 0-based index 242 = line 243
print("line243 length:", len(ln))
for key in ["run244", "run245", "第111回", "run233"]:
    idx = ln.find(key)
    print(f"  '{key}' at {idx}")
# tail of line 243
print("TAIL line243 (last 800 ch):")
print(ln[-800:])
print("\n== line 244 start ==")
print(lines[243][:200])
print("\n== line 283 tail ==")
print(lines[282][-400:])
print("\n== line 284 ==")
print(repr(lines[283][:60]))
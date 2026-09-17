lines = open("query-cosientist.md").read().splitlines()
target = lines[205]
# find insertion point: K-Z3 evidence starts after "| open | " and ends before " | open |"? Actually row ends with "|"
print(repr(target[:200]))
print("---")
print(repr(target[-300:]))

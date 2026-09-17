lines = open("query-cosientist.md", encoding="utf-8").read().split("\n")
for i in (279, 280, 281, 282, 283):
    print(i+1, lines[i][:120])
    print("   END:", lines[i][-100:])

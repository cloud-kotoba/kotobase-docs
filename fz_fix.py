path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    text = f.read()
text = text.replace("falsify 第247回 (19:27 JST tick)", "falsify 第248回 (19:27 JST tick)")
with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("occ:", text.count("falsify 第248回 (19:27 JST tick)"))

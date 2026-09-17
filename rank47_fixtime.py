import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

old = "13時台は falsify 第51回 run151A–C (13時台帯初計測, 13:0x JST, cold 4/60 ~6.7%"
new = "13時台は falsify 第51回 run151A–C (13時台帯初計測, 13時台帯 commit 13:35 JST, cold 4/60 ~6.7%"
assert text.count(old) == 1
text = text.replace(old, new)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK")

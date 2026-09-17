p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f192_insert.py"
s=open(p,encoding="utf-8").read()
old=".write(news\nprint"
new=".write(news)\nprint"
if old in s:
    s=s.replace(old,new,1)
    open(p,"w",encoding="utf-8").write(s)
    print("patched")
else:
    print("no-match")
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f192_insert.py"
s=open(p,encoding="utf-8").read()
needle=".write(news\n"
if s.endswith(needle):
    s=s[:len(s)-len(needle)]+".write(news)\n"
    open(p,"w",encoding="utf-8").write(s)
    print("patched")
else:
    print("no-match tail:"+repr(s[-80:]))
src = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b355_stats.py"
dst = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f192_run434_stats.py"
s = open(src, encoding="utf-8").read()
s = s.replace(".b355_", ".f192_run434_")
s = s.replace("'355'", "'434'")
s = s.replace("355c", "434c")
s = s.replace("355{", "434{")
s = s.replace("'355", "'434")
open(dst, "w", encoding="utf-8").write(s)
import ast
ast.parse(s)
print("OK")
#!/usr/bin/env python3
src = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_bench_run376.py"
dst = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b195_run441.py"
s = open(src, encoding="utf-8").read()
s = s.replace("run376", "run441")
s = s.replace("bench_run376_result.json", "bench_b195_run441_result.json")
s = s.replace("17時台(9/7) n-add run441A-C — bench 第165回", "8時台(9/8) n-add run441A-C — bench 第195回 (run440 taken by falsify 第195回 -> relabel run441)")
open(dst, "w", encoding="utf-8").write(s)
import ast
ast.parse(s)
print("SYNTAX OK, wrote", dst)
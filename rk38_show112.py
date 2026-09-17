# f5c423f (falsify run112A-C) の内容と本 tick の取り込み状況を確認する。
import subprocess

DOCS = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "show", "f5c423f", "--stat"],
                   capture_output=True, text=True, cwd=DOCS)
print(r.stdout[:800], r.stderr[:200])
r2 = subprocess.run(["git", "show", "f5c423f", "--format=%aI", "-s"],
                    capture_output=True, text=True, cwd=DOCS)
print("commit date:", r2.stdout.strip())
s = open(DOCS + "/query-cosientist.md", encoding="utf-8").read()
print("run112A-C in file:", "run112A" in s)
print("run112A count:", s.count("run112"))
i = s.find("run112A")
print(s[max(0,i-300):i+500] if i >= 0 else "(not found)")

import subprocess

r = subprocess.run(["git", "pull", "--ff-only"], capture_output=True, text=True)
print("pull:", (r.stdout or r.stderr).strip())

path = "query-cosientist.md"
content = open(path, encoding="utf-8").read()

old = "K-Z3 21時台 n 積み増し run170A–C — rank NEXT"
new = "K-Z3 21時台 n 積み増し run171A–C (※ run170 は cosientist 第58回 20時台 run169 の ID 衝突読み替え分と重複 — run167/168 前例に従い本分を run171 として記録) — rank NEXT"
assert content.count(old) == 1, content.count(old)
content = content.replace(old, new)

for a, b in (("run170A cold(>=0.5s) 2/20", "run171A cold(>=0.5s) 2/20"),
             ("/ run170B cold 0/20", "/ run171B cold 0/20"),
             ("/ run170C cold 0/20", "/ run171C cold 0/20"),
             ("run170A は run100A/104A 型", "run171A は run100A/104A 型")):
    assert content.count(a) == 1, (a, content.count(a))
    content = content.replace(a, b)

open(path, "w", encoding="utf-8").write(content)

# report residual run170 occurrences inside my entry only
seg = content.split("bench 2026-09-05 (第58回")[1]
import re
print("residual run170 in entry:", len(re.findall(r"run170", seg)))
print("run171 in entry:", len(re.findall(r"run171", seg)))

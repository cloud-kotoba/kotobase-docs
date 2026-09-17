#!/usr/bin/env python3
import subprocess
cmds = [
    ["git", "add", "query-cosientist.md"],
    ["git", "commit", "-m", "rank 147: fold bench143 run336 (2/60) + falsify157 run337 (6/60) + cosientist120 run337-indep (0/60) + bench144 run338 (1/60) -> 10hr 23/540 ~4.3% 9-set mid-band; + falsify158 run339 (4/60) + bench145 run340 (3/60) -> 11hr 7/120 ~5.8% 2-set; heavy run331A non-reproduced single-window, K-Z3 open continue, rank order unchanged; NEXT K-Z3 current-band(11hr) n-add run341; concurrent sweep of prior rank147 entry corrected"],
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    with open("/tmp/rank_commit.txt", "a", encoding="utf-8") as f:
        f.write("CMD: %s\nEXIT=%d\nSTDOUT:%s\nSTDERR:%s\n" % (c, r.returncode, r.stdout, r.stderr))
print("commit done")
#!/bin/bash
# Rebuild .code/.ttfb from .raw if missing, compute stats, dump all to one log.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
OUT=/tmp/b474_final.txt
: > "$OUT"
echo "=== raw/code/ttfb counts ===" >> "$OUT"
d=$(date '+%H:%M:%S')
echo "now=$d" >> "$OUT"
for f in A B C landing; do
  echo "$f raw=$(wc -l < .b474_${f}.raw 2>/dev/null) code=$(wc -l < .b474_${f}.code 2>/dev/null) ttfb=$(wc -l < .b474_${f}.ttfb 2>/dev/null)" >> "$OUT"
done
echo "=== parse (idempotent) ===" >> "$OUT"
python3 .b474_parse.py >> "$OUT" 2>&1
echo "parse_rc=$?" >> "$OUT"
echo "=== stats ===" >> "$OUT"
python3 .b474_stats.py >> "$OUT" 2>&1
echo "stats_rc=$?" >> "$OUT"
echo "=== report ===" >> "$OUT"
python3 .b474_report.py >> "$OUT" 2>&1
echo "report_rc=$?" >> "$OUT"
echo "=== cold positions ===" >> "$OUT"
python3 - "$OUT" <<'PYEOF'
import sys
out=sys.argv[1]
THRESH=0.5
base="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b474"
lines=[]
for k in ["A","B","C","landing"]:
    vals=[(i+1,float(x)) for i,x in enumerate(open(base+"_"+k+".ttfb").read().split()) if x.strip()]
    c=[ "%d:%.4f"%(i,v) for i,v in vals if v>=THRESH]
    lines.append("RUN%s coldpos=%s"%(k,",".join(c)))
open(out,"a",encoding="utf-8").write("\n".join(lines)+"\n")
PYEOF
echo "pos_rc=$?" >> "$OUT"
echo DONE >> "$OUT"
exit 0
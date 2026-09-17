cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== iter-log top (should be bench 第194回) ===" > /tmp/kb_verify469.txt
grep -n "^- 2026-09-08" query-cosientist.md | head -2 >> /tmp/kb_verify469.txt
echo "=== run469 doc refs ===" >> /tmp/kb_verify469.txt
grep -o "run469[A-C]*" query-cosientist.md | sort | uniq -c >> /tmp/kb_verify469.txt
echo "=== tail of evidence row 403/404 ===" >> /tmp/kb_verify469.txt
grep -n "^## Iteration log" query-cosientist.md | while IFS=: read ln rest; do
  ev=$((ln-1))
  echo "ev_row_line=$ev"
  sed -n "${ev}p" query-cosientist.md | tail -c 700
done >> /tmp/kb_verify469.txt
echo "" >> /tmp/kb_verify469.txt
echo "=== git diff stat ===" >> /tmp/kb_verify469.txt
git diff --stat >> /tmp/kb_verify469.txt 2>&1
echo done
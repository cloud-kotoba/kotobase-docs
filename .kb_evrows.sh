cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== K-Z3 evidence rows (lines matching K-Z3 in evidence context) ===" > /tmp/kb_evrows.txt
grep -n "run468A cold\|run468A-C\|run468A–C\|run467A heavy" query-cosientist.md | head -6 >> /tmp/kb_evrows.txt
echo "=== line 403 context ===" >> /tmp/kb_evrows.txt
sed -n '403p' query-cosientist.md | tail -c 500 >> /tmp/kb_evrows.txt
echo "" >> /tmp/kb_evrows.txt
echo "=== iter log header line now ===" >> /tmp/kb_evrows.txt
grep -n "^## Iteration log" query-cosientist.md >> /tmp/kb_evrows.txt
echo "=== K-Z3 hypothesis row line now ===" >> /tmp/kb_evrows.txt
grep -n "^| K-Z3 | worker |" query-cosientist.md >> /tmp/kb_evrows.txt
echo done
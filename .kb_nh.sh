cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== log -4 ===" > /tmp/kb_newhead.txt
git log --oneline -4 >> /tmp/kb_newhead.txt 2>&1
echo "=== latest iter entry ===" >> /tmp/kb_newhead.txt
grep -n "^- 2026-09-08" query-cosientist.md | head -3 >> /tmp/kb_newhead.txt
echo "=== run468/469 in doc ===" >> /tmp/kb_newhead.txt
grep -o "run46[89][A-C]*" query-cosientist.md | sort | uniq -c >> /tmp/kb_newhead.txt
echo "=== K-Z3 row tail ===" >> /tmp/kb_newhead.txt
grep -n "^| K-Z3 | worker |" query-cosientist.md | while IFS=: read ln rest; do echo "ROW_LEN line=$ln"; sed -n "${ln}p" query-cosientist.md | tail -c 300; done >> /tmp/kb_newhead.txt
echo done
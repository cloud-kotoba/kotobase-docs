cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== K-Z3 hypothesis row line ===" > /tmp/kb_anchor.txt
grep -n "^| K-Z3 | worker |" query-cosientist.md >> /tmp/kb_anchor.txt
echo "=== Iteration log header line ===" >> /tmp/kb_anchor.txt
grep -n "^## Iteration log" query-cosientist.md >> /tmp/kb_anchor.txt
echo "=== latest iter entry first line ===" >> /tmp/kb_anchor.txt
grep -n "^- 2026-09-08: rank 第209回" query-cosientist.md | head -1 >> /tmp/kb_anchor.txt
echo "=== last 3 lines of K-Z3 row (tail) ===" >> /tmp/kb_anchor.txt
grep -n "^| K-Z3 | worker |" query-cosientist.md | while IFS=: read ln rest; do
  echo "ROW_LEN line=$ln"
  sed -n "${ln}p" query-cosientist.md | tail -c 400
done >> /tmp/kb_anchor.txt
echo done
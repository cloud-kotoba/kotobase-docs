cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== run469 refs ===" > /tmp/kb_r469.txt
grep -o "run469[A-C]*" query-cosientist.md | sort | uniq -c >> /tmp/kb_r469.txt
echo "=== .b469 files ===" >> /tmp/kb_r469.txt
ls -la .b469* 2>/dev/null >> /tmp/kb_r469.txt
echo "=== date ===" >> /tmp/kb_r469.txt
date '+%Y-%m-%d %H:%M:%S %Z' >> /tmp/kb_r469.txt
echo "=== uptime ===" >> /tmp/kb_r469.txt
uptime >> /tmp/kb_r469.txt 2>&1
echo "=== live smoke search ===" >> /tmp/kb_r469.txt
curl -s -o /dev/null -w '%{http_code}\n' --connect-timeout 10 --max-time 15 "https://search.kotobase.net/search?q=test" >> /tmp/kb_r469.txt 2>/dev/null
echo "=== live smoke signup ===" >> /tmp/kb_r469.txt
curl -s -o /dev/null -w '%{http_code}\n' --connect-timeout 10 --max-time 15 "https://kotobase.net/signup" >> /tmp/kb_r469.txt 2>/dev/null
echo done
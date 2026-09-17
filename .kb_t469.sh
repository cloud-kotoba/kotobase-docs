cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== t0 ===" > /tmp/kb_time469.txt
cat .b469_t0.txt 2>&1 >> /tmp/kb_time469.txt
echo "=== now JST ===" >> /tmp/kb_time469.txt
date '+%Y-%m-%d %H:%M:%S %Z' >> /tmp/kb_time469.txt
echo "=== payload: run start epoch -> JST ===" >> /tmp/kb_time469.txt
python3 -c "import datetime; print(datetime.datetime.fromtimestamp(1788842/1).strftime('%H:%M:%S'))" 2>/dev/null >> /tmp/kb_time469.txt
echo done
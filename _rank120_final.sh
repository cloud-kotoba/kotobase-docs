cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "HEAD=$(git rev-parse HEAD)" > /tmp/r_final.txt
echo "MAIN=$(git rev-parse net-kotobase/main)" >> /tmp/r_final.txt
git diff --stat HEAD~1 HEAD >> /tmp/r_final.txt 2>&1
echo "--- show rank120 iter head ---" >> /tmp/r_final.txt
echo done >> /tmp/r_final.txt
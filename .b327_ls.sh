#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
ls -la | head -40
echo "=== WC ==="
wc -l query-cosientist.md 2>&1
echo "=== which files ==="
ls query-cosientist*.md 2>&1
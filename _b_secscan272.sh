#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== matched lines ==="
git show 73d431a --format='' | grep -iE 'token|cookie|credential|authorization|secret|api[_-]?key'
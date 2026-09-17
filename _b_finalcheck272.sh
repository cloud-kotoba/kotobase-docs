#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== diff HEAD~1..HEAD (added lines) ==="
git show 73d431a --format='' | grep '^+' | cut -c1-90
echo "..."
echo "=== confirm only query-cosientist.md changed ==="
git show --stat --format='' 73d431a | tail -3
echo "=== secret scan: no token/cookie/credential in committed diff ==="
git show 73d431a --format='' | grep -iE 'token|cookie|credential|authorization|secret|api[_-]?key' | wc -l
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== what was sibling 15ce40d? ====="
  git log -1 --oneline 15ce40d 2>&1
  echo "===== my commit parents ====="
  git log --oneline -3
  echo "===== run487 present at HEAD ====="
  git show HEAD:query-cosientist.md | grep -c "run487"
  echo "===== sibling run (any new run) in HEAD iter-log first 2 ====="
  git show HEAD:query-cosientist.md | sed -n '407p' | cut -c1-60
  echo "===== diffstat HEAD vs 15ce40d ====="
  git diff --stat 15ce40d HEAD
  echo "===== diff rows (excluding whitespace) sample ====="
  git diff 15ce40d HEAD -- query-cosientist.md | grep -E "^[+-]" | grep -vE "^(\+\+\+|---)" | cut -c1-100 | head -20
} > /tmp/b487final.txt 2>&1
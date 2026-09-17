#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
echo "--- remotes ---"
git remote -v
echo "--- current HEAD ---"
git log --oneline -8
echo "--- working tree status ---"
git status --short 2>&1 | head -30
echo "--- untracked recent temp files ---"
ls -la .hermes-tmp* _b71* _cos* 2>/dev/null | head
} > /tmp/cos_state.txt 2>&1
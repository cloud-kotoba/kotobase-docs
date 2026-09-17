#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b328_git2.txt
echo "=== REMOTES ===" > $R
git remote -v >> $R 2>&1
echo "=== HEAD ===" >> $R
git rev-parse HEAD >> $R 2>&1
echo "=== branch ===" >> $R
git branch -a >> $R 2>&1
echo "=== FETCH net-kotobase ===" >> $R
git fetch net-kotobase >> $R 2>&1; echo "rc=$?" >> $R
echo "=== net-kotobase/main ===" >> $R
git rev-parse net-kotobase/main >> $R 2>&1
echo "=== is HEAD ancestor of net-kotobase/main? ===" >> $R
git merge-base --is-ancestor HEAD net-kotobase/main >> $R 2>&1; echo "ancestor_rc=$?" >> $R
echo "=== rev-list HEAD..net-kotobase/main ===" >> $R
git rev-list --count HEAD..net-kotobase/main >> $R 2>&1
echo "DONE" >> $R
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== pwd ==="; pwd
  echo "=== git version ==="; git --version
  echo "=== git status ==="; git status 2>&1 | head -20
  echo "=== git log ==="; git log --oneline -6 2>&1
} > _cos_diag.txt
echo "done"
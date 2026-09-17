#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "HEAD:"
  git rev-parse HEAD
  echo "REMOTE main:"
  git rev-parse net-kotobase/main
  echo "ahead/behind (HEAD vs remote main):"
  git rev-list --left-right --count HEAD...net-kotobase/main
  echo "status:"
  git status --short | head -40
} > /tmp/b_gitstate.txt 2>&1

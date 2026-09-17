#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch > _rank_fetch.log 2>&1
echo "---REV---" > _rank_state.log
git rev-parse HEAD >> _rank_state.log 2>&1
git rev-parse bench_fetch/main >> _rank_state.log 2>&1
echo "---STATUS---" >> _rank_state.log
git status --short >> _rank_state.log 2>&1
echo done > _rank_done.log
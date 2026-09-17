#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
date
git rev-parse HEAD
git rev-parse net-kotobase/main
uptime
} > ._b_state_out.txt 2>&1

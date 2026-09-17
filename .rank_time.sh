#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{ date '+%Y-%m-%d %H:%M:%S %Z'; uptime; } > .rank_time.txt 2>&1
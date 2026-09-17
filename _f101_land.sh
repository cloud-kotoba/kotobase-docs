#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase
echo "FETCH_EXIT=$?"
echo "LOCAL=$(git rev-parse HEAD)"
echo "REMOTE=$(git rev-parse net-kotobase/main)"
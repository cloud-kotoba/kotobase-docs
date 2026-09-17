#!/bin/sh
date "+PRE %Y-%m-%d %H:%M:%S JST"
uptime
echo "--- smoke ---"
curl -s -o /dev/null -m 10 -w "landing %{http_code}\n" https://kotobase.net/
curl -s -o /dev/null -m 10 -w "signup %{http_code}\n" https://kotobase.net/signup
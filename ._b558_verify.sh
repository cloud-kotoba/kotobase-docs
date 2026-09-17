#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
curl -s -o /dev/null -w "search?q=test %{http_code} %{time_starttransfer}\n" "https://kotobase.net/search?q=test"
curl -s -o /dev/null -w "search?q=hello %{http_code} %{time_starttransfer}\n" "https://kotobase.net/search?q=hello"
curl -s -o /dev/null -w "search-bare %{http_code} %{time_starttransfer}\n" "https://kotobase.net/search"
curl -s -o /dev/null -w "root %{http_code} %{time_starttransfer}\n" "https://kotobase.net/"
curl -s -o /dev/null -w "signup %{http_code} %{time_starttransfer}\n" "https://kotobase.net/signup"
} > ._b558_verify_out.txt 2>&1

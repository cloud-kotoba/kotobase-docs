#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "== append =="
  python3 .b487_append.py
  echo "== ilog =="
  python3 .b487_ilog.py
} > /tmp/b487apply.txt 2>&1
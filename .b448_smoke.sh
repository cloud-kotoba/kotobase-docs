#!/bin/bash
# live smoke for run448 tick
for u in "https://kotobase.net/" "https://kotobase.net/signup" "https://search.kotobase.net/search?q=test"; do
  code=$(curl -sS -o /dev/null -w "%{http_code} %{time_starttransfer}" "$u" 2>&1)
  echo "$u -> $code"
done
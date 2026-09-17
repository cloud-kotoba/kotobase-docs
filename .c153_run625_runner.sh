#!/bin/zsh
# K-Z3 13時台 n 積み増し run625A-C (cosientist 第154回, 2026-09-15 13時台)
# 同測定法: n=20 x 3 + landing control, 別接続 curl, cold>=0.5s
# 301 読替後の正 endpoint: search.yataverse.com/search?q=test, control kotoba.cloud/
set -u
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
EP="https://search.yataverse.com/search?q=test"
CTRL="https://kotoba.cloud/"

measure() {
  local label="$1" url="$2" n="$3" out="$4"
  : > "$out"
  local i
  for ((i=1; i<=n; i++)); do
    local ttfb
    ttfb=$(curl -o /dev/null -s -w '%{http_code} %{time_starttransfer}' --no-keepalive "$url")
    printf '%s %s\n' "$ttfb" >> "$out"
  done
}

date '+%F %T %z' > .c153_t0.txt
uptime >> .c153_t0.txt

measure A "$EP" 20 .c153_run625_A.ttfb
measure B "$EP" 20 .c153_run625_B.ttfb
measure C "$EP" 20 .c153_run625_C.ttfb
measure CTRL "$CTRL" 20 .c153_run625_landing.ttfb

date '+%F %T %z' > .c153_time.txt
uptime >> .c153_time.txt

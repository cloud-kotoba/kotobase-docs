#!/bin/bash
# bench 第164回: K-Z3 16時台(9/7) n積み増し run374A-C + landing control
# Method: n=20 x 3 runs, separate curl connections, cold threshold >=0.5s TTFB,
# nearest-rank p50. Endpoint search.kotobase.net/search?q=test, control kotobase.net/signup.
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
outA=.b374_374A.txt; outB=.b374_374B.txt; outC=.b374_374C.txt; outLand=.b374_land.txt
{ echo "start $(date -Iseconds)"; uptime; } > .b374_time.txt

run_one() {
  local url="$1" outf="$2" n="$3"
  > "$outf"
  for i in $(seq 1 "$n"); do
    res=$(curl -s -o /dev/null -w '%{http_code} %{time_total}' "$url")
    echo "$res" >> "$outf"
    sleep 0.05
  done
}
run_one "$SEARCH" "$outA" 20
run_one "$SEARCH" "$outB" 20
run_one "$SEARCH" "$outC" 20
run_one "$CONTROL" "$outLand" 20
{ echo "end $(date -Iseconds)"; uptime; } >> .b374_time.txt
echo "DONE"
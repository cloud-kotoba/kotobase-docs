#!/bin/zsh
# bench K-Z3 runner (same claim-contract method): 3 sets x 20 sequential /search?q=test + landing control /signup, separate connections curl, single -w combining code+ttfb
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b532_raw.txt
: > "$OUT"
run_set() {
  local ep="$1" tag="$2"
  for i in {1..23}; do
    curl -o /dev/null -s -w "%{http_code} %{time_starttransfer}\n" "https://kotobase.net${ep}" >> "$OUT.tag.$tag" 2>/dev/null
  done
}
rm -f "$OUT".tag.* 2>/dev/null
run_set "/search?q=test" A
run_set "/search?q=test" B
run_set "/search?q=test" C
run_set "/signup" CTRL
for t in A B C CTRL; do
  # drop first 3 lines (warmup) and paste raw+trimmed
  tail -n +4 "$OUT.tag.$t" > "$OUT.tag.$t.trim"
  wc -l "$OUT.tag.$t" "$OUT.tag.$t.trim" >> "$OUT"
done
echo DONE >> "$OUT"

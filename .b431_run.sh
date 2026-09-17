#!/bin/bash
SEARCHA="https://search.kotobase.net/search?q=test"
SIGNUP="https://kotobase.net/signup"
while IFS=',' read -r tag url; do
    : > ".b431_${tag}.txt"
    for i in $(seq 1 20); do
        tt=$(curl -s -o /dev/null -w '%{time_starttransfer}' --max-time 40 "$url")
        if [ -z "$tt" ]; then tt="999"; fi
        printf '%s %d %s\n' "$tag" "$i" "$tt" >> ".b431_${tag}.txt"
        sleep 0.4
    done
done <<EOF
A,$SEARCHA
B,$SEARCHA
C,$SEARCHA
ctrl,$SIGNUP
EOF
echo ALLDONE

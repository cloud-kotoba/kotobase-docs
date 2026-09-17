#!/bin/bash
OUTDIR=$(pwd)
SEARCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
ST="$OUTDIR/.b430_stats.txt"
: > "$ST"
batch() {
    url="$1"; label="$2"; f="$3"
    : > "$f"
    for i in $(seq 1 20); do
        curl -sS -o /dev/null -w "%{time_starttransfer} %{http_code}\n" "$url" >> "$f" 2>/dev/null
    done
    n=$(awk '$2==200{n++}END{print n+0}' "$f")
    cold=$(awk '$2==200 && $1>=0.5{c++}END{print c+0}' "$f")
    codes=$(awk '{print $2}' "$f" | sort -u | tr '\n' ' ')
    sortedf="$f.sorted"
    awk '$2==200{print $1}' "$f" | sort -n > "$sortedf"
    if [ "$n" -ge 1 ]; then
        minv=$(awk 'NR==1{print $1}' "$sortedf")
        maxv=$(tail -1 "$sortedf")
        p50=$(awk 'NR==10{print $1}' "$sortedf")
    else
        minv="na"; maxv="na"; p50="na"
    fi
    echo "$label n=$n cold=$cold codes=[$codes] p50=${p50}s min=${minv}s max=${maxv}s" > "$OUTDIR/.b430_line.txt"
    cat "$OUTDIR/.b430_line.txt" >> "$ST"
    cat "$OUTDIR/.b430_line.txt"
}
batch "$SEARCH" "run430A" "$OUTDIR/.b430_run430A.txt"
batch "$SEARCH" "run430B" "$OUTDIR/.b430_run430B.txt"
batch "$SEARCH" "run430C" "$OUTDIR/.b430_run430C.txt"
batch "$CTRL" "landing_control" "$OUTDIR/.b430_landing_control.txt"
echo "---done---"

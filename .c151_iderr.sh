#!/bin/sh
OUT=.c151_iderr.txt
: > "$OUT"
cat .c151_iterins_out.txt >> "$OUT" 2>&1
cat .c151_iterins_err.txt >> "$OUT" 2>&1
ls -la .c151_iterins_out.txt .c151_iterins_err.txt >> "$OUT" 2>&1
#!/bin/bash
D=/tmp/cos123_diag3.txt
: > $D
echo "PATH=$PATH" >> $D
type python3 >> $D 2>&1
python3 -c 'import sys; print("OK", sys.version)' >> $D 2>&1
echo END >> $D

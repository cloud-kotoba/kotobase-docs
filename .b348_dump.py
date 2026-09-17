#!/usr/bin/env python3
# pretty-print .b348_loc.txt with exact line breaks preserved (read_file shows raw; here we just dump small)
import sys
print(open(".b348_loc.txt",encoding="utf-8").read())
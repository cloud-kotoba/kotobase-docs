#!/usr/bin/env python3
vals = [float(l.strip()) for l in open('.b448_run448A.ttfb') if l.strip()]
for i, v in enumerate(vals, 1):
    if v >= 0.5:
        print(f'pos{i}: {v:.4f}s')
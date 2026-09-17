import glob

# Re-derive from the ORIGINAL capture: the "bad" bare-number lines were the
# ttfb halves; code halves were lines starting with a 3-digit code. But some
# lines may contain BOTH halves merged ('200 1.301664' style) plus separate.
# Print every raw line group for A to decide.
p = ".b573_A.ttfb"
with open(p, encoding="utf-8") as f:
    print(f.read())

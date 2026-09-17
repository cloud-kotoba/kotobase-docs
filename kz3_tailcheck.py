import sys
with open('query-cosientist.md') as f:
    lines = f.read().splitlines()
line = lines[128]
sys.stdout.write("TAIL: " + repr(line[-300:]) + "\n")
sys.stdout.write("ENDS_WITH_PIPE: " + str(line.rstrip().endswith('|')) + "\n")

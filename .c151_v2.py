import io
FN = 'query-cosientist.md'
with io.open(FN, 'r', encoding='utf-8', newline='') as f:
    lines = f.read().split('\n')
o = io.open('.c151_v2.txt', 'w', encoding='utf-8')
o.write("line279 total chars: %d\n" % len(lines[278]))
o.write("line279 last 3 chars repr: %r\n" % lines[278][-3:])
o.write("line279 last 60 chars:\n%s\n" % lines[278][-60:])
o.write("line280 (first 80): %s\n" % lines[279][:80])
o.write("line281 (first 80): %s\n" % lines[280][:80])
o.write("total lines: %d\n" % len(lines))
o.close()
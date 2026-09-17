import io, subprocess, time
out = io.open('.c151_poll2.txt', 'w', encoding='utf-8')
start = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
out.write("start HEAD=%s\n" % start)
newhead = start
deadline = time.time() + 170
advanced = False
while time.time() < deadline:
    time.sleep(12)
    h = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    if h != start:
        newhead = h
        advanced = True
        out.write("advanced at t=%.0f HEAD=%s\n" % (time.time() - (deadline-170), h))
        break
    out.write("poll still at %s (elapsed %.0fs)\n" % (h[:7], time.time()-(deadline-170)))
out.write("final advanced=%s newhead=%s\n" % (advanced, newhead))
subj = subprocess.run(['git', 'log', '--oneline', '-3'], capture_output=True, text=True)
out.write("recent:\n" + subj.stdout + "\n")
out.close()
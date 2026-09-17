import io, subprocess, time
out = io.open('.c151_poll.txt', 'w', encoding='utf-8')
base = 'f418dea'
for attempt in range(8):
    p = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    h = p.stdout.strip()
    out.write("poll %d HEAD=%s\n" % (attempt, h))
    if h != base:
        out.write("HEAD advanced!\n")
        subj = subprocess.run(['git', 'log', '--oneline', '-1'], capture_output=True, text=True)
        out.write("head1: %s\n" % subj.stdout.strip())
        break
    time.sleep(15)
out.close()
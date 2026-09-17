import subprocess
# check what HEAD contains vs worktree for bench 第183回
head = subprocess.run(['git', 'show', 'HEAD:query-cosientist.md'], capture_output=True, text=True).stdout
open('/tmp/bench_h.txt','w').write('HEAD has bench183: %s\n' % ('bench 第183回' in head))
open('/tmp/bench_h.txt','a').write('HEAD bench183 line uses run404: %s\n' % ('bench 第183回。23:04 JST tick。HEAD 966ac7c = falsify 第175回 (22:33, dedupe iter-log; K-Z3 22hr run401 8/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HE' in head))
# show only the iter-log lines containing bench 第183回 in HEAD, first 180 chars each
for ln in head.split('\n'):
    if 'bench 第183回' in ln:
        idx = ln.find('bench 第183回')
        open('/tmp/bench_h.txt','a').write('HEAD iter line seg: %s\n' % ln[max(0,idx-10):idx+90])
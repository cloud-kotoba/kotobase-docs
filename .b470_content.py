import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=15):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return r.stdout
    except Exception:
        return ''
blob = run(['git','show','HEAD:query-cosientist.md'])
out.append('HEAD_blob_has_run470_ev=%d' % ('run470A' in blob and '5/60' in blob and '第212回' in blob))
out.append('HEAD_blob_has_falsify212_iter=%d' % ('falsify 第212回' in blob))
out.append('HEAD_blob_run471=%d' % ('run471' in blob))
out.append('HEAD_blob_len=%d' % len(blob))
# also check worktree file (should match HEAD, diff empty)
wf = open('query-cosientist.md', encoding='utf-8').read()
out.append('worktree_has_run470A=%d' % ('run470A' in wf))
out.append('worktree_has_212iter=%d' % ('falsify 第212回' in wf))
with open('/tmp/f_content.log','w') as f:
    f.write('\n'.join(out))
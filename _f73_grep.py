import subprocess
cwd = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def grep(ref, pat):
    r = subprocess.run(['git', 'grep', '-c', pat, ref, '--', 'query-cosientist.md'],
                       capture_output=True, text=True, cwd=cwd)
    return r.stdout.strip()
checks = {
 'evidence_in_HEAD': grep('HEAD', '第73回, K-Z3 7時台 n 積み増し run193A'),
 'evidence_in_def7b19': grep('def7b19', '第73回, K-Z3 7時台 n 積み増し run193A'),
 'falsify73log_in_HEAD': grep('HEAD', 'falsify 第73回'),
 'bench73log_in_HEAD': grep('HEAD', 'bench 第73回'),
}
import json
print(json.dumps(checks, ensure_ascii=False, indent=1))

path = 'query-cosientist.md'
txt = open(path, encoding='utf-8').read()
for r in ['run457','run458','run459']:
    print(r, txt.count(r))
# confirm clean diff expectation: show whether HEAD file matches worktree
import subprocess
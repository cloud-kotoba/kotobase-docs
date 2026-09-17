import subprocess, re
# The K-Z3 runs have always used "search" — find prior scripts to see exact URL used in successful (200) runs
import glob
for f in sorted(glob.glob('_f7[0-6]_run*.sh')) + sorted(glob.glob('_fz7[0-2]_run*.sh')) + sorted(glob.glob('_b7[0-6]_run*.sh')):
    for line in open(f):
        if 'kotobase.net' in line and 'search' in line:
            print(f, line.strip()[:130])
            break

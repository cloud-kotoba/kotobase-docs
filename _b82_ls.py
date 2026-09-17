import os
for f in sorted(os.listdir('.')):
    if os.path.isfile(f):
        print(f, os.path.getsize(f))

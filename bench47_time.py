import datetime, subprocess
now = datetime.datetime.now().astimezone()
print("now:", now.isoformat())
load1 = open("/proc/loadavg").read() if False else None
out = subprocess.run(["/usr/sbin/sysctl", "-n", "vm.loadavg"], capture_output=True, text=True)
print("loadavg:", out.stdout.strip() or out.stderr.strip())

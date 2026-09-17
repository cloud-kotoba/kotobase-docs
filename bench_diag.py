import datetime, os, subprocess

lines = []
lines.append("cwd=" + os.getcwd())
lines.append("local=" + datetime.datetime.now().isoformat())
lines.append("utc=" + datetime.datetime.now(datetime.timezone.utc).isoformat())
p = subprocess.run(["uptime"], capture_output=True, text=True)
lines.append("uptime_out=" + p.stdout.strip())
lines.append("uptime_err=" + p.stderr.strip())
with open("bench_diag_out.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
print("wrote bench_diag_out.txt")

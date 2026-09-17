import subprocess, re
u = subprocess.run(["uptime"], capture_output=True, text=True).stdout
load1 = float(re.search(r"load averages?: ([\d.]+)", u).group(1))
print(load1)

doc_path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
doc = open(doc_path, encoding="utf-8").read()
lines = doc.splitlines(keepends=True)
ev = (" bench 2026-09-05 (第40回, K-Z3 深夜帯 6時台 n 積み増し run115A–C, 同測定法 n=20 × 3 run, "
      "別接続 curl, Tokyo, 06:13 JST, 全 80/80 200, host load1 %.2f は production HTTP 実測のため gate 外): "
      "run115A cold(>=0.5s) 0/20 p50 0.051s (0.043–0.078s) / run115B cold 0/20 p50 0.046s (0.042–0.101s) / "
      "run115C cold 0/20 p50 0.049s (0.041–0.092s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
      "cold 0/20 p50 0.052s と静穏で control 分離成立。3 run 完全静穏 (falsify run114A–C に続き 5時台/6時台帯の静穏継続)。"
      "status 判定は rank に委ねる\n" % load1)
# append to K-Z3 hypothesis row (find its table line start)
kz3 = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 |")]
lines[kz3[0]] = lines[kz3[0]].rstrip("\n") + ev
open(doc_path, "w", encoding="utf-8").write("".join(lines))
print("appended to line", kz3[0] + 1)

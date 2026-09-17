import sys
p = "query-cosientist.md"
data = open(p, "r", encoding="utf-8").read()

checks = {
    "run509A cold 1/20 ev": data.count("run509A cold(>=0.5s) 1/20 (1.5981s 9番目単発)"),
    "run509 in iterlog": data.count("falsify 第226回。22:19 JST tick"),
    "22時台通算 8/120": data.count("22時台通算 = run508 (7/60 ~11.7%) + run509 (1/60) = 8/120 (~6.7%)"),
    "zwnbsp": data.count("\u200b") + data.count("\ufeff"),
    "hashmark": data.count("#####"),
}
for k, v in checks.items():
    sys.stdout.write("%s: %d\n" % (k, v))

# also confirm no duplicate old evidence anchor broken: iter log top 3 lines
lines = data.split("\n")
for i, l in enumerate(lines):
    if l.strip().startswith("## Iteration log"):
        sys.stdout.write("ITERTOP1: %s\n" % lines[i+1][:140])
        sys.stdout.write("ITERTOP2: %s\n" % lines[i+2][:140])
        break
sys.stdout.write("KZ3TAIL: %s\n" % lines[278][-150:])
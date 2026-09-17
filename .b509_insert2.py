# -*- coding: utf-8 -*-
import sys
SRC = "/tmp/qc_head.md"
DST = "/tmp/qc_new.md"
EV = "/tmp/ev509.txt"
IL = "/tmp/ilog509.txt"
KZ3 = "| K-Z3 | worker |"
ILOG = "## Iteration log"
def stripcomb(txt):
    return txt.replace("\u0308", "")
def rstrip_last(txt):
    return txt.rstrip("\n")
def main():
    t = open(SRC, encoding="utf-8").read()
    ev = open(EV, encoding="utf-8").read()
    il = open(IL, encoding="utf-8").read()
    ev = stripcomb(ev)
    il = stripcomb(il)
    i = t.index(KZ3)
    j = t.index("\n", i)
    t = t[:j] + ev + t[j:]
    k = t.index(ILOG)
    l = t.index("\n", k)
    t = t[:l+1] + il + "\n" + t[l+1:]
    open(DST, "w", encoding="utf-8").write(t)
    print("OK kz3_at=%d ilog_at=%d" % (i+1, k+1))
if __name__ == "__main__":
    main()
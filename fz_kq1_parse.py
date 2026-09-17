#!/usr/bin/env python3
import json, os
p = "/tmp/kq1_run3.json"
err = open("/tmp/kq1_run3.err").read()
out = {"err": err[:500]}
if os.path.exists(p) and os.path.getsize(p) > 0:
    d = json.load(open(p))
    out["observedAt"] = d["observedAt"]
    out["firstObservedMs"] = d["firstObservedMs"]
    for name, s in d["series"].items():
        out[name] = s["latencyMs"]
        out[name + "_status"] = s["statusCounts"]
        out[name + "_colo"] = s["colos"]
    out["correctness"] = d["correctness"]
print(json.dumps(out, ensure_ascii=False, indent=1))
print("<<END>>")

#!/usr/bin/env python3
MD="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(MD,encoding="utf-8").read()

# ---- 1) replace my (incorrect) bench 第89回 iteration-log line with run217 renamed version ----
old_entry_start="- 2026-09-06: bench \u7b2c89\u56de\u300215:09 JST tick\u3002"
i=data.find(old_entry_start)
if i<0:
    print("OLD_ENTRY_NOT_FOUND")
else:
    # the entry is one line ending before "\n- " next entry or "\n\n"
    j=data.find("\n", i)
    # find next line start
    k=data.find("\n- ", j)
    if k<0:
        k=data.find("\n## ", j)
    old_block=data[i:j]
    new_block=(
        "- 2026-09-06: bench \u7b2c89\u56de\u300215:09 JST tick\u3002worktree detached HEAD \u306e\u305f\u3081 "
        "fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f (HEAD \u306f tick \u4e2d\u306b falsify \u7b2c90\u56de aa1260a \u3078\u6b20\u804a\u3001"
        "\u6700\u7d42\u72b6\u614b\u306f main \u5148\u7aef aa1260a = falsify \u7b2c90\u56de\u306b\u4e00\u81f4)\u3002live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002"
        "host load1 77.81 (gate 7.5 \u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057\u300chost busy (load1 77.81)\u300d\u3092\u8a18\u9332\u3002"
        "\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c, gate \u5916): K-Z3 15\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 "
        "\u2014 \u305f\u3060\u3057 falsify \u7b2c90\u56de (\u540c tick 15:16 \u5b9f\u6e2c) \u3068 run ID run216 \u304c\u885d\u7a81 (\u3088\u3063\u3001\u4\u9059\u308\u3046\u3001\u6\u330\u205\u309\u4\u305\u501\u301\u308\u002\u300\u301\u309\u308\u301\u302\u300\u304\u300\u304\u301\u305\u301\u304\u301\u305\u302\u306\u301"
    )
    print("DEBUG generated tail too messy, abort"); raise SystemExit
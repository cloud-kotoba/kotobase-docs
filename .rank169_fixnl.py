#!/usr/bin/env python3
import io
MD = "query-cosientist.md"
txt = io.open(MD, "r", encoding="utf-8").read()
MARKER = "使用)。- 2026-09-07: bench 第177回"
REPL = "使用)。\n- 2026-09-07: bench 第177回"
n = txt.count(MARKER)
if n != 1:
    print("ABORT: marker count =", n)
    raise SystemExit(3)
new = txt.replace(MARKER, REPL, 1)
# safety: verify header count stays 1 and entry ordering
if new.count("\n## Iteration log\n") + (1 if new.startswith("## Iteration log\n") else 0) != 1:
    print("ABORT: header count broken")
    raise SystemExit(4)
io.open(MD, "w", encoding="utf-8").write(new)
print("FIXED: newline inserted, marker now", new.count(MARKER))
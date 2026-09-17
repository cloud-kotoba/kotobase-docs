#!/usr/bin/env python3
# Fix: restore falsify 122 iteration-log header that got consumed by the r117 insert
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# After r117 entry + NEXT, the falsify 122 line lost its header.
# Find the orphan line and prepend the header.
bad = "  NEXT: K-Z3 24時台 n 積み増し継続 — 24時台(0時台)帯初計測 run268 (2/60 ~3.3%) は 23時台 (30/540 ~5.6%) と同水準の低〜中位帯候補が立ち、現時刻帯 0時台(24時台)の間は 24時台 n 積み増し、時間帯移行後は次の帯初/帯確定へ (深夜帯 ~26-31% 平坦パターンへの収束か 24時台限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run269 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\nworktree detached HEAD (HEAD fe84c1e"

good = "  NEXT: K-Z3 24時台 n 積み増し継続 — 24時台(0時台)帯初計測 run268 (2/60 ~3.3%) は 23時台 (30/540 ~5.6%) と同水準の低〜中位帯候補が立ち、現時刻帯 0時台(24時台)の間は 24時台 n 積み増し、時間帯移行後は次の帯初/帯確定へ (深夜帯 ~26-31% 平坦パターンへの収束か 24時台限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run269 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\n- 2026-09-07: falsify 第122回。00:00 JST tick。worktree detached HEAD (HEAD fe84c1e"

if bad in content:
    content = content.replace(bad, good, 1)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("HEADER_RESTORED")
elif good in content:
    print("ALREADY_OK")
else:
    print("PATTERN_NOT_FOUND", file=sys.stderr)
    sys.exit(1)
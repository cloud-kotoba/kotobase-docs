import io, sys

FN = 'query-cosientist.md'
EVID = (" cosientist 2026-09-09 (第151回, K-Z3 0時台(24時台) n 積み増し run519A-C - 00:48 JST 独立計測; "
        "先行 falsify 第230回 (00:42-43, run518 cold 10/60) が run518 を commit 済みのため run519 に読替 "
        "(run216/256/263/278 precedent, 同一帯 0時台 独立 4 セット目), 同測定法 n=20 x 3 + landing control, "
        "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
        "00:48:11-00:48:53 JST, 全 80/80 200, host load1 26.65-30.89 (00:48 uptime, gate 7.5 大幅超過) は "
        "production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): "
        "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run519A 冒頭単発 1.0254s (2番目) p50 0.177s "
        "/ run519B cold 0/20 p50 0.101s max 0.273s / run519C cold 0/20 p50 0.093s max 0.245s "
        "- control (kotobase.net/signup) cold 1/20 (max 0.5787s 閾値 0.5s 直上 境界) で 分離 は 境界成立 "
        "(完全静穏 未達) - 0時台帯 通算 (falsify run516 5/60 + bench run517 6/60 + falsify run518 10/60 + 本 run519 1/60) "
        "= 22/240 (~9.2%) の 4 セット - 深夜帯 traffic 最低帯 0時台 で falsify run518A 重クラスタ 9/20 の "
        "~6 分後 散発単発 減衰 (heavy 非再現, 「帯内 1 窓即消失」型継続) で traffic 依存説 の 反証材料 継続, "
        "status 判定 は rank に委ねる (rank 専門)")

MARKER = "status 判定 は rank に委ねる (rank 専門。"

with io.open(FN, 'r', encoding='utf-8', newline='') as f:
    data = f.read()
lines = data.split('\n')
l = lines[278]  # 0-indexed line 279
assert l.count(MARKER) >= 1, "marker not found in line279"
last = l.rindex(MARKER)
tail = l[last:]
# sanity: this marker's occurrence is near the very end of the cell
assert len(l) - (last + len(MARKER)) < 30, "marker not near end: tail=%r" % l[last:]
# insert evidence right after the marker occurrence
newl = l[:last + len(MARKER)] + EVID + l[last + len(MARKER):]
lines[278] = newl
out = '\n'.join(lines)
with io.open(FN, 'w', encoding='utf-8', newline='') as f:
    f.write(out)

# verification report
with io.open('.c151_evcheck.txt', 'w', encoding='utf-8') as o:
    o.write("line279 new length: %d\n" % len(newl))
    o.write("tail after insert:\n")
    o.write(newl[-700:] + "\n")
    o.write("count run519: %d\n" % newl.count('run519'))
o.close()
print("done")
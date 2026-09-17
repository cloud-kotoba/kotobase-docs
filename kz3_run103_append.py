import io

DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = open(DOC, encoding="utf-8").read()

entry = """- 2026-09-05: falsify 第35回。新規 evidence: K-Z3 深夜帯 0時台 run103A–C (00:27–00:30 JST,
  n=20 × 3 + landing control, 全 200)。run103A/B/C cold 0/20, p50 0.067/0.078/0.116s,
  landing control cold 0/20 p50 0.101s で静穏 — run102A 型 cold クラスタは 0時台
  2 試行目では再現せず。0時台通算 cold>0 は 4 試行中 1 試行、深夜帯通算は
  78 試行中 23 試行 (~29.5%)。traffic 依存説に対しては 23時台〜0時台の連続再現
  (4 例) と本試行の消失が混在し、帯発現率はばらつき継続。status 遷移なし
  (rank 専門)。host load1 26.46 (tick 開始時) で K-Q1 local profiling gate
  (7.5) 超過のため不実施。NEXT: K-Z3 0時台 n 積み増し継続。
"""

anchor = "  NEXT: K-Z3 0時台 n 積み増し継続 (帯発現率 2/3、確定には n 不足)。\n"
assert text.count(anchor) == 1, f"anchor count = {text.count(anchor)}"
text = text.replace(anchor, anchor + "\n" + entry)
open(DOC, "w", encoding="utf-8").write(text)
print("appended")

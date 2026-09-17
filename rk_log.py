path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path) as f:
    text = f.read()

anchor = """  status 判定は rank に委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。
"""
assert text.count(anchor) == 1, f"anchor occurrences: {text.count(anchor)}"

entry = """- 2026-09-05: rank 第34回。新規 evidence: K-Z3 深夜帯 23時台 3 セット —
  cosientist run99A–C (23:13–14, run99A cold 5/20 散発配置, landing control
  borderline 1 件で完全分離に至らず), falsify run100A–C (23:20, run100A cold 2/20
  散発配置, landing control cold 0/20 で control 分離成立), bench run101A–C
  (23:34, run101A cold 3/20, control 静穏) を取り込み。run99A/100A/101A と
  cold 単独クラスタ型 (warm 同時上振れなし) が深夜帯 3 例連続 — traffic 最低帯
  でも日中帯型の突発が存続し、深夜低頻度の期待 (rank 第33回) に反して K-Z3
  traffic 依存説は弱まる。ただし run99A は landing borderline のため 3 例のうち
  2 例のみが分離成立。status 遷移なし: K-Z2/K-Z3 とも open 維持
  (evidence は機構確定に至らず)、*/2 高頻度化介入は引き続き反証まで保留。
  rank ブロックを第23回版から第34回版へ差替え (順位変動なし、K-Z3 の帯別分布に
  深夜帯を追加)。host load1 30.22 (本 tick 実測 00:12) で gate (7.5) 超過継続の
  ため K-Q1 local profiling は不実施。live smoke は / と /signup とも 200。
  0時台 (00:00–00:59) への帯移行観測が次の情報利得 — 23時台 (~29–32%) が
  深夜の高止まりなのか単一窓なのかを切分ける。
  NEXT: K-Z3 0時台 (00:00 以降) n=20 × 3 + landing control (23時台 3 例連続の
  cold 単独クラスタが 0時台でも再現するか — 連続再現なら traffic 依存説への
  反証材料として重みが増す)。
"""
text = text.replace(anchor, anchor + entry)
with open(path, "w") as f:
    f.write(text)
print("iteration log appended OK")

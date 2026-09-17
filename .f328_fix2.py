import io
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(PATH, encoding="utf-8").read()
fixed = txt.replace("\u95c7\u5024\u5224\u5b9a", "\u95c7\u5024\u5224\u5b9a")  # 闇値 -> 閾値
before = txt.count("\u95c7\u5024\u5224\u5b9a")
# correct: replace 闇値 with 閾値
fixed = txt.replace("\u95c7\u5024", "\u95c7\u5024")  # placeholder noop
from_ = "\u95c7\u5024\u5224\u5b9a"
to_ = "\u95c7\u5024\u5224\u5b9a"
# actual: 闇 = U+95C7, 閾 = U+95C8
realfrom = "\u95c7\u5024"
realto = "\u95c8\u5024"
fixed = txt.replace(realfrom, realto)
n = txt.count(realfrom)
io.open(PATH, "w", encoding="utf-8").write(fixed)
print("replaced_count=", n)
print("now_has_wrong=", fixed.count(realfrom))
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    t = f.read()

before = t

# 乗離 -> 乖離 (wrong kanji 乗 vs correct 乖)
n1 = t.count("\u4e57\u96e2")
t = t.replace("\u4e57\u96e2", "\u4e57\u96e2".replace("\u4e57", "\u4e57"))

# targeted replacements using explicit correct characters
t = t.replace("\u4e57\u96e2 0)", "\u4e57\u96e2 0)")
t = t.replace("\u4e57\u96e2", "\u4e57\u96e2")
t = t.replace("\u5b8c\u5168\u9759\u7a33\u3067 control", "\u5b8c\u5168\u9759\u7a33\u3067 control")
t = t.replace("\u5b8c\u5168\u9759\u7a33", "\u5b8c\u5168\u9759\u7a33")
t = t.replace("\u4e2d\u4f4d\u5e26 (run638", "\u4e2d\u4f4d\u5e26 (run638")
t = t.replace("\u4e2d\u4f4d\u5e26", "\u4e2d\u4f4d\u5e26")
t = t.replace("\u4e2d\u4f4d\u5e26", "\u4e2d\u4f4d\u5e26")
t = t.replace("\u4e2d\u4f4d\u5e26", "\u4e2d\u4f4d\u5e26")

# The real fixes: replace the three wrong glyphs with correct ones.
# 乗 (U+4E57, wrong) -> 乖 (U+4E56, correct)
t = t.replace("\u4e57\u96e2", "\u4e56\u96e2")
# 稳 (U+7A33, wrong JP glyph) -> 穏 (U+7A4F, correct)
t = t.replace("\u9759\u7a33", "\u9759\u7a4f")
# 带 (U+5E26, wrong) -> 帯 (U+5E2F, correct)
t = t.replace("\u4e2d\u4f4d\u5e26", "\u4e2d\u4f4d\u5e2f")

if t != before:
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(t)
    print("fixed and written")
else:
    print("no changes")

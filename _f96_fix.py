f = "query-cosientist.md"
text = open(f, encoding="utf-8").read()
# The inserted line contains literal \u2013 / \u2014 / \u201387 / wrong chars
# Fix: only target the run225 evidence line to avoid touching other content.
start = text.find("falsify 2026-09-06 (第96回")
end = text.find("\n## Iteration log", start)
assert start != -1 and end != -1, "run225 line not found"
seg = text[start:end]
fixed = (seg
    .replace("\\u2013", "\u2013")
    .replace("\\u2014", "\u2014")
    .replace("帯确定", "帯確定")
    .replace("闇値", "閾値")
    .replace("浓度", "濃度")
)
text = text[:start] + fixed + text[end:]
open(f, "w", encoding="utf-8").write(text)
print("fixed")
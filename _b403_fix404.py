PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
doc = open(PATH, encoding='utf-8').read()
old = "に従い現時刻帯 23時台 帯初計測 (22時台 falsify run401 + bench run402 完了後の帯移行, 次 run ID run404)"
new = "に従い現時刻帯 23時台 n 積み増し (帯初計測は sibling falsify 第176回 run403 が実施済み, 本測は独立計測 run404)"
if old in doc:
    doc = doc.replace(old, new)
    open(PATH, 'w', encoding='utf-8').write(doc)
    print('fixed: %s' % 'OK')
else:
    print('fix target not found; leaving as-is')
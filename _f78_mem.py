content = """§
falsify K-Z3 測定 URL は必ず search.kotobase.net/search?q=test (K-Z3 標準)。kotobase.net/search は 404。2026-09-06 第78回で誤 URL 2 試行無効にした上、前 tick 第77回 run200 も 404 60/60 の無効測定と判明 — スクリプト新規作成時は過去 _f7*_run*.sh から URL をコピーする。実測後 5 分以内に fetch net-kotobase で push 反映を rev-parse 一致で確認する習慣も有効。
"""
with open('/Users/junkawasaki/.hermes/profiles/net-kotobase-falsify/memories/memory.md', 'a', encoding='utf-8') as f:
    f.write(content)
print('memory appended')

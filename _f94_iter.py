import io

path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')

# find "## Iteration log" header
hidx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        hidx = i
        break
if hidx is None:
    print('ITERLOG-HEADER-NOT-FOUND')
    raise SystemExit(1)

entry = (u"- 2026-09-06: falsify 第94回。16:16 JST tick。worktree HEAD c020215e = "
         u"fetch 後 net-kotobase/main 先端一致 (乖離 0)。rank 第90回/bench 第91回 NEXT "
         u"(「cacao_b64 harness / K-Z3 現在時刻帯」) 取込み — cacao_b64 は cosientist "
         u"実装担当のため実施範囲外。live smoke 200 (/, /signup; pre-run 計測)。"
         u"host load1 8.19 (16:15 実測, gate 7.5 超過) のため local 測定は拒否。"
         u"フォールバック (production HTTP 実測, gate 外): K-Z3 16時台 n 積み増し "
         u"run223A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 16:16 JST, "
         u"全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
         u"cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run223A 6番目の単発 1.142s "
         u"(散発型, B/C 0/20 で即消失) p50 42.7ms, run223B/C 0/20 (p50 41.4/46.0ms), "
         u"control (kotobase.net/signup) cold 0/20 p50 53.9ms max 257ms 静穏で "
         u"control 分離成立、cold 群は search 側に局在。run222A 型 (1.182s 冒頭単発) の "
         u"7 分後に同じ「帯内 1 窓即消失」弱単発が再現、16時台は run221(0/60)+run222(1/60)+"
         u"本 tick(1/60) で 180 試行中 2 試行 (~1.1%) の低位帯サンプル継続。"
         u"status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
         u"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 "
         u"n 積み増し継続 — 16時台 n 積み増し 2 セット済みのため次の観測枠は 17時台帯)。")

# insert right after the header
lines.insert(hidx + 1, entry)

open(path, 'w', encoding='utf-8').write('\n'.join(lines))
print('ITERLOG-ENTRY-INSERTED at', hidx + 2)
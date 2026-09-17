import io
path = 'query-cosientist.md'
text = open(path, encoding='utf-8').read()
anchor = '8時台通算 run195+run196 で 2/120 (~1.7%) 低位帯'
i = text.find(anchor)
if i < 0:
    raise SystemExit('anchor not found')
insert = (' falsify 2026-09-06 (第78回, K-Z3 9時台帯初計測 run201A–C, 同測定法 n=20 × 3 + landing control, '
          '別接続 curl, Tokyo, 09:28:42–09:29:03 JST, 全 80/80 200, host load1 14–15 (gate 7.5 超過) は '
          'production HTTP 実測のため gate 外): run201A cold(>=0.5s) 1/20 (0.987s, 6番目の単発) p50 47ms / '
          'run201B cold 0/20 p50 44ms / run201C cold 0/20 p50 45ms — landing control (kotobase.net/signup, '
          '同時刻, n=20, 全 200) は cold 0/20 p50 58ms max 117ms と静穏で control 分離成立、cold 群は search 側に局在。'
          '9時台は帯初計測で cold 1/60 単発 (run100A/116A/161A/192A 型「帯内 1 窓即消失」パターンと整合)。'
          '※本 tick 最初の 2 試行 (_f78_run201_out.txt, _f78_run201b_out.txt) は URL を誤り '
          'kotobase.net/search (404 応答, 60/60) を叩いたため無効 — 正 endpoint は '
          'search.kotobase.net/search?q=test で再実施したのが本計測。前 tick falsify 第77回 run200 も同様に '
          '404 (60/60) の無効測定の可能性大 ( Kotobase.com 運営者への K-Z3 9時台再計測推奨)。'
          'status 判定は rank に委ねる (rank 専門)。')
text = text[:i] + insert + text[i:]
open(path, 'w', encoding='utf-8').write(text)
print('appended ok, new size:', len(text))

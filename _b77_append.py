import re
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(p).read().split('\n')
ev = (" bench 2026-09-06 (第77回, K-Z3 8時台 n 積み増し run199A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 08:39–08:39:50 JST, 全 80/80 200, host load1 18–20 (gate 7.5 超過 tick) は "
      "production HTTP 実測のため gate 外): run199A cold(>=0.507s) 1/20 (0.877s 単発, 6番目) p50 44ms / "
      "run199B cold 0/20 p50 42ms / run199C cold 0/20 p50 38ms — landing control (kotobase.net/signup, 同時刻, "
      "n=20, 全 200) は cold 0/20 p50 41ms max 234ms と静穏で control 分離成立。cold 1/60 単発は "
      "run195/196 (falsify, 各 1/60) と同型。本 tick warm p50 (38–44ms) は静穏帯水準で run194–197 の "
      "host load 高騰 tick 上振れとは対照的 — latency 絶対値も分離傾向。8時台通算 run195+196+197+199 で "
      "3/240 (~1.3%) 低位帯。run186A 型群発は継続非再現。status 判定は rank に委ねる (rank 専門)。")
idx = 206  # line 207 (1-indexed)
assert lines[idx].startswith('| K-Z3 |'), lines[idx][:40]
lines[idx] = lines[idx] + ev
open(p, 'w').write('\n'.join(lines))
print('appended, line len', len(lines[idx]))

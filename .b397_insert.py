# -*- coding: utf-8 -*-
# Append bench 第178回 run397 evidence to K-Z3 evidence column (L279 tail).
path = "query-cosientist.md"
data = open(path, encoding="utf-8").read()
lines = data.split("\n")
assert lines[278].startswith("| K-Z3 | worker |"), "L279 is not K-Z3 row"
anchor = "andら"  # placeholder, replaced below
# We append at the end of line 279 (index 278), before its newline.
# The line currently ends with the falsify 第169回 run395 evidence entry "...status 判定は rank に委ねる (rank 専門)。"
# We insert a space + new bench evidence right after that tail.
tail_marker = "深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"
assert lines[278].endswith(tail_marker), "L279 tail anchor mismatch"
ev = (" bench 2026-09-07 (第178回, K-Z3 21時台帯初計測 run397A–C — rank 第169回 NEXT"
      "「K-Z3 21hr band-first run397」 の run397 枠を本 tick 実施 (現時刻帯 21時台 への帯移行後の帯初計測,"
      " 次 run ID は rank 第169回が run397 指定), 同測定法 n=20 × 3 + landing control, 別接続 curl,"
      " cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 21:11:27–21:11:45 JST,"
      " 全 80/80 200, host load1 35.7–39.0 (21:11 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測"
      " のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/1/2 per 20 = 3/60 (~5.0%)"
      " — run397A cold 0/20 p50 0.076s (0.047–0.206s) / run397B cold 単発 1/20 (1.1255s pos1 冒頭) p50 0.060s"
      " / run397C cold 2/20 (0.5752s pos15 / 0.9290s pos19 中盤〜末尾散発) p50 0.119s, control"
      " (kotobase.net/signup) cold 1/20 (0.5023s — 閾値ぎりぎり境界値 1 件) p50 0.120s max 0.502s"
      " で control に cold 1 件が出現し control 分離は borderline not-separated 傾向"
      " (search 側 cold 3/60 のうち run397B pos1 1.13s / run397C pos19 0.93s は閾値決定的だが,"
      " control 境界 0.50s + host load 35-39 high tick の p50 上振れ込みで機構判定としては弱い)。"
      " run397B 冒頭単発 + C 中盤〜末尾散発ペアは「帯内 1 窓即消失」散発単発/ペア型の続行"
      " (20時台 run396A 冒頭集中 3/20 (20:58) の 13 分後は B/C 散発減弱方向, heavy>=6/20 再達せず)。"
      " 21時台 (9/7) 帯初計測 cold 3/60 (~5.0%) — 20時台 (20/360 ~5.6% 6-set)・19hr (~8.0%) と同水準の"
      " 中位〜低位帯候補, 日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。"
      " 帯初 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する (not-separated-leaning のため"
      " 追加 clean-tick n 推奨)。status 判定は rank に委ねる (rank 専門)。")
lines[278] = lines[278] + ev
open(path, "w", encoding="utf-8").write("\n".join(lines))
print("appended ok, new L279 len:", len(lines[278]))
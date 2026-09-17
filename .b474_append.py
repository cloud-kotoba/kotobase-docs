#!/usr/bin/env python3
# Append run474 evidence to line 404 (1-indexed) end of query-cosientist.md
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
ev = (" falsify 2026-09-08 (第213回, K-Z3 14時台 n 積み増し run474A–C — bench 第197回 NEXT「委ねる (rank 指定優先; "
      "フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run474)」の run474 枠, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:51–14:52 JST, 全 80/80 200, "
      "host load1 106.25→90 (14:45→14:5x uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — "
      "curl + python stats のみ): cold(>=0.5s) 2/0/1 per 20 = 3/60 (~5.0%) — run474A 散発 2/20 (pos2 1.8646s / pos12 1.0389s) "
      "p50 147.9ms max 1864.6ms / run474B cold 0/20 p50 107.6ms max 367.5ms / run474C 単発 1/20 (pos9 1.6205s) p50 145.7ms max 1620.5ms, "
      "control (kotobase.net/signup) cold 1/20 (pos14 0.5409s — threshold ぎりぎりの境界値) p50 144.7ms max 540.9ms — control 境界 1 件で"
      "完全静穏不成立 borderline not-separated-leaning 注記 (search cold 3/60 が 1.04–1.86s で threshold 決定的, search/control とも http200 80/80). "
      "run474A/C 散発 3/60 は B 0/20 + control 境界 1 件で「帯内 1 窓即消失」型継続 (run473A heavy 6/20 (14:45) の 6 分後散発減弱 — 14時台初 heavy は"
      "帯内持続せず単一窓即消失, heavy>=6/20 の帯水準持続は 4 セットで未確認のまま)。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + bench run471 (1/60) "
      "+ bench run472 (5/60) + bench run473 (8/60) + 本 tick run474 (3/60) = 22/300 (~7.3%) の 5 セット中位帯候補 — 帯初 5/60 → 1/60 → 5/60 → 8/60 (heavy 再上振れ) "
      "→ 3/60 の振幅、日中帯セット間変動大継続 (traffic 依存説の日中帯方向支持継続, 深夜帯 ~26–31% 平坦パターンとの対比不変)。"
      "本 tick control borderline 1 件 + host load 高騰混入は note として rank 判定に委ねる。status 判定は rank に委ねる (rank 専門)。")
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
idx = 403  # 0-indexed line 404
assert lines[idx].rstrip().endswith("(rank 専門)。"), "anchor mismatch: " + repr(lines[idx][-40:])
lines[idx] = lines[idx].rstrip() + ev
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("append done, new len404", len(lines[idx]))
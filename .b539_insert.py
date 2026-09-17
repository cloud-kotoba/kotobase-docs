# -*- coding: utf-8 -*-
import io

QC = "/tmp/qc_head.md"

ev = (u" bench 2026-09-09 (第244回, K-Z3 9時台 帯初計測 run539A-C - "
      u"iter-log HEAD (bench 第243回 NEXT 委ねる - フォールバック 現在時刻帯 n 積み増し続行 次 run ID run538) に対し "
      u"run538 枠は in-flight sibling (falsify/cosientist) が同一プレフィクス .b538_ で同時実行中で .raw が cross-append (n=40) したため "
      u"run539 に読替 (run216/256/263 precedent), 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, "
      u"nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 09:12:57-09:13:05 JST, 全 80/80 200, "
      u"host load1 20.94 (09:12 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
      u"cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run539A cold 0/20 p50 0.0585s max 0.1997s / "
      u"run539B cold 0/20 p50 0.0505s max 0.1535s / run539C cold 0/20 p50 0.0488s max 0.1496s, "
      u"control (kotobase.net/signup) cold 0/20 p50 0.0436s max 0.2869s 完全静穏で control 分離成立 (search/control とも 0 cold)。"
      u"9時台 (9/9) 帯初 = 0/60 完全静穏 - 6時台 (3/300 ~1.0% 9/8) 5時台 (5/180 ~2.8%) 朝帯に続く静穏低位帯候補方向で "
      u"K-Z3 traffic 依存説への強反証材料なし (深夜帯 ~26-31% 平坦パターンとの対比不変)。帯水準確定・機構判断には未達 "
      u"(K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。")

iter_entry = (u"- 2026-09-09: bench 第244回。09:12 JST tick。HEAD b7c7452 = bench 第243回 (05:25, K-Z3 5時台 run537 cold 3/60) "
              u"= remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; detached HEAD のため fetch 系で取込; "
              u"terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT 委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。 は stale (rank 帯 artifact) - "
              u"true progressive NEXT は iter-log HEAD 連鎖 (bench 第243回 NEXT 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run538 使用))。"
              u"本 tick は 09:12 現時刻帯 9時台 n 積み増し/帯初計測。run538 枠は in-flight sibling が .b538_ 同一プレフィクスで併走中で "
              u".raw cross-append (n=40) を検出したため run539 に読替 (run216/256/263 precedent)。live smoke 200 (/, /signup; pre-run + 本 tick 実測 200)。"
              u"host load1 20.94 (09:12 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。"
              u"K-Z3 9時台 帯初計測 run539A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
              u"正 endpoint search.kotobase.net/search?q=test, 09:12:57-09:13:05 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
              u"cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run539A cold 0/20 p50 0.0585s max 0.1997s / "
              u"run539B cold 0/20 p50 0.0505s max 0.1535s / run539C cold 0/20 p50 0.0488s max 0.1496s, "
              u"control (kotobase.net/signup) cold 0/20 p50 0.0436s max 0.2869s 完全静穏で control 分離成立 (search/control とも 0 cold)。"
              u"9時台 (9/9) 帯初 0/60 完全静穏 - 5時台 (5/180 ~2.8%) から 6/7/8時台 記録なしを挟み 9時台 帯初完全静穏、"
              u"朝帯静穏低位帯候補方向に整合し K-Z3 traffic 依存説への強反証材料なし。帯水準確定・機構判断には未達 "
              u"(K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
              u"secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し続行, "
              u"次 run ID は run540 使用 - run538 は in-flight sibling 消費, run539 は本 tick 消費のため次セットは run540)。")

lines = io.open(QC, encoding="utf-8").read().split("\n")

# 1) K-Z3 evidence row append
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        kz3_idx = i
        break
if kz3_idx is None:
    raise SystemExit("K-Z3 row not found")
lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + ev

# 2) iter-log entry insert right after '## Iteration log' header (newest first)
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    raise SystemExit("Iteration log header not found")
lines.insert(hdr_idx + 1, iter_entry)

io.open(QC, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print("kz3_idx=%d hdr_idx=%d ok" % (kz3_idx, hdr_idx))
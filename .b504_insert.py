#!/usr/bin/env python3
# falsify 224: append run504 evidence to K-Z3 row (L279) + insert iter-log entry at top
import io

FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(FN, "r", encoding="utf-8") as f:
    content = f.read()

def scrub(s):
    # remove zero-width / BOM / weird control chars that have corrupted prior edits
    return "".join(ch for ch in s if ch not in ("\u200b", "\u200c", "\u200d", "\ufeff", "\u202a", "\u202b", "\u202c", "\u202d", "\u202e"))

lines = content.split("\n")

# ---- locate K-Z3 row ----
kz_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        kz_idx = i
        break
assert kz_idx is not None, "K-Z3 row not found"

# ---- locate Iteration log header ----
il_header = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        il_header = i
        break
assert il_header is not None, "Iteration log header not found"

EV = ("  falsify 2026-09-08 (第224回, K-Z3 21時台帯初計測 run504A-C - 最新 NEXT (base 7900a8f = bench 220 run503 の"
      "「委ねる -> フォールバック 現時刻帯 n 積み増し, 次 run ID run504」, cron 時刻 21:16 が 21時台, pre-run monitor NEXT「23時台」は stale (rank 帯 artifact) 前例多)。"
      "同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 21:16:24-21:16:48 JST, 全 80/80 200, "
      "host load1 28.7 (21:09 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
      "cold(>=0.5s) 8/0/1 per 20 = 9/60 (~15.0%) - run504A heavy クラスタ 8/20 (pos1-4 連続 1.1761/1.3374/1.3995/2.7015s + pos6/7 1.2273/1.4457s + pos15/16 1.6282/2.1356s, 冒頭+中盤+後半 3 簇, deep 2.70s) p50 148.8ms max 2.7015s "
      "/ run504B 0/20 p50 49.6ms max 143.3ms / run504C 単発 1/20 (pos20 1.8672s) p50 53.7ms - control (kotobase.net/signup) cold 1/20 境界値 (pos17 0.5508s, 閾値 0.5s の僅か越境) p50 51.4ms で完全静穏分離は不成立 (control 境界 1 件) 注記 - "
      "ただし search 側 cold 9/60 は run504A heavy 8/20 (deep 2.70s) が主体で search 局在強信号, control 境界 1 件は検出/分離を大きく損なわない。"
      "run504A heavy 8/20 = 日中 high 帯 (17時台 run487A 7/20 / 18時台系) 級の strong 再現で, 晩側 (19時台 ~3.8% / 20時台 ~5.0%) からの 21時台急上昇 = 帯内短時間スケール変動の夜帯遷移側での再発 (K-Z3 traffic 依存説の日中/夜帯いずれでも帯内突発の方向支持)。"
      "21時台 (9/8) 帯初 n=1 セットのため帯水準確定には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

IL = ("- 2026-09-08: falsify 第224回。21:16 JST tick。HEAD 7900a8f = bench 第220回 (20:54, K-Z3 20時台 run503 cold 3/60 ~5.0%; NEXT 委ねる -> フォールバック 現時刻帯, 次 run ID run504) = "
      "remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由)。"
      "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (bench 第220回 NEXT 委ねる -> フォールバック K-Z3 現時刻帯 n 積み増し, 次 run ID run504)。"
      "host load1 28.7 (21:09 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; pre-run 計測)。"
      "K-Z3 21時台帯初計測 run504A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 21:16:24-21:16:48 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
      "cold(>=0.5s) 9/60 (~15.0%) - run504A heavy クラスタ 8/20 (pos1-4 連続 1.1761/1.3374/1.3995/2.7015s + pos6/7 1.2273/1.4457s + pos15/16 1.6282/2.1356s, deep 2.70s) p50 148.8ms / run504B 0/20 p50 49.6ms / "
      "run504C 単発 1/20 (pos20 1.8672s) p50 53.7ms, control (kotobase.net/signup) cold 1/20 境界値 (pos17 0.5508s) p50 51.4ms で完全静穏分離は不成立 (control 境界 1 件) 注記 - search 側 cold 9/60 は run504A heavy 8/20 が主体で search 局在強信号。"
      "21時台 (9/8) 帯初計測 cold 9/60 ~15.0% は晩側 (19時台 ~3.8% / 20時台 ~5.0%) から急上昇し日中 high 帯 (17-18時台 ~9-17%) 級の heavy クラスタ (run504A 8/20 deep) 再現 = 帯内短時間スケール変動の夜帯遷移側での再発 (traffic 依存説の日中/夜帯いずれでも帯内突発支持)。"
      "帯初 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。"
      "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行, 次 run ID は run505 使用)。")

EV = scrub(EV)
IL = scrub(IL)

# append evidence to K-Z3 row end
lines[kz_idx] = lines[kz_idx] + EV

# insert iter-log entry as the newest (right after header)
lines.insert(il_header + 1, IL)

new_content = "\n".join(lines)
with io.open(FN, "w", encoding="utf-8") as f:
    f.write(new_content)

print("K_Z3_IDX", kz_idx + 1)
print("IL_HEADER_IDX", il_header + 1)
print("EV_LEN", len(EV))
print("IL_LEN", len(IL))
print("DONE")
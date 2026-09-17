import io
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
p = base + "/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
# find "## Iteration log" line index
idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        idx = i
        break
assert idx is not None, "iter log header not found"
entry = (
 "- 2026-09-08: falsify 第217回。17:14 JST tick。HEAD 3cdeb89 = bench 第210回 (16:54, K-Z3 16時台 run484 cold 2/60; NEXT run485) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第210回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 17時台 n 積み増し, 次 run ID は run485))。run484 は bench 第210回 が 16時台に使用済みのため本 tick (17時台) は run485 に読替 (定例 run216/256/263/278)、17時台帯初計測として実施。K-Z3 17時台 run485A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:14–17:16 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10.0%), control cold 2/20 (borderline not-separated 傾向)。17時台 (9/8) 帯初計測 cold 6/60 (~10.0%) — 16時台通算 (27/360 ~7.5% 6set) に続く日中帯 high 側の帯初再上振れ、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。host load1 115.75 (17:14 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。live smoke 200 (/, /signup; pre-run)。control 分離 borderline + host load 高騰混入で帯水準確定・機構判断は未達 (rank 追加 n 要)。status 判定は rank 専門。secret 不含。詳細は K-Z3 evidence 欄 (L279 末尾) に追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し続行, 次 run ID は run486)。"
)
entry = entry.replace("\r", " ")
entry = entry.replace("\n", " X")
clean = []
for ch in entry:
    cp = ord(ch)
    if 0x200B <= cp <= 0x200F:
        continue
    if ch in "\x0b\x0c":
        continue
    clean.append(ch)
entry = "".join(clean) + "\n"
lines.insert(idx + 1, entry)
with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted iter-log at physical line", idx + 2)
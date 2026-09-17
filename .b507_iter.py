#!/usr/bin/env python3
# Insert falsify 第225回 iteration-log line after "## Iteration log" header (line 406)
import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# locate header
hdr_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "Iteration log header not found"
# next line must currently be the bench 第222回 line (newest); we insert above it
assert "bench 第222回" in lines[hdr_idx + 1], "expected bench 第222回 on next line, got: " + lines[hdr_idx + 1][:60]
# guard against dup
assert "falsify 第225回" not in lines[hdr_idx + 1], "already present"

NEW = ("- 2026-09-08: falsify 第225回。21:51 JST tick。HEAD b20c76a = bench 第222回 "
       "(21:42, K-Z3 21時台 run506 cold 4/60 ~6.7%; NEXT 委ねる -> フォールバック K-Z3 現在時刻帯 "
       "21時台 n 積み増し続行, 次 run ID は run507 使用) = remote net-kotobase/main 一致 "
       "(git fetch + rev-parse 比較 乖離 0; detached HEAD のため fetch 系で取込; terminal foreground "
       "stdout 空=既知のため状態確認・計測出力はファイル書出経由; worktree doc clean + run507 未使用 "
       "確認済 (HEAD の run507 出現は bench 第222回 NEXT「次 run ID は run507 使用」の未来参照のみで "
       "実測 commit なし - run507 枠を本 tick 実施))。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 "
       "23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD "
       "連鎖 (bench 第222回 NEXT 委ねる -> フォールバック K-Z3 現在時刻帯 21時台 n 積み増し, 次 run "
       "ID run507)。host load1 35.89 (21:51 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測の "
       "ため gate 外で実施。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 "
       "200)。K-Z3 21時台 n 積み増し run507A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 "
       "curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
       "21:51:10-21:51:27 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
       "cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) - run507A 冒頭隣接クラスタ 3/20 (pos2 1.2281s / pos3 "
       "1.1090s / pos5 1.6492s) p50 128.0ms / run507B 単発 1/20 (pos12 1.1857s) p50 99.1ms / run507C "
       "0/20 p50 82.1ms, control (kotobase.net/signup) cold 0/20 p50 100.1ms max 166.2ms 完全静穏で "
       "control 分離成立, cold 群 search 側局在。21時台 (9/8) 通算 = run504 (9/60) + run505 (9/60) + "
       "run506 (4/60) + run507 (4/60) = 26/240 (~10.8%) 4 セット - 晩側 (19時台 ~3.8% / 20時台 ~5.0%) "
       "からの帯初急上昇 (run504A heavy 8/20) 後の散発減衰続行 (run506 4/60 + 本 tick 4/60), heavy>=6/20 "
       "の帯水準持続は非再現で散発型尾引き, traffic 依存説の晩側トランジション帯方向支持継続。p50 "
       "上振れ (search/control とも ~80-130ms) は host load 35 の全体的上振れ borderline 注記付き, "
       "cold 4 件 1.109-1.649s 閾値決定的。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 "
       "evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバック "
       "は K-Z3 現在時刻帯 21時台 n 積み増し続行, 次 run ID は run508 使用)。\n")

lines.insert(hdr_idx + 1, NEW)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()
sys.stdout.write("iter_225_count=%d\n" % txt.count("falsify 第225回"))
sys.stdout.write("run507_count=%d\n" % txt.count("run507"))
sys.stdout.write("run508_count=%d\n" % txt.count("run508"))
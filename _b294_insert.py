#!/usr/bin/env python3
import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- locate Iteration log header ---
hl_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        hl_idx = i
        break
assert hl_idx is not None, "Iteration log header not found"

# --- K-Z3 evidence: insert before the blank line preceding the header ---
kz3_evidence = (
    "bench 2026-09-07 (第121回, K-Z3 3時台(深夜帯) n 積み増し run294A\u2013C"
    " \u2014 rank 第129回 NEXT\u300C K-Z3 3時台(現時刻帯) n 積み増し継続"
    " (次 run ID は run294 使用)\u300D の run294 枠として実施, 同測定法 n=20 \u00d7 3"
    " + landing control, 別接続 curl, Tokyo, 03:23:02\u201303:23:09 JST, 全 80/80 200,"
    " 正 endpoint search.kotobase.net/search?q=test, host load1 25.89 (03:23 uptime 実測,"
    " gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl のみ):"
    " cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%)"
    " \u2014 run294A cold 2/20 (1.5302s 3番目 / 0.8765s 8番目 \u2014 冒頭+中盤散発,"
    " warm 群 0.034\u20130.068s と交互) p50 44.1ms"
    " / run294B cold 0/20 p50 41.4ms max 63.8ms"
    " / run294C cold 0/20 p50 39.2ms max 47.6ms,"
    " control (kotobase.net/signup) cold 0/20 p50 39.2ms max 47.6ms 完全静穏で"
    " control 分離成立、cold 群は search 側に局在。run294A 散発 2/20 は B/C 0/20"
    " + control 0/20 で即消失し\u300C帯内 1 窓即消失\u300D散発型継続"
    " (run292A 単発 1/20 \u2192 本 tick 2/20, heavy クラスタは run271A 以降 21 セット非再現)。"
    " 3時台通算 (falsify run291 2/60 + COD run292 1/60 + falsify run293 0/60 + 本 tick 2/60)"
    " = 5/240 (~2.1%) の 4 セット、deep-night 累計 run275..294 = 27/1260 (~2.1%) の 21 セットで"
    " 低位帯水準継続 \u2014 深夜最低帯 (traffic 最低) での cold 散発再出現"
    " (falsify run293 完全静穏 0/60 の直後の 2 件再出現) は K-Z3 traffic 依存説への"
    " 反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
    " ただし帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる"
    " (rank 専門)。\n".replace("COD run292", "bench run292")
)

# insert before the blank line (hl_idx-1 currently blank). Place evidence line there.
kz3_insert_pos = hl_idx - 1  # position of the blank line separating cell from header
# sanity: the line we insert before should be blank
assert lines[kz3_insert_pos].strip() == "", "expected blank separator before Iteration log"
lines.insert(kz3_insert_pos, kz3_evidence)

# --- Iteration log entry: insert right after header ---
iter_entry = (
    "- 2026-09-07: bench 第121回。03:22 JST tick。HEAD f86a4aa = rank 第129回"
    " (run293 まで fold) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0;"
    " worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み;"
    " 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力を"
    " ファイル書き出し経由で確認)。live smoke 200 (/, /signup; pre-run 計測)。"
    " host load1 30.26 (03:22 pre-run uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し"
    " production HTTP フォールバック (gate 外)。rank 第129回 NEXT"
    "\u300C K-Z3 3時台(現時刻帯) n 積み増し継続 (次 run ID は run294 使用)\u300D の"
    " 現時刻帯フォールバック継続として 3時台 n 積み増し run294A\u2013C を実施"
    " (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, 03:23:02\u201303:23:09 JST,"
    " 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test):"
    " cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%)"
    " \u2014 run294A cold 2/20 (1.5302s / 0.8765s 散発) p50 0.0441s"
    " / run294B 0/20 p50 0.0414s / run294C 0/20 p50 0.0392s,"
    " control (kotobase.net/signup) cold 0/20 p50 0.0392s max 0.0476s 完全静穏で"
    " control 分離成立、cold 群は search 側に局在。run294A 散発 2/20 は B/C 0/20 で即消失し"
    "\u300C帯内 1 窓即消失\u300D散発型継続 (falsify run293 完全静穏 0/60 の直後の 2 件再出現)。"
    " 3時台通算 (falsify run291 2/60 + bench run292 1/60 + falsify run293 0/60 + 本 tick 2/60)"
    " = 5/240 (~2.1%) の 4 セット、deep-night 累計 run275..294 = 27/1260 (~2.1%) の 21 セットで"
    " 低位帯水準継続 \u2014 深夜最低帯での cold 散発再出現は K-Z3 traffic 依存説への"
    " 反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 遷移なし (rank 専門)。"
    " secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは"
    " K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run295 使用)。\n"
)
iter_insert_pos = hl_idx + 1  # right after "## Iteration log\n"
lines.insert(iter_insert_pos, iter_entry)

with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted OK; total lines now", len(lines))
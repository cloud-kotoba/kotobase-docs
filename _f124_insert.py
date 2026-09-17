import io

FN = "query-cosientist.md"

# Evidence row insertion: after falsify run270 evidence line (K-Z3 row)
EVID_ANCHOR = "falsify 2026-09-07 (第123回, K-Z3 24時台(0時台) n 積み増し run270A-C"
NEW_EVID = ("falsify 2026-09-07 (第124回, K-Z3 24時台(0時台) n 積み増し run271A-C - rank 第118回 NEXT "
       "「K-Z3 24時台(0時台) n 積み増し継続 (次 run ID は run271 使用)」の run271 枠として実施, "
       "同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 00:31:10 JST, 全 80/80 200, "
       "正 endpoint search.kotobase.net/search?q=test, host load1 24.61 (00:31 uptime 実測, "
       "gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl のみ): "
       "cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) - run271A heavy 散発クラスタ 6/20 "
       "(0.9385/1.0773/1.1442/1.1642/1.5370/1.8709s 散発配置 冒頭+中盤, warm 群と交互) "
       "p50 0.054s warm_p50 0.043s / run271B cold 1/20 (1.2019s 単発) p50 0.045s max 1.202s / "
       "run271C cold 0/20 p50 0.047s max 0.066s, control (kotobase.net/signup) cold 0/20 "
       "p50 0.042s max 0.332s (0.33s 単発 1 件は閾値未満) 完全静穏で control 分離成立、cold 群は "
       "search 側に局在。run271A cold 6/20 は B/C 0/20 即消失で「帯内 1 窓即消失」heavy 寄り散発"
       "クラスタの再上振れ (run269A 3/20 → run270A 1/20 の散発減弱から再上昇, run260A 8/20 / "
       "run263A 5/20 / run267A 5/20 型 heavy の弱い再現)。24時台総 = falsify run268 (2/60) + "
       "bench run269 (3/60) + falsify run270 (1/60) + 本 tick run271 (7/60) = 13/240 (~5.4%) で "
       "4 セット連続 cold>0 - 深夜帯 24/0時台 (traffic 最低帯) での heavy クラスタ再上振れを含む "
       "cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合"
       "方向)。ただし全セット「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。"
       "status 判定は rank に委ねる (rank 専門)。"
       )

# Timeline insertion: new falsify 124 entry inserted BEFORE falsify 123 timeline line
TL_ANCHOR = "- 2026-09-07: falsify 第123回。00:15 JST tick"
NEW_TL = ("- 2026-09-07: falsify 第124回。00:31 JST tick。worktree detached HEAD (HEAD 82274f7 = "
       "net-kotobase/main 先端一致, fetch net-kotobase + rev-parse 比較で確認, 乖離 0)。live smoke "
       "200 (/, /signup; pre-run 計測)。host load1 24.61 (00:31 uptime 実測, gate 7.5 大幅超過) "
       "のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第118回 NEXT"
       "「K-Z3 24時台(0時台) n 積み増し継続...次 run ID は run271 使用」に従い 現時刻帯 0時台"
       "(24時台) n 積み増し run271A-C を実施 (同測定法 n=20 x 3 + landing control, 別接続 curl, "
       "00:31:10 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
       "cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) - run271A heavy 散発クラスタ 6/20 "
       "(0.9385/1.0773/1.1442/1.1642/1.5370/1.8709s 散発配置), run271B 単発 1.2019s, run271C 0/20, "
       "control cold 0/20 p50 0.042s max 0.332s 完全静穏で control 分離成立、cold 群は search 側に"
       "局在。run271A heavy 6/20 は B/C 0/20 即消失で「帯内 1 窓即消失」heavy 寄り散発クラスタの"
       "再上振れ (run269A 3/20 → run270A 1/20 の散発減弱から再上昇)、24時台総 13/240 (~5.4%) の "
       "4 セット連続 cold>0 で K-Z3 traffic 依存説への反証材料を継続。status 遷移なし (rank 専門)。"
       "secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; "
       "フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run272 使用)。"
       )

with io.open(FN, "r", encoding="utf-8") as f:
    lines = f.readlines()

# --- evidence row insert ---
ev_idx = None
for i, ln in enumerate(lines):
    if ln.startswith(EVID_ANCHOR):
        ev_idx = i
        break
assert ev_idx is not None, "evidence anchor not found"
assert (ev_idx + 1) < len(lines)
lines = lines[:ev_idx+1] + [NEW_EVID + "\n"] + lines[ev_idx+1:]

# --- timeline insert: before falsify 123 ---
tl_idx = None
for i, ln in enumerate(lines):
    if ln.startswith(TL_ANCHOR):
        tl_idx = i
        break
assert tl_idx is not None, "timeline anchor not found"
lines = lines[:tl_idx] + [NEW_TL + "\n"] + lines[tl_idx:]

with io.open(FN, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("evidence inserted after line", ev_idx+1)
print("timeline inserted before line", tl_idx+1)
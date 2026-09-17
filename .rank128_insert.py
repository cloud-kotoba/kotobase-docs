import sys

path = "query-cosientist.md"
anchor = "- 2026-09-07: rank 第127回。"

new_entry = (
    "- 2026-09-07: rank 第128回。03:03 JST tick。HEAD e721f9c = falsify 第133回 (run291A-C, 3時台(深夜帯) 帯初計測, 03:01-03:02, 2hr 帯 n-add 継続から 3時台へ帯移行) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力をファイル書き出し経由で確認)。rank 第127回 (69b9dd6, 02:57, run290 まで fold) 以降の新規確定 evidence は 1 commit: falsify 第133回 run291A-C (e721f9c, 03:01-03:02, 3時台 帯初計測, cold(>=0.5s) 1/1/0 per 20 = 2/60 ~3.3% — run291A 単発散発 0.9367s (9番目) / run291B 単発散発 1.6194s (13番目), C 0/20 即消失, control (kotobase.net/signup) cold 0/20 p50 0.0423s max 0.0551s 完全静穏で control 分離成立, cold 群は search 側に局在, host load1 20.99 は production HTTP 実測のため gate 外)。取り込み判定: (a) K-Z3: run291 を取込、3時台は帯初計測 cold 2/60 (~3.3%) — 帯初 1 セットのみで帯水準確定・機構判断には未達 (追加 n 継続)。deep-night 累計 run275..291 = 24/1080 (~2.2%) の 18 セットで低位帯水準継続。run291A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy クラスタ run271A 6/20 型は run271A 以降 18 セット連続非再現)。3時台帯初 ~3.3% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%)・2時台 (9/480 ~1.9%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯 (24/0/1/2/3時台) での cold 散発継続は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 3時台帯初 2/60 は帯水準確定・機構判断に至らず)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・3時台帯初 2/60 ~3.3% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 3時台帯初 ~3.3% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 19.39-27.54 (03:02 uptime 実測, gate 7.5 超過) のため rank は測定を行わず状態正本の更新のみ。secret は一切記録せず。\n"
    "  NEXT: K-Z3 3時台(現時刻帯) n 積み増し継続 — 現時刻 03:03 は 3時台 (falsify 第133回 run291 が 3時台帯初計測済み, 次 run ID は run292)。3時台は帯初 n=1 セットのみ (run291 2/60 ~3.3%) で帯水準確定には 1-2 セット要 — 現時刻 3時台の間は 3時台 n 積み増し、時間帯移行後は次の帯初へ (深夜帯 ~26-31% 平坦パターンへの収束か 深夜各帯限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run292 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\n"
)

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

if anchor not in content:
    print("ANCHOR NOT FOUND", file=sys.stderr)
    sys.exit(1)

idx = content.index(anchor)
new_content = content[:idx] + new_entry + "\n" + content[idx:]

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("INSERTED OK")
print("new total lines:", new_content.count("\n"))
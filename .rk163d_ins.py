#!/usr/bin/env python3
# rank tick prepend - v4 (insert after the single iteration-log header)
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, "r", encoding="utf-8") as f:
    t = f.read()

hdr = "## Iteration log"
idx = t.find(hdr)
if idx < 0:
    raise SystemExit("HDR NOT FOUND")
end = idx + len(hdr) + 1  # +1 to swallow the '\n' after the header

entry = ('- 2026-09-07: **rank  第163回**. ~18:40 JST tick\tHEAD e97c6dd = bench'
          '  第169回 (18:32, run383) = remote net-kotobase/main 【一致】(git fetch + rev-parse 比較,'
          '  乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため'
          '  状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load 大幅超過'
          '  (gate 7.5) — rank は測定せず状態正本のみで影響なし. ※pre-run monitor NEXT【K-Z3 深夜帯'
          '   23時台 n 積み増し継続】は stale (rank  第90回帯 artifact — 全 bot 共有判断済み) — true progressive'
          '   NEXT は iter-log HEAD(bench  第169回)【委ねる (rank 指定優先;フォールバックは K-Z3'
          '    現在時刻帯 18時台 n 積み増し続行,,次 run ID  は run384 使用】. rank   第162回'
          '   (4e66f3f, ~18:20) 以降の新規確定 evidence は 1 commitで、すべて K-Z3 18時台 n 積み増し:'
          '   bench   第169回 e97c6dd (run383A–C,    18:28, cold>=0.5s 3/3/1 per20 =  7/60'
          '   (~11.7%)—— run383A/B 各散発 3/20 + C 単発 1/20 (閾値越 1.0–1.5s 散発配置), control'
          '   【kotobase.net/signup】 0/20 完全静穏で分離成立, cold 群は search 側に局在; run381 2/60 + run382'
          '    4/60 の積み増しに続く続行で【帯内 1 窓即消失】散発単発/ペア型継続, heavy(>=6/20) は再達せず)।'
          '   取り込み判定: (a) K-Z3: bench169-run383 を取込,,18時台通算 = run381 (2/60) + run382 (4/60)'
          '   + 本 tick run383 (7/60) =13/180 (~7.2%) の 3 セット中位帯候補 — 17時台 (27/360'
          '   ~7.5%) と同水準の帯横断継続で、日中帯 traffic 依存説の方向支持継続,,深夜帯 ~26-31% 平坦'
          '   パターンとの対比不変; control 0/20 完全静穏で機構判定としては clean 方向 (帯水準確定は rank 追加'
          '   n に委ねる)。(b) K-Q1:変動なし — transact 401 静的切れ手は全棄却済み,残余は cosientist 実装'
          '   専任の動的切れ手 biscuit delegation-for-request 動的照合のみ (rank 測定指示対象外, KV read 内訳初実測'
          '   滞留継続,,最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし'
          '    (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準'
          '   確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち'
          '   仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 18時台 13/180'
          '   ~7.2% は順位を変えない)。secret は一切記録せず (curl のみ)。NEXT: K-Z3 18時台 n 積み増し'
          '   継続 (3 セット 13/180 ~7.2% 中位帯候補 — 実行時刻が 18時台内なら積み増し続行,,19時台移行後'
          '   は 19時台帯初計測へ;   次 run ID   は run384 使用, host load gate 超過時は production HTTP '
          '   フォールバックの従来手順) — K-Q1  は cosientist  実装専任のまま (rank 測定指示対象外)。')

t2 = t[:end] + entry + "\n" + t[end:]

if t2.count(hdr) != 1:
    raise SystemExit("HEADER COUNT NOT 1")
if "第163回" not in t2:
    raise SystemExit("ENTRY NOT FOUND")

with io.open(P, "w", encoding="utf-8") as f:
    f.write(t2)
print("OK inserted rank163")
import io

PATH = "query-cosientist.md"
with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()

# --- 1. rank header bump ---
old_hdr = "rank (期待 gain × 確率, 2026-09-06 第113回):"
new_hdr = "rank (期待 gain × 確率, 2026-09-06 第114回):"
assert txt.count(old_hdr) == 1, "hdr anchor count = %d" % txt.count(old_hdr)
txt = txt.replace(old_hdr, new_hdr)

# --- 2. append 23hr fold paragraph to K-Z3 item 3, before closing "( K-Q2 ... rank 外 )" ---
fold = (
    "\n第114回の 23時台 folds: falsify 第118回 run260A-C (23:05, 23時台帯初計測, "
    "cold 8/60 ~13.3% — run260A heavy 散発クラスタ 8/20 1.11-2.76s 散発配置, B/C 0/20 即消失, "
    "control cold 0/20 完全静穏で分離成立) + bench 第105回 run259A-C (23:09, 23時台 2 セット目 n 積み増し, "
    "cold 4/60 ~6.7% — run259A 冒頭散発 4/20 1.24-2.36s, B/C 0/20 即消失, control cold 0/20 静穏で分離成立, "
    "6 分前 run260A heavy の弱い再現) + falsify 第119回 run261A-C (23:15, 23時台 3 セット目 n 積み増し, "
    "cold 3/60 ~5.0% — run261A 冒頭隣接ペア 2/20 + C 単発 1, control cold 0/20 静穏で分離成立, "
    "host load 高騰の p50 上振れ込み borderline, cold 濃度決定的) を取込、23時台通算 = "
    "run260 (8/60) + run259 (4/60) + run261 (3/60) = 15/180 (~8.3%) の高位帯候補確定方向。"
    "深夜帯 23時台 (traffic 最低帯) で帯初計測から 3 セット連続 cold>0 (8/60 → 4/60 → 3/60 の重→軽減弱) が出現し、"
    "run232A/252A/260A 型 heavy クラスタの深夜帯への連続再現 (run260A 8/20) と散発減弱 (run259A/261A) の合成で "
    "K-Z3 traffic 依存説への反証材料として重みが増す (深夜帯 ~26-31% 平坦パターンと整合の方向)。"
    "ただし 3 セットとも「帯内 1 窓即消失」型 (B/C 0/20) で、深夜帯通算 cold>0 で帯区分算入した場合の "
    "深夜帯発現率への影響は小 — traffic 最低帯での発現継続と日中低温帯 (13-17時台 ~2-5%) との対比は "
    "時間帯非依存の突発 cold-start 説を支持方向 (機構判断は据え置き)。23時台通算 15/180 (~8.3%) は "
    "22時台 (~6.0%) よりやや高位で 深夜帯平坦パターン (~26-31%) への収束方向と整合。status: K-Z3 open 継続 "
    "(意味のある status 遷移を満たす決定的反証/支持 evidence には未達 — 23時台帯初 3 セットで heavy クラスタと "
    "散発減弱の混合であり帯水準確定には追加 n 要)。\n"
)
anchor = "\n( K-Q2 / K-W1 / K-W2 / K-Z1 は判定済みのため rank 外 )"
assert txt.count(anchor) == 1, "fold anchor count = %d" % txt.count(anchor)
txt = txt.replace(anchor, fold + anchor)

# --- 3. Iteration log entry at top ---
entry = (
    "- 2026-09-06: rank 第114回。23:17 JST tick。HEAD 7fa6a1a = remote net-kotobase/main 一致 "
    "(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み)。"
    "rank 第113回 (7f85ae5, 23:00) 以降の新規確定 evidence は 3 commit、いずれも K-Z3 23時台: "
    "(1) falsify 第118回 run260A-C (ecd28a8, 23:05, 23時台帯初計測, cold 8/60 ~13.3% — run260A heavy "
    "散発クラスタ 8/20, control 完全静穏分離成立), (2) bench 第105回 run259A-C (7fa6a1a, 23:09, "
    "23時台 2 セット目 n 積み増し, cold 4/60 ~6.7% — run259A 冒頭散発, control 分離成立, run260A の弱い再現), "
    "(3) falsify 第119回 run261A-C (23:15, 23時台 3 セット目 n 積み増し, cold 3/60 ~5.0% — run261A ペア + C 単発, "
    "control 分離成立)。取り込み判定: (a) K-Z3: run260/run259/run261 を取込 23時台通算 = 8+4+3 = 15/180 (~8.3%) の "
    "高位帯候補確定方向。深夜帯 23時台 (traffic 最低帯) で帯初から 3 セット連続 cold>0 が出現 (重→軽減弱) し、"
    "run260A 8/20 heavy クラスタが run232A/252A 型の深夜帯再現、その後散発減弱 — K-Z3 traffic 依存説への反証材料継続 "
    "(深夜帯 ~26-31% 平坦パターンと整合方向)、日中低温帯 (13-17時台 ~2-5%) との対比で時間帯非依存 cold-start 説を "
    "弱く支持 (機構判断は据え置き)。23時台通算 ~8.3% は 22時台 ~6.0% よりやや高位で深夜帯収束方向と整合。"
    "(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の "
    "動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。"
    "(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: "
    "K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・23時台 15/180 ~8.3% は時台帯初 3 セットで帯水準確定・機構判断に "
    "至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
    "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 23時台 15/180 ~8.3% は順位を変えない)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 26.01/36.15/40.76 (23:17 uptime 実測, gate 7.5 超過) — "
    "rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。"
    "  NEXT: K-Z3 23時台 n 積み増し継続 — 23時台は帯初計測 3 セットで 15/180 (~8.3%) の高位帯候補 (run260A heavy "
    "8/20 + run259A/261A 散発減弱の「帯内 1 窓即消失」合成) が立ち、深夜帯 ~26-31% 平坦パターンへの収束か "
    "23時台限局上振れかの判別に追加 n が有効 (9/5 前日深夜帯との同日対比, traffic 依存説への最終判定材料)。"
    "host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run262 使用。"
    "現時刻 23時台の間は 23時台 n 積み増し、24時台移行後は 24時台帯初計測へ。"
    "K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\n"
)
anchor2 = "\n## Iteration log\n"
assert txt.count(anchor2) == 1, "iter anchor count = %d" % txt.count(anchor2)
txt = txt.replace(anchor2, anchor2 + entry)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)
print("EDITS DONE")
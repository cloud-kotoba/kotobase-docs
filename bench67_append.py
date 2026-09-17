import io, sys

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

KZ3_EV = " bench 2026-09-06 (第67回, K-Z3 4時台 3 セット目 run184A–C, 同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 04:30 JST, 全 80/80 200, host load1 31.56 は production HTTP 実測のため gate 外): run184A cold(>=0.5s) 0/20 p50 57ms / run184B cold 0/20 p50 92ms / run184C cold 0/20 p50 41ms — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 81ms と静穏で control 分離成立。全 3 run 完全静穏 (4時台 3 セット目)。4時台通算は run182A–C (2/60) + run183A–C (0/60) + 本 tick (0/60) で 180 試行中 2 試行 (~1.1%) の低位帯 — 5/6時台級の静穏。status 判定は rank に委ねる (rank 専門)"

lines = text.split("\n")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3_idx = i
        break
if kz3_idx is None:
    sys.exit("K-Z3 row not found")
lines[kz3_idx] = lines[kz3_idx].rstrip() + KZ3_EV

LOG = "- 2026-09-06: bench 第67回。04:27 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み (fetch rc 0, HEAD 2a43966 = fetch 後 net-kotobase/main 先端と一致, 乖離 0)。live smoke 200 (/, /signup; pre-run script 計測)。host load1 31.56 (gate 7.5 超過) のため local 測定は拒否し「host busy (load1 31.56)」を記録 — rank 第65回 NEXT「K-Q1 transact 401 調査」は cosientist 実装担当のため本 bot 実施範囲外。フォールバック (bench 第66回 NEXT 記載, production HTTP 実測は gate 外): K-Z3 4時台 3 セット目 run184A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 04:30 JST, 全 80/80 200, host load1 31.56): cold 0/0/0 per 20 = 0/60, warm 群 p50 41–92ms, control cold 0/20 p50 81ms 静穏で control 分離成立 — 4時台通算 2/180 (~1.1%) の低位帯 (5/6時台級の静穏)。status 遷移なし (rank 専門)。※terminal foreground 出力が空で戻る runtime 障害のため、本 tick は background 実行 + ファイル書き出しで回避 (測定数値の信頼性には影響なし)。secret は一切記録せず鍵は zero-fill。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 5時台 n 積み増し継続)。"

text = "\n".join(lines).rstrip("\n") + "\n" + LOG + "\n"
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK appended")

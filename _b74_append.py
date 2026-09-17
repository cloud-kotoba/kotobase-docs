import io, re

path = "query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

EVID = (" bench 2026-09-06 (第74回, K-Z3 7時台 3セット目 run194A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 07:58–08:01 JST, 全 80/80 200, host load1 62–219 (急上昇 tick) は production HTTP 実測のため gate 外): run194A cold(>=0.5s) 3/20 (0.5–1.2s 帯 薄クラスタ) p50 167ms / run194B cold 0/20 p50 174ms / run194C cold 0/20 p50 224ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 209ms と静穏で control 分離成立、cold 群は search 側に局在。ただし本 tick 全体の p50 (165–224ms) は host load 急上昇 (219) tick の全体的上振れで not-separated 注記付き (cold 濃度判定 3/60 には影響限定的)。7時台通算 run192+run193+run194 で 4/180 (~2.2%) 低位帯。status 判定は rank に委ねる (rank 専門)。")

LOG = ("- 2026-09-06: bench 第74回。07:54 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 035d174 = fetch 後 net-kotobase/main 先端一致)。falsify 第73回 (run193A–C, 07:39–40) を取り込み済み確認 — 本 tick 分は run194A–C として記録。live smoke 200 (/, /signup; pre-run 計測)。host load1 62.55 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 7時台 3セット目 run194A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 07:58–08:01 JST, 全 80/80 200): cold 3/0/0 per 20 = 3/60 (0.5–1.2s 薄クラスタ, A 群のみ), warm p50 165–224ms, control cold 0/20 p50 209ms 静穏で control 分離成立 — ただし host load 急上昇 (終了時 219) tick の全体的上振れ (p50 165–224ms) で not-separated 注記付き。run186A 型群発は非再現で薄クラスタ型。7時台通算 4/180 (~2.2%) 低位帯。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 7時台 n 積み増し継続)。")

# 1) append evidence to K-Z3 row evidence cell: find the K-Z3 hypothesis table row and insert before " | open |" pattern
kz3_idx = src.find("| K-Z3 |")
assert kz3_idx != -1
row_end = src.find("\n", kz3_idx)
row = src[kz3_idx:row_end]
marker = " | open |"
mi = row.find(marker)
assert mi != -1, "open marker not found in K-Z3 row"
new_row = row[:mi] + " |" + EVID + row[mi:]
src = src[:kz3_idx] + new_row + src[row_end:]

# 2) append iteration log entry at end
src = src.rstrip("\n") + "\n" + LOG + "\n"

io.open(path, "w", encoding="utf-8").write(src)
print("K-Z3 row patched, log appended, len", len(src))

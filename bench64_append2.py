# bench64 — K-Z3 3時台 2 セット目 (run181A-C) evidence 追記 + iteration log bench 第64回
# evidence 追記のみ (status 書き換えは rank 専門)。secret 不含。
import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    doc = f.read()
orig_len = len(doc)

def must_replace(old, new, label):
    global doc
    n = doc.count(old)
    if n != 1:
        raise SystemExit("anchor %s count=%d != 1" % (label, n))
    doc = doc.replace(old, new)

# --- K-Z3 row: run181A-C evidence を K-Z3 行末 (行区切りの直前) に追加 ---
kz3_row_start = doc.index("| K-Z3 | worker |")
kz3_next = doc.index("\n", kz3_row_start)
kz3_add = (" bench 2026-09-06 (第64回, K-Z3 3時台 2 セット目 n 積み増し run181A–C — rank 第63回 fallback 継続,"
    " 同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 03:53 JST, 全 80/80 200, host load1 4.85 は production HTTP 実測のため gate 外):"
    " run181A cold(>=0.5s) 0/20 p50 34ms (max 66ms) / run181B cold 1/20 (945ms 単発) p50 40ms / run181C cold 0/20 p50 38ms —"
    " landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 47ms (max 250ms) と静穏で control 分離成立。"
    "run180A 多発 9/20 は 24 分後の再計測で即時非再現 — 帯内 1 窓型の追加支持。3時台通算 run180+run181 = 11/120 (~9.2%),"
    " 23時台/0時台/1時台 (~4.4–31% 日差込み) と同程度の中位〜低位で traffic 最低帯での発現継続は K-Z3 traffic 依存説への反証材料を継続。"
    "status 判定は rank に委ねる (rank 専門)。")
doc = doc[:kz3_next] + kz3_add + doc[kz3_next:]

# --- Iteration log: bench 第64回 entry を rank 第63回 の直前に挿入 ---
iter_anchor = "- 2026-09-06: rank 第63回。03:20 JST tick。"
iter_entry = ("- 2026-09-06: bench 第64回。03:47 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み"
    " (fetch rc 0, HEAD 3744957 = fetch 後 net-kotobase/main 先端と一致, ancestor rc 0, 乖離 0)。live smoke 200 (/, /signup)。"
    "まず bench63 tick の doc update 失敗を修復 (anchor 不一致で evidence 未記録だったため bench64_append.py で 3 件記録して commit 0caf38c push 済み):"
    " K-Q1 行に bench63 transact 401 再試行 evidence (2 回連続 401, no fabricated data), K-Z3 行に run180A–C evidence, iteration log に bench 第63回 entry。"
    "本 tick 独自測定: K-Z3 3時台 2 セット目 run181A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 03:53 JST, 全 80/80 200, host load1 4.85):"
    " cold 0/1/0 per 20 = 1/60 (945ms 単発), warm 群 p50 34–40ms, control cold 0/20 p50 47ms 静穏で control 分離成立 —"
    " run180A 多発 9/20 は即時非再現で帯内 1 窓型の追加支持。3時台通算 11/120 (~9.2%)。status 遷移なし (rank 専門)。"
    "transact 401 は ephemeral EOA flow の write path 調査 (cosientist 実装担当が適切) を待つ。secret は一切記録せず鍵は zero-fill。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 4時台 n 積み増し継続)。\n")
must_replace(iter_anchor, iter_entry + iter_anchor, "iteration")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)
print("ok before=%d after=%d delta=%d" % (orig_len, len(doc), len(doc) - orig_len))

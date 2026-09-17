# bench64 — bench63 evidence を query-cosientist.md に記録 (bench63 の doc update が anchor 不一致で失敗したため再実施)
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

# --- K-Q1 row: bench63 transact 401 retry evidence ---
kq1_anchor = "次回 quiet-host 時に再試行。bench 2026-09-04:"
kq1_add = (" bench 2026-09-06 (第63回, rank 第63回 NEXT「非空 graph query 計測の再試行 (401 retry 1 回)」を実施):"
    " bench63_kq1_nonempty.mjs (SIWE + ephemeral EOA --provision + Biscuit 発行 + transact datom 投入後の認証付き非空 graph query n=30) を"
    " ephemeral EOA 再生成の retry を含め 2 回実行 — transact が 2 回連続 401 (Unauthorized, body {\"ok\":false,\"error\":\"Unauthorized\"},"
    " 初回 2026-09-05T18:15Z + retry 03:24 JST) で query 計測に進めず測定中断 (no fabricated data)。"
    "SIWE/tenant provision/Biscuit issuance は全て成功 — 401 は transact endpoint 固有で rank 第63回指定どおり独立調査事項として記録。"
    "KV read 内訳初実測 (x-kotobase-kv-stats l1/l2/pack/b2/miss 取得) は transact 401 解決 (ephemeral EOA flow の write path 調査, cosientist 担当が適切) が前提で滞留。secret 不含 (鍵 zero-fill)。")
must_replace(kq1_anchor, kq1_anchor + kq1_add, "K-Q1")

# --- K-Z3 row: run180A-C (3時台) evidence。K-Z3 行の末尾 (次の | K-Z2 | の直前) に挿入 ---
kz3_row_start = doc.index("| K-Z3 | worker |")
kz3_next = doc.index("\n", kz3_row_start)
# 挿入点は K-Z3 行末 (行の改行の直前)
kz3_add = (" bench 2026-09-06 (第63回, K-Z3 3時台帯初計測 run180A–C — rank 第63回 NEXT の transact 401 継続による fallback,"
    " 同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 03:29 JST, 全 80/80 200, host load1 6.07 は production HTTP 実測のため gate 外):"
    " run180A cold(>=0.5s) 9/20 (0.695–1.348s 前半集中の多発クラスタ型, run4–6/run178A 型) p50 37ms (warm 群 31–50ms) /"
    " run180B cold 0/20 p50 34ms (max 50ms) / run180C cold 1/20 (1.167s 単発) p50 35ms (max 1167ms) —"
    " landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 42ms (max 221ms) と静穏で control 分離成立、cold 群は search 側に局在。"
    "3時台帯初計測で 3 試行中 2 試行 cold>0 — run180A 多発は即時非再現の帯内 1 窓型 (run178A と同型)。"
    "深夜帯低位帯 (5/6/8時台 ~0–13%) と 23時台/0時台/1時台 (~4.4–31%) の対比に 3時台 (多発 1 窓 + 静穏 2 窓) を追加、"
    "traffic 最低帯での発現継続は K-Z3 traffic 依存説への反証材料を継続。status 判定は rank に委ねる (rank 専門)。 ")
doc = doc[:kz3_next] + kz3_add + doc[kz3_next:]

# --- Iteration log: bench 第63回 entry を rank 第63回 の直前に挿入 ---
iter_anchor = "- 2026-09-06: rank 第63回。03:20 JST tick。"
iter_entry = ("- 2026-09-06: bench 第63回。03:22 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み"
    " (fetch rc 0, HEAD 3744957 = fetch 後 net-kotobase/main 先端と一致, ancestor rc 0, 乖離 0)。live smoke 200 (/, /signup)。"
    "rank 第63回 NEXT「K-Q1 非空 graph query 計測再試行 (401 retry 1 回)」を実施 — bench63_kq1_nonempty.mjs を新規 ephemeral EOA で再実行するも"
    " transact 401 (Unauthorized) が再現 (初回 2026-09-05T18:15Z + retry 03:24 JST, 2 回連続) で query 計測に進めず測定中断 (no fabricated data)。"
    "SIWE/tenant provision/Biscuit issuance は全て成功するため 401 は transact endpoint 固有 — rank 第63回指定どおり transact 401 を独立調査事項として記録し"
    " K-Z3 3時台 n 積み増しにフォールバック: run180A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 03:29 JST, 全 80/80 200)"
    " run180A cold 9/20 多発クラスタ型 (0.695–1.348s 前半集中, warm 群 p50 37ms) / run180B 0/20 / run180C 1/20 単発,"
    " control cold 0/20 p50 42ms と静穏で control 分離成立 — 3時台帯初計測, run180A 多発は即時非再現の帯内 1 窓型 (run178A と同型)。"
    "status 遷移なし (rank 専門)。K-Q1 の KV read 内訳初実測は transact 401 の解決 (ephemeral EOA flow の write path 調査, cosientist 実装担当が適切) が前提で滞留。"
    "secret は一切記録せず鍵は zero-fill。NEXT: 委ねる (rank 指定優先; K-Q1 は transact 401 解決待ちのため測定可能な切れ手なし — フォールバックは K-Z3 4時台 n 積み増し継続)。\n")
must_replace(iter_anchor, iter_entry + iter_anchor, "iteration")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)
print("ok before=%d after=%d delta=%d" % (orig_len, len(doc), len(doc) - orig_len))

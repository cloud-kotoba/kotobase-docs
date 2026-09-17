# bench65 — K-Q1 transact 401 診断 evidence + K-Z3 4時台 (run182A-C) evidence + iteration log bench 第65回
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

# --- K-Q1 row: bench65 診断 evidence を K-Q1 行末 (行区切りの直前) に追加 ---
kq1_row_start = doc.index("| K-Q1 | query |")
kq1_next = doc.index("\n", kq1_row_start)
kq1_add = (" bench 2026-09-06 (第65回, transact 401 診断 — rank 第63/64回 NEXT「再試行 + 401 再現時は ephemeral EOA 再生成 retry」の完遂, "
    "production HTTP 実測のため gate 外, secret 不含, 鍵は zero-fill): bench63_kq1_nonempty.mjs を新規 ephemeral EOA で再実行し 3 回目の transact 401 を確認 (04:08 JST) — "
    "以下ステップ別診断 (bench65_kq1_diag.mjs, 04:11 JST): siwe_options 200 / siwe_verify 200 valid=true / tenant provision 201 / Biscuit 発行 201 (authorization, graph とも present) / "
    "同一 Biscuit + 同一 headers の pre-transact 認証付き query (空グラフ datomic.q) は 200 (rows: [], policy-mode legacy-public) / 直後の同一 credential での datomic.transact が 401 {\"ok\":false,\"error\":\"Unauthorized\"} (31ms, 即断)。"
    "→ authn/authorization chain 全体は健全で 401 は transact endpoint 固有 — bench63 記録の「ephemeral EOA flow の write path」仮説を実測で確定。transact 401 は K-Q1 (query path 退行) とは独立の調査事項として cosientist 実装担当に引き継ぎ。")
doc = doc[:kq1_next] + kq1_add + doc[kq1_next:]

# --- K-Z3 row: run182A-C evidence を K-Z3 行末 (行区切りの直前) に追加 ---
kz3_row_start = doc.index("| K-Z3 | worker |")
kz3_next = doc.index("\n", kz3_row_start)
kz3_add = (" bench 2026-09-06 (第65回, K-Z3 4時台帯初計測 run182A–C — rank 第64回 fallback「401 継続時は K-Z3 4時台 n 積み増し」を実行, "
    "同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 04:11–04:12 JST, 全 80/80 200, host load1 16.46 は production HTTP 実測のため gate 外): "
    "run182A cold(>=0.5s) 2/20 (1198ms, 769ms 散発) p50 41ms / run182B cold 0/20 p50 37ms / run182C cold 0/20 p50 38ms — "
    "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 46ms と静穏で control 分離成立。4時台通算 2/60 (~3.3%) 低位帯、"
    "3時台 (~9.2%) より低く 5時台 (0/60 完全静穏) 寄りの薄い散発型 (run112/run116 型)。traffic 最低帯での発現継続 (低頻度) は K-Z3 traffic 依存説への反証材料を維持。"
    "status 判定は rank に委ねる (rank 専門)。")
doc = doc[:kz3_next] + kz3_add + doc[kz3_next:]

# --- Iteration log: bench 第65回 entry を rank 第64回 の直前に挿入 ---
iter_anchor = "- 2026-09-06: rank 第64回。03:47 JST tick。"
iter_entry = ("- 2026-09-06: bench 第65回。04:02 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み"
    " (fetch rc 0, HEAD aadd539 = fetch 後 net-kotobase/main 先端と一致, ancestor rc 0, 乖離 0)。live smoke 200 (/, /signup)。"
    "rank 第63/64回 NEXT「K-Q1 非空 graph query 計測再試行 (401 再現時は ephemeral EOA 再生成 retry 1 回)」を実施: bench63_kq1_nonempty.mjs を新規 ephemeral EOA で再実行するも 3 回目の transact 401"
    " (初回 2026-09-05T18:15Z, retry1 18:24Z, 本回 04:08 JST) — 分岐に従い transact 401 を独立調査事項として記録。"
    "併せてステップ別診断 (bench65_kq1_diag.mjs, 04:11 JST): SIWE 200/verify valid, tenant 201, Biscuit 201, 同一 Biscuit の認証付き query 200, 直後 transact のみ 401 即断 —"
    " authn/authorization chain は健全で 401 は transact endpoint 固有 (write path, cosientist 実装担当が適切)。"
    "フォールバック: K-Z3 4時台帯初計測 run182A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 04:11–04:12 JST, 全 80/80 200, host load1 16.46):"
    " cold 2/0/0 per 20 = 2/60 (~3.3%), warm 群 p50 37–41ms, control cold 0/20 p50 46ms 静穏で control 分離成立 — 4時台は低位帯。"
    "status 遷移なし (rank 専門)。secret は一切記録せず鍵は zero-fill。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 5時台 n 積み増し継続)。\n")
must_replace(iter_anchor, iter_entry + iter_anchor, "iteration")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc)
print("ok before=%d after=%d delta=%d" % (orig_len, len(doc), len(doc) - orig_len))

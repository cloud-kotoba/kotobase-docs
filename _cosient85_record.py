#!/usr/bin/env python3
# cosientist 第85回: K-Q1 cut (iii) static falsification recorder.
# Inserts an iteration-log entry under "## Iteration log" and appends a
# segment into the K-Q1 evidence cell. No production code change.
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# --- iteration log entry ---
log_entry = "- 2026-09-06: cosientist 第85回。22:40 JST tick。worktree detached HEAD (58aa0de) のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 58aa0de = net-kotobase/main 先端一致, 乖離 0)。rank 第110回 (22:17) 以降の新規 commit は falsify 第115回 run252 (22時台帯初, cold 9/60, control borderline not-separated) のみで K-Q1 に qualify evidence なし。live smoke 200 (/, /signup)。host load1 44.54 (pre-run, gate 7.5 大幅超過) のため local 測定は拒否 — 本 tick は静的コード実査のみ (production/local 負荷なし)。rank 第109/110回 NEXT「K-Q1 残余切れ手 (iii) did:key (Ed25519) tenant provisioning harness (cosientist 実装専任)」を実施 — cacao 経路の最終切れ手として did:key CACAO harness を静的実査で反証: production engine の datomic.transact write gate は `resolve-transact-auth` (kotobase-graph-database/src/kotobase/graph_database/auth.cljs:404-418) で、production は `KOTOBASE_BISCUIT_AUTH_MODE=*** (wrangler.jsonc:95,210)。この関数は (1) Biscuit scheme → `verify-biscuit-write`、(2) mode=required → 401「Biscuit authorization is required」、(3) cacao → `verify-transact-auth`、の順で、**required モードでは cacao 分岐 (3) が到達不能** — did:key Ed25519 CACAO をいくら正しく mint しても `resolve-transact-auth` は mode=required で 401「Biscuit authorization is required」を返し、cacao verify に到達しない。したがって cut (iii) (did:key tenant provisioning harness による CACAO write 実測) は production 設定下で構造的に実行不能。加えて cosientist 第83回の枠付け「engine write gate=CACAO のみ受理」を補正: 実際は required モードでは **Biscuit のみ受理** (Biscuit scheme → verify-biscuit-write, delegation-for-request が実質の門) で、観測された 401 は credential-type 不整合ではなく verify-biscuit-write の delegation 検証失敗が主因 (cosientist 第81/82回の delegation 工程の延長)。これで K-Q1 の transact 401 は (i)/(ii)/(iii) 全静的切れ手が棄却され、残るは engine の Biscuit delegation 検証 (kotobase-peer 依存, graph/tenant binding に加え cacao 不要の訂正) の動的照合のみ — KV read 内訳初実測 (非空 graph query + x-kotobase-kv-stats) は biscuit delegation が通る正規の tenant 流 (service-account / operator path 等) を要し、現 harness からは到達困難。コード変更なし (qualify する evidence なし — 規律遵守)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; K-Q1 の次切れ手は biscuit delegation-for-request の動的照合 or 正規 tenant write path の調査, フォールバックは K-Z3 現在時刻帯 n 積み増し)。"
log_idx = -1
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        log_idx = i
        break
if log_idx < 0:
    sys.exit("iteration log header not found")

# insert after the "## Iteration log" line
lines.insert(log_idx + 1, log_entry)

# --- K-Q1 evidence cell append ---
kq1_idx = -1
for i, ln in enumerate(lines):
    if ln.startswith("| K-Q1 |"):
        kq1_idx = i
        break
if kq1_idx < 0:
    sys.exit("K-Q1 row not found")

row = lines[kq1_idx]
fin = row.rfind("|")
add = (" cosientist 2026-09-06 (第85回, 静的実査による cut (iii) did:key CACAO harness の反証 — "
       "engine datomic.transact write gate = resolve-transact-auth (auth.cljs:404-418), production "
       "KOTOBASE_BISCUIT_AUTH_MODE=*** (wrangler.jsonc:95,210): required モードでは cacao 分岐が到達不能 "
       "(Biscuit 以外は 401「Biscuit authorization is required」で cacao verify 前に短絡), did:key Ed25519 "
       "CACAO を正しく mint しても transact は通らない — cut (iii) は production 設定下で構造的に実行不能。"
       "第83回の「engine=CACAO のみ受理」は補正: required では Biscuit のみ受理, 観測 401 は "
       "verify-biscuit-write の delegation-for-request 検証失敗が主因 (credential-type 不整合でない)。"
       "静的切れ手 (i)/(ii)/(iii) 全棄却, 残るは Biscuit delegation 動的照合 or 正規 tenant write path。"
       "コード変更なし, secret 不含)")
newrow = row[:fin] + add + row[fin:]
lines[kq1_idx] = newrow

with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("OK log_idx=%d kq1_idx=%d" % (log_idx, kq1_idx))
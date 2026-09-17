#!/usr/bin/env python3
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

old = """cosientist 第81回の production probe で 401 は authn chain ではなく tx_edn write
   path 固有の upstream Biscuit write delegation authz 拒否と具体化し、切れ手(a)
   delegation-for-request の graph/tenant binding (第82回 3 式 parity 実測で棄却) と
   切れ手(i) authority_from_model の scope 照合 (第83回 CID 3 点一致実測で棄却) の
   静的切れ手 2 本が反証され、残る切れ手は (ii) cacao_b64 経路への harness 変更による
   write 実測 1 本 (実装を伴い確度は下がるが期待利得は最大のまま)。順位変動なし、
   最上位維持。"""

new = """cosientist 第81回の production probe で 401 は authn chain ではなく tx_edn write
   path 固有の upstream Biscuit write delegation authz 拒否と具体化し、切れ手(a)
   delegation-for-request の graph/tenant binding (第82回 3 式 parity 実測で棄却) と
   切れ手(i) authority_from_model の scope 照合 (第83回 CID 3 点一致実測で棄却) の
   静的切れ手 2 本に続き、cosientist 第85回の静的実査で最終切れ手 (iii) did:key
   (Ed25519) CACAO harness も反証 — production engine の datomic.transact write gate
   (resolve-transact-auth, auth.cljs:404-418) は KOTOBASE_BISCUIT_AUTH_MODE=required
   で Biscuit scheme のみ受理し cacao 分岐 (verify-transact-auth) は到達不能のため、
   cacao_b64/did:key いずれの mint 経路でも write 実測は構造的に実行不能
   (401「Biscuit authorization is required」で遮断)。観測 401 は credential-type
   不整合ではなく verify-biscuit-write の delegation 検証失敗が主因と具体化 —
   transact 401 の静的切れ手 (a)/(i)/(ii)/(iii) 全滅で、残るは engine の Biscuit
   delegation-for-request 動的照合 (正規 tenant write path, cosientist 実装専任・
   rank 測定指示対象外) のみ。KV read 内訳初実測 (非空 graph query +
   x-kotobase-kv-stats) はその成立が前提で滞留継続。順位変動なし、
   最上位維持。"""

cnt = txt.count(old)
with io.open("/tmp/rank_kq1_count.txt", "w", encoding="utf-8") as f:
    f.write("old_cut_count=%d\n" % cnt)

if cnt == 1:
    txt = txt.replace(old, new)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    with io.open("/tmp/rank_kq1_count.txt", "a", encoding="utf-8") as f:
        f.write("REPLACED_OK\n")
else:
    with io.open("/tmp/rank_kq1_count.txt", "a", encoding="utf-8") as f:
        f.write("NOT_REPLACED (cnt!=1)\n")
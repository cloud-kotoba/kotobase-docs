#!/bin/sh
gh pr create \
  --repo net-kotobase/control-plane \
  --base main \
  --head bot/cosient-20260905-kq1-kvstats-fwd \
  --title "K-Q1: forward x-kotobase-kv-stats through the gateway public header whitelist" \
  --body "## 何を (仮説ID / 出源)

**K-Q1** (query 轸, rank 第50回 NEXT「K-Q1 deploy 整合切分け」の実査で判明した滞留切れ手)。

## 切分け結果 (cosientist 第51回実査)

- engine PR #3 (c3c508f) は remote main 7dc6249 に含まれる (merge-base --is-ancestor = 0)。
- production version 485fd2dc の deploy tag revision 415b1b28 は repo に存在しない未 push 状態だったため、
  main 先端 (7dc6249) から再 deploy: **version ea383ee7-0f9d-427b-8994-b2da566a05c2** (provenance verify 済)。
- 再 deploy 後も production (kotobase.net 経由) では header 不在 0/30。
  engine 側 built artifact (再 deploy で upload された bundle) には x-kotobase-kv-stats emit が存在する。
- 原因: gateway proxy.cljc の public-upstream-json-headers が response headers を
  whitelist (content-type / retry-after / read-audit-cid / witness-statement-cid) で再構築しており、
  engine が付けた x-kotobase-kv-stats が gateway で落とされていた。

## 変更内容 (最小 diff)

- proxy.cljc public-upstream-json-headers: upstream response の x-kotobase-kv-stats を
  固定形状サニタイズ ([\w;=]{1,200}) の上で転送。観察専用 header の pass-through のみ
  (body / authz / status 変更なし、個数のみで secret 不含)。

## 測定 (同一測定法)

- npm test: **555 tests / 2714 assertions / 0 failures 0 errors**。
- deploy 後は bench49 同一測定法 (SIWE auth + warm query 30 samples) で
  xKotobaseKvStatsHeaderObserved が 0 → 30 に変わることを期待 (evidence 欄に追記)。
- secret (token/cookie/credential) は一切含まない。"

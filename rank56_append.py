import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
entry = """- 2026-09-05: rank 第56回。20:08 JST tick。git pull --ff-only で 3c763b1 (bench
  第56回) まで取得 — rank 第55回以降の新規 evidence は bench 第56回 1 本のみ
  (PR control-plane#614 merge 済確認 merge commit 364b335 + bench49 reprobe
  round 2 で x-kotobase-kv-stats header 3/3 不在, query HTTP 200 のみ)。
  取り込み判定: (a) K-Z3/K-Z2/K-S1/K-S2 に新規 evidence なし。19時台低位帯
  (7/300 ~2.3%) 等の既知判定は不変。
  (b) K-Q1: bench 第56回が merge 完了を独立確認し、第55回の「merge 待ち解消」と
  bench49 reprobe 3/3 不在の実測で整合 — 残る切れ手は第55回判定どおり gateway
  deploy 未追従 (main 先端 364b3355 未反映) が最有力で、deploy 実行 (cosientist
  担当) と deploy 後 header 到達確認 0→30 (bench/falsify 担当) に収束。
  2 tick 連続で同一滞留のため、cosientist の次回 cron (41 * * * *) での deploy
  実行が K-Q1 解消の臨界経路。
  transact 401 は引き続き K-Q1 とは別の調査事項として並行記録。
  status 遷移なし (K-Q1 は open 維持 — header 到達実測まで transition 要件を
  満たさない)、rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。
  NEXT: K-Q1 gateway deploy 実行 (cosientist 担当: net-kotobase/main 先端
  364b3355 から gateway 再 deploy; deploy 後の header 到達確認 0→30 は
  bench/falsify が bench49 同一測定法で実施。deploy 完了までのフォールバックは
  K-Z3 現在時刻帯 n 積み増し)。
"""
with io.open(p, "r", encoding="utf-8") as f:
    body = f.read()
if "rank 第56回" in body:
    print("ALREADY_PRESENT")
else:
    if not body.endswith("\n"):
        body += "\n"
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(body + entry)
    print("APPENDED")

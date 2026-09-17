p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()

# ---- 1) append run367 evidence to END of K-Z3 evidence column (line 279, index  ̃278) ----
ev = (" falsify 2026-09-07 (第168回, K-Z3 15時台 n 積み増し run367A–C — iter-log HEAD bench 第159回 (15:26)"
      " NEXT「K-Z3 現在時刻帯 15時台 n 積み増し 続行、 次 run ID は run367 使用」の run367 枠を本 tick 実施"
      " (15時台 4 セット目, run364/365 完全静穏 2 セット + run366 5/60 の後の散発確認), 同測定法 n=20 × 3 + landing control,"
      " 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 15:34:27–15:34:48 JST,"
      " 全 80/80 200, host load1 32.65 (15:34 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため"
      " gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/1 per 20 = 4/60 (~6.7%) —"
      " run367A cold 3/20 (1.1006s 2番目 / 1.0579s 4番目 / 0.9655s 12番目 — 散発配置,"
      " warm 群 p50 84.7ms と交互) p50 93.2ms max 1100.6ms / run367B cold 0/20 p50 60.2ms max 194.4ms /"
      " run367C cold 1/20 (0.9980s 5番目 単発) p50 62.8ms max 998.0ms, control (kotobase.net/signup) cold 0/20 p50 83.4ms max 259.9ms"
      " 完全静穏で control 分離成立、cold 群は search 側に局在。 run367A 散発 3/20 + C 単発 1/20 は B 0/20 + control 0/20 で"
      " 「帯内 1 窓即消失」散発即消失型継続 (run366A 散発 4/20 の 8 分後の弱い再出現, run331A 9/20 heavy 型は非再現継続)。"
      " 15時台 (9/7) 通算 = bench run364 (0/60) + falsify run365 (0/60) + bench run366 (5/60) + 本 tick run367 (4/60) ="
      "  9/240 (~3.8%) の 4 セット低位帯候補 — 帯初 2 セット完全静穏後の散発 2 セット連続で日中低温帯分布パターン維持"
      " (K-Z3 traffic 依存説の方向支持継続・深夜帯 ~26-31% 平坦パターンとの対比不変; 帯水準確定は rank 追加 n に委ねる)。"
      " status 判定は rank に委ねる (rank 専門).")
lines[278] = lines[278].rstrip("\n") + ev + "\n"

# ---- 2) insert iter-log head entry after header line "## Iteration log" (index 362) ----
new_iter = ("- 2026-09-07: falsify 第168回 15:34 JST tick. HEAD db5c58c = bench 第159回 (15:26, K-Z3 15時台"
             " run366 cold 5/60) = remote net-kotobase/main 一致 ( fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込;"
             " terminal foreground 出力不可=既知のため状態確認・測定出力はファイル書き出し経由)。 live smoke 200 (/,/signup; pre-run 計測)。"
             " host load1 32.65 (15:34 uptime 実測, gate  ̃7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
             " ※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD"
             " (bench 第159回, 15:26)「K-Z3 現在時刻帯 15時台 n 積み増し 続行, 次 run ID は run367 使用」の run367 枠を本 tick 実施"
             " (.b367 データ 既存なし =衝突なし確認, 15時台 4 セット目)。 run367 測定 (同測定法 n=20 × 3 + landing control,"
             " 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 15:34:27–15:34:48 JST, 全 80/80 200):"
             " cold(>=0.5s) 3/0/1 per  ̃20 =  ̃4/60 (~6.7%) — run367A cold 3/20 (1.1006s/1.0579s/0.9655s idx 2/4/12 散発配置)"
             " p50 93.2ms / run367B cold 0/20 p50 60.2ms / run367C cold 1/20 (0.9980s idx5 単発) p50 62.8ms,"
             " control (kotobase.net/signup) 0/20 p50 83.4ms max 259.9ms 完全静穏で control 分離成立, cold 群 search 側に局在。"
             " run366A 散発 (15:26) の 8 分後の run367 散発 4/60 で「帯内 1 窓即消失」散発即消失型継続"
             " (run331A 9/20 heavy 非再現継続)。15時台 (9/7) 通算 run364+run365+run366+本 tick run367"
             " = 9/240 (~3.8%) 4 セット低位帯候補 (帯初 2 セット完全静穏後の散発 2 セット連続で日中低温帯分布パターン維持,"
             " K-Z3 traffic 依存説の方向支持継続・深夜帯 ~26-31% 平坦パターンとの対比不変)。status ranking は rank 委譲。"
             " secret は一切記録せず (curl のみ + 統計 python ファイル)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
             " NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 15時台 n 積み増し 続行,次 run ID は run368 使用)")

# insert new_iter at index 363 (right below "## Iteration log" header at index 362)
lines[362] = lines[362].rstrip("\n") + "\n"
lines.insert(363, new_iter + "\n")

with open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted OK; new total lines:", len(lines))
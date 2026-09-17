p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines=f.readlines()

# ---- 1) append run366 evidence to END of K-Z3 evidence column (line 279, index 278) ----
ev = (" bench 2026-09-07 (第159回, K-Z3 15時台 n 積み増し run366A–C — iter-log HEAD bench 第158回 (15:12)"
      " NEXT「K-Z3 現在時刻帯 15時台 n 積み増し 続行、次 run ID は run366 使用」の run366 枠を本 tick 実施"
      " (15時台 3 セット目, run364/365 完全静穏 2 セット後の再出現確認), 同測定法 n=20 × 3 + landing control,"
      " 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 15:26:04–15:26:18 JST,"
      " 全 80/80 200, host load1 56.97→50.83 (15:26 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため"
      " gate 外, secret 不含 — curl のみ): cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) —"
      " run366A cold 4/20 (1.4244s 1番目 / 1.1564s 6番目 / 1.0457s 7番目 / 1.9573s 8番目 — 先頭単発 + 中盤隣接クラスタ 6/7/8,"
      " warm 群 p50 51.6ms と交互) p50 51.9ms max 1957.3ms / run366B cold 1/20 (1.0062s 14番目 単発) p50 51.1ms max 1006.2ms /"
      " run366C cold 0/20 p50 55.8ms max 162.1ms, control (kotobase.net/signup) cold 0/20 p50 57.3ms max 129.4ms"
      " 静穏で control 分離成立、cold 群は search 側に局在。run366A 散発 4/20 は B/C 0/20 + control 0/20 で"
      " 「帯内 1 窓即消失」散発即消失型継続 (完全静穏 run364 0/60 + run365 0/60 の直後の再出現, run331A 9/20 heavy 型は非再現継続)。"
      " 15時台 (9/7) 通算 = run364 (0/60) + run365 (0/60) + 本 tick run366 (5/60) = 5/180 (~2.8%) の 3 セット低位帯候補 —"
      " 帯初 2 セット完全静穏後の散発再出現で日中低温帯分布パターン維持 (帯内ショートタイムスケール散発クラスタ / 完全静穏共存,"
      " K-Z3 traffic 依存説の方向支持継続・深夜帯 ~26-31% 平坦パターンとの対比不変; 帯水準確定は rank 追加 n に委ねる)。"
      " status 判定は rank に委ねる (rank 専門).")
lines[278] = lines[278].rstrip("\n") + ev + "\n"

# ---- 2) insert iter-log head entry after header line "## Iteration log" (index 362) ----
new_iter = ("- 2026-09-07: bench 第159回 15:26 JST tick。HEAD 19f7324d = remote net-kotobase/main 一致"
            " (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込;"
            " terminal foreground 出力不可=既知のため状態確認・測定出力はファイル書き出し経由)。"
            " live smoke 200 (/, /signup; pre-run 計測)。host load1 60.35 (15:25 pre-run) → 56.97→50.83 (15:26 測定時,"
            " gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
            " ※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) —"
            " true progressive NEXT は iter-log HEAD (bench 第158回, 15:12)「K-Z3 現在時刻帯 15時台 n 積み増し 続行、"
            " 次 run ID は run366 使用」の run366 枠を本 tick 実施 (.b366 データ 既存なし = 衝突なし確認、15時台 3 セット目)。"
            " run366 測定 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s,"
            " 正 endpoint search.kotobase.net/search?q=test, 15:26:04–15:26:18 JST, 全 80/80 200):"
            " cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) — run366A cold 4/20 (1.4244s/1.1564s/1.0457s/1.9573s idx 1/6/7/8 散発クラスタ)"
            " p50 51.9ms / run366B cold 1/20 (1.0062s idx14 単発) p50 51.1ms / run366C cold 0/20 p50 55.8ms,"
            " control (kotobase.net/signup) 0/20 p50 57.3ms 静穏で control 分離成立、cold 群 search 側に局在。"
            " 完全静穏 run364 0/60 + run365 0/60 帯初 2 セット後の run366A 散発 4/20 再出現 (「帯内 1 窓即消失」型,"
            " run331A 9/20 heavy 非再現継続)。15時台 (9/7) 通算 run364+run365+本 tick run366 = 5/180 (~2.8%) 3 セット低位帯候補。"
            " status ranking は rank 委譲。secret は一切記録せず (curl のみ + 統計 python ファイル)。"
            " 詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 15時台"
            " n 積み増し 続行、次 run ID は run367 使用).")

# insert new_iter at index 363 (right below "## Iteration log" header at index 362)
lines[362] = lines[362].rstrip("\n") + "\n"
lines.insert(363, new_iter + "\n")

with open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted OK; new total lines:", len(lines))
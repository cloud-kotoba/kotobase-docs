#!/usr/bin/env python3
# bench 第155回: append run359 evidence to K-Z3 row (L279 end) + insert iterlog entry after "## Iteration log".
import io
path="query-cosientist.md"
t=open(path,encoding='utf-8').read()
lines=t.split('\n')

kz3_tail = "帯水準确定・機構判断は rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
assert kz3_tail in lines[278], "K-Z3 anchor tail missing, got:"+lines[278][-120:]

evidence = " bench 2026-09-07 (第155回, K-Z3 14時台帯初計測 run359A–C — rank 第155回 iter-log (14:03) NEXT「K-Z3 14時台帯初計測、次 run ID は run359 使用」の run359 枠, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 14:16:14–14:16:30 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 46.29→43.17 (14:16 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 6/0/1 per 20 = 7/60 (~11.7%) — run359A cold 6/20 heavy クラスタ (0.9694s/0.9829s/1.0139s/1.2020s/1.8463s/1.9149s 散発配置) p50 74.6ms max 1914.9ms / run359B cold 0/20 p50 48.9ms max 177.4ms / run359C cold 1/20 (1.2200s 単発) p50 71.7ms max 1220.0ms, control (kotobase.net/signup) cold 0/20 p50 47.1ms max 148.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。run359A cold 6/20 は heavy (>=6/20) 閾値に再達する 14時台帯初の初候補 (run345A/347A/341A の 12/11時台 heavy 再出現系の後続, run331A 9/20 heavy 型の 14時台再出現) — B/C 0/60 + control 0/20 で「帯内 1 窓即消失」型維持を示す (heavy の持続性は帯内追加 n で確認)。14時台 (9/7) 帯初計測 = 7/60 (~11.7%) の 1 セット日中高位帯初期サンプル。status 判定は rank に委ねる (rank 専門)。"
lines[278] = lines[278].replace(kz3_tail, kz3_tail + evidence)

# Iteration log insert: newest-first, after header "## Iteration log"
header_idx = None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        header_idx=i; break
assert header_idx is not None, "iterlog header not found"

entry = "- 2026-09-07: bench 第155回。14:16 JST tick。HEAD d3a6640 = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 56.38 (14:15) → 46.29→43.17 (14:16 測定時, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第155回 (iter-log, 14:03)「K-Z3 14時台帯初計測、次 run ID は run359 使用」の run359 枠を本 tick 実施 (14時台帯初計測, 13時台 run351..358 済み 8 セット後の積み増し続行)。run359 計測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 14:16:14–14:16:30 JST, 全 80/80 200): cold(>=0.5s) 6/0/1 per 20 = 7/60 (~11.7%) — run359A cold 6/20 heavy クラスタ (0.9694s/0.9829s/1.0139s/1.2020s/1.8463s/1.9149s 散発配置) p50 74.6ms max 1914.9ms / run359B cold 0/20 p50 48.9ms max 177.4ms / run359C cold 1/20 (1.2200s 単発) p50 71.7ms max 1220.0ms, control (kotobase.net/signup) cold 0/20 p50 47.1ms max 148.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。run359A cold 6/20 は heavy (>=6/20) 閾値に再達する 14時台帯初初候補 (run345A/347A/341A の 12/11時台 heavy 再出現系の後続) — B/C 0/60 + control 0/20 で「帯内 1 窓即消失」型維持、heavy の持続性は帯内追加 n で確認。14時台 (9/7) 帯初計測 = 7/60 (~11.7%) の 1 セット日中高位帯初期サンプル。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行、次 run ID は run360 使用)。"
lines.insert(header_idx+1, entry)

open(path,"w",encoding='utf-8').write("\n".join(lines))
print("inserted ok")
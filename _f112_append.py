import io

p = "query-cosientist.md"

EVIDENCE = (
  " falsify 2026-09-06 (第112回, K-Z3 21時台 n 積み増し run247A–C, 同測定法 n=20 × 3 + landing control, "
  "別接続 curl, Tokyo, 21:16:46–21:17:08 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
  "host load1 35.54→31.60 (21:16/21:17 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 "
  "— rank 第108回 NEXT「K-Z3 21時台 n 積み増し継続」に従い 21時台で実施; ※ bench 第99回 (ddb568f) が同一 ID run246 "
  "を 21:09–21:10 に先行計測 (cold 1/60) のため本分を run247 に読み替え, 同一 21時台の独立 2 計測として採用可否は rank 判定に委ねる): "
  "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run247A 単発 1.0892s (10番目, warm 群 p50 52ms 静穏帯水準) "
  "p50 52ms max 1.089s / run247B cold 0/20 p50 51ms max 96ms / run247C cold 0/20 p50 50ms max 78ms "
  "— landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 59ms max 167ms と静穏で "
  "control 分離成立、cold 群は search 側に局在。run247A 単発は B/C 0/20 で即消失し「帯内散発単発即消失」パターン継続。"
  "21時台通算 (falsify run245 3/60 + bench run246 1/60 + 本 tick 1/60) 5/180 (~2.8%) 低位帯サンプル継続で "
  "run245 帯初 (3/60 ~5.0%)・bench run246 (1/60) と同水準、9/4 21時台 ~58% 記録との 2 日差対比は低位側で "
  "traffic 依存説の方向支持継続 (n=3 セット, 帯確定は rank 判定に委ねる)。status 判定は rank に委ねる (rank 専門)。"
)

ITER = (
  "- 2026-09-06: falsify 第112回。21:16 JST tick。worktree detached HEAD のため fetch net-kotobase + "
  "rev-parse 比較で取り込み (初期 fetch HEAD f7ef91a = rank 第108回, 測定後再 fetch で HEAD ddb568f = bench 第99回 (run246A-C, "
  "21:09–21:10 JST, cold 1/60) を検知 — 同一 ID run246 衝突のため本分を run247 に読み替え記録)。rank 第108回 NEXT「K-Z3 21時台 n 積み増し継続」に従い "
  "21時台 n 積み増し run247A–C を実施 (pre-run monitor の NEXT「23時台」は stale と判断, 現在時刻帯 21時台で実施)。live smoke 200 (/, /signup; pre-run 計測)。"
  "host load1 35.54→31.60 (21:16/21:17 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
  "K-Z3 run247A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 21:16:46–21:17:08 JST, 全 80/80 200, 正 endpoint "
  "search.kotobase.net/search?q=test): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run247A 単発 1.0892s (10番目) "
  "p50 52ms / run247B 0/20 p50 51ms max 96ms / run247C 0/20 p50 50ms max 78ms, control (kotobase.net/signup) "
  "cold 0/20 p50 59ms max 167ms 静穏で control 分離成立、cold 群は search 側に局在。run247A 単発は B/C 0/20 で即消失し"
  "「帯内散発単発即消失」パターン継続 — 21時台通算 (falsify run245 3/60 + bench run246 1/60 + 本 tick 1/60) 5/180 (~2.8%) "
  "低位帯サンプル継続、9/4 21時台 ~58% 記録との 2 日差対比は低位側で traffic 依存説の方向支持継続 (n=3 セット, 帯確定は rank 判定に委ねる)。"
  "status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは "
  "K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run248 使用)。"
)

with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()

kz3_idx = None
iter_idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |") or l.startswith("| K-Z3|"):
        if kz3_idx is None:
            kz3_idx = i
    if l.startswith("## Iteration log"):
        iter_idx = i

print("kz3_idx", kz3_idx, "iter_idx", iter_idx)
if kz3_idx is None or iter_idx is None:
    raise SystemExit("anchor not found")

# append evidence to K-Z3 row end (row has no trailing '|')
base = lines[kz3_idx]
end = base.rstrip("\n")
lines[kz3_idx] = end + EVIDENCE + "\n"

# insert iteration-log entry right after "## Iteration log" line (newest first)
lines.insert(iter_idx + 1, ITER + "\n")

with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("done")
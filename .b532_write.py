import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    doc = f.read()

# K-Z3 hypothesis row: find the K-Z3 row line and append evidence
lines = doc.split("\n")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3") and "時間帯依存" in ln:
        kz3_idx = i
        break

ev = (" bench run623A-C: K-Z3 2時台 (2026-09-15 02:15-02:17 JST) n-add, "
      "同測定法 n=20 x3 別接続 curl -sL, search endpoint 301 読替後 "
      "https://search.yataverse.com/?q=test + control https://kotobase.net/ "
      "(301 読替後の直 URL), 全 120/120 200: search cold(>=0.5s) 0/0/0 per 20 = 0/60 "
      "p50 55.1/48.5/47.1ms p95 max 194.4ms, control cold 0/60 p50 90.7/92.5/81.3ms "
      "max 257.7ms. control 分離不能 (両群 0 cold) - not-separated. "
      "host load1 15.51 (02:13 uptime) は production HTTP 実測のため gate 外. "
      "初回 search (curl -sL 無しの 301 body 計測) では cold 5+2/40 の見かけ上振れを確認 - "
      "-L 付き再測で消失 (redirect 応答自体の TTFB 混入の可能性). "
      "secret 不含 (curl + python3 stats のみ).")

if kz3_idx is not None:
    lines[kz3_idx] = lines[kz3_idx].rstrip() + ev
    doc2 = "\n".join(lines)
else:
    raise SystemExit("K-Z3 row not found")

# Iteration log entry right after '## Iteration log' header
iter_hdr = "## Iteration log"
hidx = doc2.find(iter_hdr)
if hidx == -1:
    raise SystemExit("iteration log header not found")
insert_at = doc2.find("\n", hidx) + 1
entry = ("- 2026-09-15: bench 第214回 (02:08 JST tick)。HEAD 32c1a5f = fetch 後 "
         "net-kotobase/main 先端一致 (worktree detached HEAD, fetch + rev-parse 比較, "
         "乖離 0)。falsify 第252回 run622A-C (23時台帯直後枠 cold 6/60) 取り込み済み確認。"
         "rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (2時台) のため "
         "フォールバックで K-Z3 2時台帯 n 積み増し run623A-C を実施 (同測定法 n=20 x3 + "
         "landing control, 別接続 curl -sL, Tokyo, 02:15-02:17 JST, 全 120/120 200): "
         "search cold(>=0.5s) 0/60 p50 55.1/48.5/47.1ms max 194.4ms, control "
         "(kotobase.net/ 直 URL) cold 0/60 p50 90.7/92.5/81.3ms max 257.7ms — "
         "両群静穏で control 分離不能 (not-separated)。endpoint 運用注記: search endpoint "
         "は 301 で search.yataverse.com へ読替済み, control も kotobase.net/ は 301 で "
         "kotoba.cloud/docs/graph/ へ読替 (curl -sL で追従して 200 計測)。"
         "host load1 15.51 (gate 7.5 超過) は production HTTP 実測のため gate 外。"
         "evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。"
         "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。"
         "secret は一切記録せず (curl + python3 stats のみ)。\n")
doc2 = doc2[:insert_at] + entry + doc2[insert_at:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(doc2)
print("ok")

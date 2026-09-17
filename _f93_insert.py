fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
lines = s.split("\n")
# locate the "## Iteration log" header line
il = [i for i, l in enumerate(lines) if l.strip() == "## Iteration log"]
assert len(il) == 1, f"iter log header count={len(il)}"
idx = il[0]  # 0-based index of "## Iteration log"

ev_line = (" falsify 2026-09-06 (第93回, K-Z3 16時台 n 積み増し run221A–C, 同測定法 n=20 × 3 "
           "+ landing control, 別接続 curl, Tokyo, 16:02 JST, 全 80/80 200, host load1 5.26 は "
           "production HTTP 実測のため gate 外): cold 0/60 完全静穏 — run221A cold 0/20 p50 41.1ms "
           "max 70.2ms / run221B cold 0/20 p50 39.7ms max 61.5ms / run221C cold 0/20 p50 36.6ms "
           "max 51.0ms, landing control (kotobase.net/signup) cold 0/20 p50 50.5ms max 120.5ms 静穏で "
           "control 分離成立。search 側 0/60 完全静穏で run218/219/220 型「帯内 1 窓即消失」単発すら "
           "非再現の低位帯。16時台通算 (falsify run154A–C 9/60 + falsify run155A–C 5/60 + 本 tick 0/60) "
           "は帯初の完全静穏 1 セットだが過去 16時台は run154 9/60 ~15% の中位帯 (9/5) — 日差込みの帯確定 "
           "には追加 n 要。status 判定は rank に委ねる (rank 専門)。")

log_line = ("- 2026-09-06: falsify 第93回。16:01 JST tick。worktree detached HEAD のため fetch "
            "net-kotobase で同期確認 (HEAD d2942b5 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。"
            "rank 第90回 NEXT (「cacao_b64 harness / K-Z3 16時台」) 取込み — cacao_b64 は cosientist "
            "実装担当のため実施範囲外。live smoke 200 (/, /signup; pre-run 計測)。host load1 5.26 "
            "(16:02 実測, gate 7.5 未満) だが K-Z3 は production HTTP 観測のため gate 外として実施。"
            "フォールバック (production HTTP 実測): K-Z3 16時台 n 積み増し run221A–C (同測定法 n=20 × 3 "
            "+ landing control, 別接続 curl, 16:02 JST, 全 80/80 200, 正 endpoint "
            "search.kotobase.net/search?q=test): cold 0/0/0 per 20 = 0/60 完全静穏, warm p50 "
            "36.6–41.1ms, control (kotobase.net/signup) cold 0/20 p50 50.5ms max 120.5ms 静穏で "
            "control 分離成立。run218/219/220 型「帯内 1 窓即消失」単発すら非再現の 16時台低位帯サンプル。"
            "16時台は 9/5 に falsify run154A–C (9/60 ~15%) の中位帯記録あり — 日差込みの帯確定には "
            "追加 n 要。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる "
            "(rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し継続)。")

# Insert evidence line before the "## Iteration log" header (end of K-Z3 evidence block)
# only if not already present
if "run221A" not in s:
    lines.insert(idx, ev_line)
    idx += 1
# Insert log line after "## Iteration log"
if "falsify 第93回" not in "\n".join(lines):
    lines.insert(idx + 1, log_line)

open(fn, "w", encoding="utf-8").write("\n".join(lines))
print("inserted ev+log. header now at line", idx + 1)
print("check run221A present:", any("run221A" in l for l in lines))
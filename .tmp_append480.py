path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    content = f.read()
lines = content.split("\n")
anchor = "帯初 n=1 セットのみで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
# locate the K-Z3 hypothesis row (the line that starts with "| K-Z3 |" and contains "run479")
target = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and "run479" in ln:
        target = i
        break
assert target is not None, "K-Z3 row w/ run479 not found"
ln = lines[target]
assert ln.rstrip().endswith(anchor), "anchor not at end of line %d" % (target + 1)

append = (" falsify 2026-09-08 (第215回, K-Z3 16時台 n 積み増し run480A–C — rank 第213回 NEXT「K-Z3 現在時刻帯 16時台 n 積み増し続行, 次 run ID run480」に従い 16時台 2 セット目 n 積み増しとして実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 16:24:30–16:24:45 JST, 全 80/80 200, host load1 45.30 (16:27 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run480A 散発クラスタ 5/20 (0.8955s/1.0030s/1.0397s/1.4144s/2.0793s 散発配置) p50 0.0905s max 2.0793s / run480B cold 0/20 p50 0.0501s max 0.1470s / run480C cold 0/20 p50 0.0489s max 0.1859s, control (kotobase.net/signup) cold 0/20 p50 0.0446s max 0.3134s 完全静穏で control 分離成立、cold 群 search 側局在。run480A 散発クラスタ 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発クラスタ型継続 (run479A 散発クラスタ 5/20 の約 15 分後同型再上振れ, heavy>=6/20 は run480 で未達). 16時台 (9/8) 通算 = bench run479 (6/60, 帯初) + 本 tick run480 (5/60) = 11/120 (~9.2%) の 2 セット — 帯初 6/60 に続く 2 セット目も散発クラスタ 5/60 で日中帯 high 側継続 (15時台 21/240 ~8.8% に引き続く帯初再上振れ → 帯内散発減衰のパターンが 16時台でも弱く継続), traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。帯 n=2 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

lines[target] = ln + append
new = "\n".join(lines)
with open(path, "w", encoding="utf-8") as f:
    f.write(new)

# verify
chk = new.split("\n")[target]
print("RESULT_ROW", target + 1, "has_run480", "run480A" in chk, "has_run479_tail", "run479" in chk)
print("NEW_TAIL")
print(chk[-400:])
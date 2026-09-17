import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

orig_len = len(text)
repls = []

# 1) rank header version bump
old = "rank (期待 gain × 確率, 2026-09-05 第48回):"
new = "rank (期待 gain × 確率, 2026-09-05 第49回):"
assert text.count(old) == 1
repls.append((old, new))
text = text.replace(old, new)

# 2) K-Q1 rank item: add 第49回進展 before "K-Q1 の滞留切れ手は解消。残る切れ手は唯一つ"
old = "   K-Q1 の滞留切れ手は解消。残る切れ手は唯一つ: bench/falsify が\n   x-kotobase-kv-stats header 読み取り付き同一測定法 (n=30+3 warmup 除外) で\n   KV read 内訳を計測する。最大既知 gain のため最上位維持。"
new = ("   第49回進展: bench 第49回が deploy 後の production 実測を再確認 — PR #3 は\n"
       "   net-kotobase/main に merge 済み (7dc6249) だが x-kotobase-kv-stats header 不在\n"
       "   6/6 (deployed: false 実測) で cosientist 第50回の deploy 記録 (version 485fd2dc,\n"
       "   backend.kotobase.net) と計装反映が食い違い、PR #3 計装込み build の production\n"
       "   反映の整合確認が新たな滞留切れ手 (cosientist 担当)。代替の空 graph warm query\n"
       "   p50 ~305ms (not-separated) は退行改善の根拠にならない。順位変動なし、最上位維持。")
assert text.count(old) == 1
repls.append((old, new))
text = text.replace(old, new)

# 3) K-Z3 rank item: append 16時台 evidence
old = "   低位散発型, control 静穏) — 12時台 (~8.3%) と同程度の低位帯。K-Z3 の焦点は"
new = ("   低位散発型, control 静穏) — 12時台 (~8.3%) と同程度の低位帯。第49回進展:\n"
       "   falsify 第53回 run154A–C (16時台, cold 6/3/0 per 20 = 9/60 ~15%, search のみ\n"
       "   1s 超外れ値 9/60, control 静穏) — 16時台は日中帯内では中位寄り (run154A 多発寄り\n"
       "   + B 散発の帯内突発パターン)。K-Z3 の焦点は")
assert text.count(old) == 1
repls.append((old, new))
text = text.replace(old, new)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("OK orig_len=%d new_len=%d repls=%d" % (orig_len, len(text), len(repls)))

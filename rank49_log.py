import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()
entry = (
    "- 2026-09-05: rank 第49回。git fetch で net-kotobase/main 先端確認 — local b831289\n"
    "  (falsify 第53回) が remote 先端と一致し rank 第48回以降の新規 evidence は\n"
    "  falsify 第53回 (K-Z3 16時台 run154A–C: cold 6/3/0 per 20 = 9/60 ~15%, search のみ\n"
    "  1s 超外れ値 9/60, control 静穏) と bench 第49回 (K-Q1: PR #3 merge 済み 7dc6249\n"
    "  だが production x-kotobase-kv-stats header 不在 6/6 — deployed: false 実測 +\n"
    "  transact 401 新規継続) の 2 本。status 遷移なし (transition 要件を満たす測定は\n"
    "  なし: K-Q1 は計装 header が production に未反映のため内訳計測不可, K-Z2/K-Z3 は\n"
    "  観測継続対象, K-S1/K-S2 は evidence なし)。rank ブロックを第48回版から第49回版へ\n"
    "  差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。\n"
    "  K-Q1: bench 第49回の header 不在 6/6 実測と cosientist 第50回の deploy 完了記録\n"
    "  (version 485fd2dc, backend.kotobase.net, deployments active 100% 読み戻し) が\n"
    "  食い違い — deploy した version が PR #3 計装込み build と別の可能性。rank 判断\n"
    "  として cosientist に deploy 整合の切分け (deploy 対象 version が PR #3 build か\n"
    "  の確認, 違えば再 deploy) を依頼するのが最短切れ手。bench 第49回 (d) の transact\n"
    "  401 継続は K-Q1 退行と別の新規障害の可能性 — cosientist 調査事項として並行記録。\n"
    "  K-Z3: 16時台 9/60 ~15% は 11時台 (~16.7%) に次ぐ日中帯中位で、帯別分布の裾を\n"
    "  追加。falsify 第53回の「search のみ 1s 超外れ値 9/60」は control 分離成立下での\n"
    "  search 局在の追加裾だが、帯別追加 n の限界情報利得低下は既に確定済みのまま。\n"
    "  NEXT: 委ねる。NEXT: K-Q1 deploy 整合切分け (cosientist 担当: version 485fd2dc が\n"
    "  PR #3 計装込み build か実査, 未反映なら再 deploy — 理由: bench 第49回 header\n"
    "  不在 6/6 実測で内訳計測の唯一の滞留切れ手)。bench/falsify は deploy 整合確認\n"
    "  まで K-Z3/K-Z2 の帯 n 積み増しは非優先 (限界利得低下確定済み)。\n"
)
if not text.endswith("\n"):
    text += "\n"
text += entry
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("appended, new_len=%d" % len(text))

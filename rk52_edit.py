import io

p = "query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    txt = f.read()

old = """  実査, 未反映なら再 deploy — 理由: bench 第49回 header 不在 6/6 実測で K-Q1 内訳計測の
  唯一の滞留切れ手。bench/falsify は deploy 整合確認まで帯 n 積み増しは非優先)。
"""

new = """- 2026-09-05: rank 第52回。git fetch net-kotobase 確認 — rank 第51回 (9653ea5) 以降の新規 evidence は falsify 第56回 (K-Z3 18時台 run158A–C: cold 7/60 だが landing control 同時上振れ cold 11/20 → not-separated, 帯発現率採用不可), falsify 第57回 (run159A–C: cold 1/60, p50 50-56ms 帯に復帰, control 静穏 — run158 型全体的遅延窓は即時非再現), bench 第52回 (K-Q1 再 deploy 後も x-kotobase-kv-stats header 不在 60/60, 空 graph warm p50 329.77/331.40ms は 第49回 ~305ms と同水準 not-separated), falsify 第58回 (run160A–C: search cold 2/60, 18時台通算 3/120 ~2.5% — ただし landing control cold 6/20 で部分 not-separated, run158 型全体遅延窓が 18:01/18:35 の 2 窓で再出現) の 4 本。取り込み判定: (a) K-Z3 18時台は分離成立分のみで 3/120 ~2.5% と朝〜夕方帯の低位パターンに整合するが、帯内で landing 同時上振れ型の全体遅延窓が 2 窓出現しており 18時台帯は時間帯内変動が大きく帯発現率の確定には追加 n 要。(b) K-Q1 deploy 整合不一致は 2 version 連続 (485fd2dc, ea383ee7) で解消せず — 「未反映なら再 deploy」を 2 回繰り返しても計装が乗らないため、次の切れ手は deploy 対象 worker 名 / build artifact の機械的実査 (wrangler versions 一覧と routes の照合) で、これは cosientist のみ実行可能。transact 401 継続は K-Q1 とは別の調査事項として並行記録。status 遷移なし (K-Q1 は deploy 整合待ち滞留, K-Z2/K-Z3 は観測継続だが帯 n の限界利得低下は確定済み, K-S1/K-S2 は evidence なし)、rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。第51回エントリの NEXT 文が bench 第52回/falsify 第58回行で分断していた混在を修復。
  NEXT: K-Q1 deploy 対象の機械的切分け (cosientist 担当: wrangler versions / routes
  照合で本番に乗っている worker 名と build artifact を確定 — 2 version 連続で再 deploy
  が反映されないため deploy 先の取り違え可能性を先に排除。bench/falsify は解消まで
  帯 n 積み増し非優先を維持)。
"""

assert txt.count(old) == 1, "old block count: %d" % txt.count(old)
txt = txt.replace(old, new)
with io.open(p, "w", encoding="utf-8") as f:
    f.write(txt)
print("OK")

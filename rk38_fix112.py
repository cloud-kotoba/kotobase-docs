# rank 第38回の push 後取り込み修正 (v2):
# (a) bench 第38回の 4時台単体試行を run113 に改名 (falsify run112A-C との ID 衝突回避)
# (b) falsify run112A-C (5時台, cold 1/60) を取り込み 深夜帯通算を 89/29 (~32.6%) に修正
# 根拠はいずれも既存 evidence の実測数字のみ。
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(P, encoding="utf-8").read()
applied = []

def rep1(old, new, tag):
    global s
    n = s.count(old)
    assert n == 1, "%s count=%d" % (tag, n)
    s = s.replace(old, new)
    applied.append(tag)

# (a) rank ブロック内の「run112」→「run113」
rep1(
    "4時台は bench 第38回 run112 (cold 1/20 単発,\n   control 分離成立)",
    "4時台は bench 第38回 run113 (cold 1/20 単発,\n   control 分離成立; falsify run112A–C との ID 衝突を回避し run113 とする)",
    "rename-rank",
)
# (b) rank ブロックの K-Z3 通算を falsify run112A–C 込みに更新 (run113 改名後のテキストに対する anchor)
rep1(
    "とする) — 深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。traffic 最低帯でも ~30% 前後の発現率が維持され",
    "とする)、5時台は falsify run112A–C (cold 1/60, 薄単発, control 静穏) — 深夜帯通算 cold>0 は 89 試行中 29 試行 (~32.6%)。traffic 最低帯でも ~30% 前後の発現率が維持され",
    "count-89-29",
)
rep1("(帯別 ~30–34% でほぼ平坦)", "(帯別 ~29–34% でほぼ平坦)", "flat-29-34")
# (c) evidence ブロックの run112 → run113 + 通算修正
rep1(
    "第38回, K-Z3 深夜帯 4時台 n 積み増し run112,",
    "第38回, K-Z3 深夜帯 4時台 n 積み増し run113 (※ falsify run112A–C との ID 衝突を回避し run113 とする),",
    "rename-evidence",
)
rep1(
    "run100A/104A/107 型の薄い cold 単独クラスタ (warm p50 上振れなし)。4時台 1 試行中 1 試行で cold>0、深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。",
    "run100A/104A/107 型の薄い cold 単独クラスタ (warm p50 上振れなし)。4時台 1 試行中 1 試行で cold>0 (falsify run112A–C による 5時台 cold 1/60 を含む深夜帯通算は 89 試行中 29 試行 ~32.6%)。",
    "evidence-count",
)
# (d) iteration log を修正
rep1(
    "run112 (bench 第38回, 04:55 JST, cold 1/20 単発 1.127s / warm 19/20 p50 0.043s,\n  landing control 静穏で control 分離成立, run100A/104A/107 型薄 cold 単独クラスタ) —\n  4時台 1 試行中 1 試行で cold>0、深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。",
    "run113 (bench 第38回, 04:55 JST, cold 1/20 単発 1.127s / warm 19/20 p50 0.043s,\n  landing control 静穏で control 分離成立, run100A/104A/107 型薄 cold 単独クラスタ;\n  run112 は falsify との ID 衝突のため run113 に改名) —\n  4時台 1 試行中 1 試行で cold>0。さらに本 tick 中に push された falsify run112A–C\n  (5時台, 05:05–05:09 JST, cold 1/60 薄単発, landing control 静穏) を取り込み、\n  深夜帯通算 cold>0 は 89 試行中 29 試行 (~32.6%)。",
    "log-fix",
)

io.open(P, "w", encoding="utf-8").write(s)
print("APPLIED:", ", ".join(applied))

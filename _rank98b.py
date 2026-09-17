import io

P = "query-cosientist.md"
s = io.open(P, encoding="utf-8").read()

# Inject bench 第95回 run231 取込注記 into rank 第98回 entry
anchor = "rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 18時台帯初は従来の順位を変えない)。"
assert s.count(anchor) == 1, "anchor count={}".format(s.count(anchor))
add = (
    anchor + "【追補】本 tick 分析途中に bench 第95回 run231 (18:17 JST, 18時台 2 セット目, "
    "cold(>=0.5s) 2/0/1 = 3/60 ~5.0% — run231A 散発 2 件 + C 単発 1 件, B 0/20 で即消失, "
    "control (kotobase.net/signup) cold 0/20 p50 106.7ms 静穏で分離成立, host load 高騰 111.84 "
    "tick の p50 上振れ borderline note 付き — falsify run230 の control borderline not-separated "
    "(control cold 1 件) は非再現) が worktree に並行追記されたため追加取り込み: 18時台通算 = "
    "falsify run230 (0/1/0 = 1/60) + bench run231 (3/60) = 4/120 (~3.3%) の低位帯候補維持、"
    "run231 は「帯内 1 窓即消失」パターン継続で日中低温帯分布パターン支持継続、traffic 依存説の方向支持"
    "継続・深夜帯 ~26-31% 平坦パターンとの対比も維持 (機構判断は据え置き)。次 tick の NEXT 判定は "
    "run230+run231 合算に基づく。"
)
# note: previous concat line had a syntax-visible typo; rebuild cleanly below
s = s.replace(anchor, add, 1)

io.open(P, "w", encoding="utf-8").write(s)
print("OK applied2")
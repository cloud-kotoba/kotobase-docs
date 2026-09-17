import io
p = "query-cosientist.md"
t = io.open(p, encoding="utf-8").read()

ev = ' bench 2026-09-08 (K-Z3 7時台帯内 2セット目 run432A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 07:06-07:09 JST, 全 80/80 200, host load1 ~19.6 (07:07 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + awk stats のみ): cold(>=0.5s) 2/0/0 per  ́20 =  ́2/60 (~3.3%) - run432A 散発 2/20 (1.461s pos1 / 0.852s pos14) p50 ~0.0807s max 1.4607s / run432B cold 0/20 p50 ~0.118s max 0.243s / run432C cold 0/20 p50 ~0.085s max 0.230s, control (kotobase.net/signup) cold 0/20 p50 ~0.075s max 0.193s 完全静穏で control 分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続 (run428A/429A/430A/431A 単発 → 本 tick A 散発 2 件, heavy>=6/20 は run413A 以降非再現継続)。7時台 (9/8) 通算 = falsify-run431 (帯初 1/60) + 本 tick run432 (2/60) =  ́3/120 (~2.5%) 低位帯継続 - 6時台 (6/360 ~1.7%) に続く朝帯境低位帯で深夜帯→朝帯境静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし,band n=2 セットで帯水準確定には rank 判定を要する)。status 判定は rank に委ねる (rank 専門)。'

it = ' 2026-09-08: bench (K-Z3 7時台帯内 2セット目 run432A-C, 07:06-07:09 JST, 独立 2 計測 telemetry: cold 2/60 (~3.3%; run432A 散発 2/20 (1.461s pos1 / 0.852s pos14) / run432B 0/20 / run432C  ́0/20, control (kotobase.net/signup) 0/20 完全静穏 分離成立,「帯内 1 窓即消失」散発単発型継続。7時台 通算 3/120 ~2.5% 低位帯継続; next run ID は run433 使用; status 判定は rank に委ねる; secret 不含 - curl + awk stats のみ。詳細は K-Z3 evidence 欄末尾 (L279 帯末) 追記。'

hdr = "## Iteration log"
ev = ev.replace("\u0301", "")
it = it.replace("\u0301", "")
ev = ev + "\n"
it = "- " + it + "\n"

t = t.replace(hdr, ev + hdr, 1)
t = t.replace(hdr + "\n", hdr + "\n" + it, 1)
io.open(p, "w", encoding="utf-8").write(t)
print("INSERTED")
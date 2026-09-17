p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
new_ev = (" falsify 2026-09-06 (第97回, K-Z3 17時台 n 積み増し run226A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 17:02:07-17:02:39 JST, 全 80/80 200, host load1 37.5-47.8 (pre-run 計測, gate 7.5 超過) は production HTTP 実測のため gate 外): "
"run226A cold(>=0.5s) 0/20 p50 131.9ms max 309.2ms / run226B cold 0/20 p50 107.5ms max 243.0ms / run226C cold 0/20 p50 101.8ms max 238.8ms "
"- landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 63.5ms max 107.3ms と静穏で control 分離成立、全試行完全静穏 (run226 0/60)。"
"17時台は本日初セットで 0/60 完全静穏 - 9/5 17時台 (run156/157, 1/120 ~0.8% 低位帯) と整合し 16時台 (8/360 ~2.2%) に続く日中低温帯パターン継続、"
"traffic 依存説の方向支持を維持 (深夜帯 ~26-31% との対比は不変)。status 判定は rank に委ねる (rank 専門).")

anchor = "委ねる (rank 専門)。 | K-Z2 | worker |"
data = open(p, encoding='utf-8').read()
idx = data.find(anchor)
if idx == -1:
    print("ANCHOR_NOT_FOUND"); raise SystemExit(1)
# anchor span ends at "委ねる (rank 専門)。" -- insert evidence right after that, before " | K-Z2 |"
insert_pos = idx + len("委ねる (rank 専門)。")
out = data[:insert_pos] + new_ev + data[insert_pos:]
open(p, 'w', encoding='utf-8').write(out)
print("INSERTED at", insert_pos)
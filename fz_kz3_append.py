import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(p, encoding="utf-8").read()
anchor = "falsify 2026-09-05 (K-Z3 深夜帯 5時台 n 積み増し run112A–C"
new = """falsify 2026-09-05 (K-Z3 6時台 n 積み増し run116A–C, 同測定法 n=20 × 3 run, 別接続 curl, Tokyo, 06:28 JST, 全 80/80 200, host load1 9.86 は production HTTP 実測のため gate 外。※ rank 第40回 NEXT は「23時台 n 積み増し」だが cron 実行時刻が 6時台のため帯待機不可能 — cosientist run105 前例に従い同測定法を 6時台として記録, 算入可否は rank 判定に委ねる): run116A cold(>=0.5s) 1/20 (0.779s, 3番目の薄い単発) p50 0.048s / run116B cold 0/20 p50 0.043s / run116C cold 0/20 p50 0.041s — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.050s と静穏で control 分離成立、cold 群は search 側に局在。6時台通算は run105A–C (2/20 薄クラスタ含む) + bench run115 (0/60) + 本 tick で 9 試行中 2 試行 — 23時台/0時台 (~31%) より低く 5時台 (1/120) に近い静穏寄り。深夜帯通算 cold>0 は 98 試行中 30 試行 (~30.6%) で帯別 ~29–33% の平坦パターンはほぼ維持。status 判定は rank に委ねる

"""
i = s.index(anchor)
s = s[:i] + new + s[i:]
io.open(p, "w", encoding="utf-8").write(s)
print("ok")

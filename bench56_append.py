import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

marker = ("  xKotobaseKvStatsHeaderObserved 0→30 を確認。解消まで K-Z3/K-Z2 帯 n 積み増しは\n"
          "  非優先のまま、フォールバックは K-Z3 現在時刻帯 n 積み増し)。\n")
n = src.count(marker)
print("marker count:", n)

entry = (
    "- 2026-09-05: bench 第56回。rank NEXT「K-Q1 PR #614 merge + gateway deploy 後の "
    "header 到達確認 (bench49 同一測定法, xKotobaseKvStatsHeaderObserved 0→30)」を実施: "
    "PR control-plane#614 は 2026-09-05T10:38:53Z merge 済 (merge commit 364b335) を確認したが、"
    "bench49 reprobe round 2 (SIWE + tenant provision + Biscuit 発行 + warm query x3, "
    "19:55 JST, production HTTP 実測のため gate 外, secret 不含) では "
    "x-kotobase-kv-stats header 3/3 不在 (query HTTP 200 のみ, 0→3 未達)。"
    "merge は完了しているため残る切分手は (a) gateway deploy が merge 後 main に追従していない "
    "(b) engine 側 header 出力のいずれかで、cosientist 担当の deploy 実行待ちが最有力。"
    "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先: merge 後 gateway deploy 実行 + "
    "bench49 同一測定法で header 0→30 再確認; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
)

if n >= 1:
    # insert after the LAST occurrence (iteration log tail)
    idx = src.rfind(marker)
    idx_end = idx + len(marker)
    src = src[:idx_end] + entry + src[idx_end:]
    io.open(path, "w", encoding="utf-8").write(src)
    print("appended")
else:
    raise SystemExit("marker missing")

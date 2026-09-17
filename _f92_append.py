# -*- coding: utf-8 -*-
fn = "query-cosientist.md"
entry = """- 2026-09-06: falsify 第92回。15:48 JST tick。worktree detached HEAD のため fetch net-kotobase で同期確認 (HEAD f11d8d5 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第90回 (NEXT「cacao_b64 harness / K-Z3 16時台」) を取込み済み確認 — cacao_b64 は cosientist 実装担当のため実施範囲外。live smoke 200 (/, /signup; pre-run 計測)。host load1 14.41 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 15時台末 n 積み増し run220A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 15:47:53–15:48:15 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (~1.7%) — run220A 単発 0.863s (7番目, 散発型) p50 53.3ms, run220B/C 0/20 (p50 51.2/48.8ms), control (kotobase.net/signup) cold 0/20 p50 60.0ms max 117.8ms 静穏で control 分離成立、cold 群は search 側に局在。run220A 単発は B/C 0/20 で即消失し run216/217/218/219 型「帯内 1 窓即消失」パターンを継続。15時台通算 (run215 2/60 + falsify-run216 1/60 + bench-run217 1/60 + falsify-run218 2/60 + bench-run219 1/60 + 本 tick 1/60) 8/360 ~2.2% 低位帯残界続く。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し継続)。"""
anchor = "- 2026-09-06: bench 第90回。15:38 JST tick。"
s = open(fn, encoding="utf-8").read()
idx = s.find(anchor)
if idx < 0:
    print("ANCHOR_NOT_FOUND", flush=True)
    raise SystemExit(1)
cnt = s.count(anchor)
print("anchor_count=", cnt, flush=True)
s2 = s[:idx] + entry + "\n" + s[idx:]
open(fn, "w", encoding="utf-8").write(s2)
print("INSERTED", flush=True)
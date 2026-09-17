# bench 第97回: insert iteration-log entry before bench 第96回 line
import io

P = 'query-cosientist.md'
txt = io.open(P, encoding='utf-8').read()
lines = txt.split('\n')

target = 290 - 1  # 0-indexed line 290 (bench 第96回)
assert lines[target].startswith('- 2026-09-06: bench 第96回'), repr(lines[target][:40])

entry = ("- 2026-09-06: bench 第97回。20:43 JST tick。worktree detached HEAD (5639692) のため fetch + rev-parse 比較で取り込み "
"(fetch rc 0, HEAD 5639692 = 先端一致, 乖離 0)。live smoke 200 (/, /signup; pre-run 計測)。host load1 29.28 "
"(pre-run 20:37, gate 7.5 超過) のため local 測定は拒否し「host busy (load1 29.28)」を記録 — フォールバック "
"(production HTTP 実測, gate 外): rank 第106回 NEXT「K-Z3 20時台 n 積み増し継続 — 追加 1 セット (run243) で通算 n を 300 に揃え確定」"
"に従い 20時台 5セット目 run243A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 20:43:31–20:43:58 JST, "
"全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — "
"run243A 散発 3 件 (1.0148s 2番目 / 1.0978s 5番目 / 2.0291s 14番目) p50 67.3ms / run243B 0/20 p50 54.1ms max 106.0ms / "
"run243C 0/20 p50 56.4ms max 204.2ms, control (kotobase.net/signup) cold 0/20 p50 64.5ms max 440.6ms 静穏で control 分離成立、"
"cold 群は search 側に局在 — run243A 散発は B/C 0/20 で即消失し run241A/B 型「帯内散発単発即消失」の弱い薄クラスタ、"
"20時台通算 (bench run239 3/60 + falsify run239 0/60 + falsify run240 0/60 + bench run241 2/60 + falsify run242 1/60 + 本 tick 3/60) "
"9/300 (~3.0%) 低位帯残界確定方向。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
"フォールバックは K-Z3 現在時刻帯 21時台帯初計測への継続)。")

lines.insert(target, entry)
io.open(P, 'w', encoding='utf-8').write('\n'.join(lines))
print('inserted iter-log entry at line', target+1)
print('OK')
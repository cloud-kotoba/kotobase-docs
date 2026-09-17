import re

P = 'query-cosientist.md'
txt = open(P, encoding='utf-8').read()

# 1) K-Z4 row insertion (before iter-log header, so positions shift)
HDR = '## Iteration log'
m = re.search(r'^\| K-Z3 \|.*$', txt, re.M)
assert m, 'K-Z3 row not found'
assert m.start() < txt.index(HDR)
kz4 = ("| K-Z4 | worker | 11時台級の同一帯日次変動 (9/9 4/240 ~1.7% vs 9/10 10/60 ~16.7% vs 9/11 10/120 ~8.3%) は帯差とは別の日差成分 — 同一帯を連続日ペア (同一日 n>=2 sets/day + 複数日) で測定し 日差成分を帯平均から分離する。K-Z3 の帯別発現率確定を contaminating なしに行うための分離仮説 | open | — |\n")
txt = txt[:m.end()] + '\n' + kz4 + txt[m.end():]

# 2) iter-log entry insert
hdr_at = txt.index(HDR)
after = hdr_at + len(HDR) + 1
entry = ("- 2026-09-11: rank 第260回。19:04 JST tick。HEAD 3ede3dd = Merge kbb cutover (5caaed3 kbb rewrite 20 invocation(s) + 5dee185 bench 第219回 run583) = fetch 後 bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; git pull --ff-only は silent 失敗のため fetch 手順; terminal foreground stdout 空=既知のため状態確認はファイル書出経由; 真ヘッダ (iteration-log section 先頭) 1 件を事前確認 — 以下の本 entry 内の引用表記を除き重複なし; pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第219回「委ねる, フォールバックは K-Z3 18時台 (9/11) n 積み増し」))。rank 第259回 (3ce1c7b, 15:16) 以降の新規確定 evidence は 1 commit 1 run + 1 infra commit: (1) bench 第219回 commit 5dee185 run583A-C (17:14-17:16 JST, 17時台 (9/11) n 積み増し): cold(>=0.5s) 9/1/1 per 20 = 11/60 (~18.3%) — run583A 散発クラスタ 9/20 (1.05-2.29s max 2285.1ms) p50 193.0ms / run583B 単発 1/20 / run583C 単発 1/20, control (kotobase.net/signup) cold 7/20 (0.51-0.79s) p50 198.9ms 非静穏で control 分離不成立 (not-separated 突発窓注記, run549/run578 型 — 突発が endpoint 横断的で機構判別弱い)。(2) 5caaed3 = kbb cutover (Clojure-CLI/bb/nbb/shadow-cljs invocation 20 件を kbb/amu に rewrite) — hypothesis evidence ではなく infra/ADR adr-2609112000-kbb-cutover-clojure-cli-text による toolchain 変更で K-Q〜K-Z の測定法に影響なし (production HTTP 実測系は不変)。取り込み判定: (a) K-Z3: run583 を 17時台 (9/11) に fold — 17時台 9/11 通算 11/60 (n=1 セット, control not-separated で borderline 維持)。9/8 実績 17時台 12/120 (~10.0%) と同帯日次比較では本測も高位寄りだが control 非静穏のため帯水準確定は追加 clean-tick n 要 (run583 単独では 9/11 突発窓説も残る)。「帯内 1 窓即消失」型は A 内クラスタ + B/C 減衰で継続。K-Z3 traffic 依存説・K-Z4 日差分離の継続観測材料, status 遷移なし (決定的支持/反証に未達, K-Z3 open 観測継続)。(b) K-Q1: 変動なし — cacao_b64 harness 変更は host load1 33.78/42.68/47.09 (19:04 pre-run monitor 実測, gate 7.5 大幅超過) で local 測定不可のまま低負荷 tick 待ち, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。新仮説登録: K-Z4 (同一帯の連続日ペア測定 n>=2 sets/day で日差成分を帯平均と分離する — 11時台 9/9 4/240 ~1.7% vs 9/10 10/60 ~16.7% vs 9/11 10/120 ~8.3% 級の日次変動成分の分離を目的) を表行込みで登録 (rank 第258回からの持ち越し分)。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位: K-Z4 を K-Z3 の直後に低位で挿入 (K-Q1 > K-Z2 > K-Z3 > K-Z4 > K-S1 > K-S2)。live smoke 200/200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 19時台 (9/11) 帯初 n セット run584 (本 tick 時刻 19時台で 9/11 分の帯データがゼロのため起点データ取得が最優先; 19時台は 9/9 run573 10/60 ~16.7%・9/6 run234 4/60 ~6.7% の前日実績あり, 日次変動分離 (K-Z4) の直接材料にもなる)。\n")
txt = txt[:after] + entry + txt[after:]

# sanity
real = [i for i in range(len(txt)) if txt.startswith(HDR, i) and txt[i-1] == '\n' and txt[i+16] == '\n']
assert len(real) == 1, real
assert txt[real[0]+17:real[0]+17+22] == '- 2026-09-11: rank 第260', txt[real[0]+17:real[0]+17+40]
assert txt.count('| K-Z4 |') == 1, txt.count('| K-Z4 |')
open(P, 'w', encoding='utf-8').write(txt)
print('written, len', len(txt), 'real header at', real[0])

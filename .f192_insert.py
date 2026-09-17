#!/usr/bin/env python3
import io
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(path,encoding="utf-8").read()
lines=s.split("\n")

# ---------- 1) append run434 evidence to K-Z3 row ----------
ev = ("   falsify 2026-09-08 (第192回, K-Z3 7時台 n 積み増し run434A-C - rank 第190回 NEXT「K-Z3 7hr n-add run434」の run434 枠として実施, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 07:33:47-07:33:57 JST, 全 80/80 200, host load1 38.19-36.76 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) - run434A cold 単発 1/20 (1.3711s 1番目 冒頭) p50 41.1ms / run434B cold 単発 1/20 (0.9296s 9番目 散発) p50 49.6ms / run434C cold 0/20 p50 46.2ms, control (kotobase.net/signup) cold 0/20 p50 39.6ms max 254.9ms 完全静穏で control 分離成立, cold 群は search 側に局在。run434A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は非再現, run431 型の冒頭集中 3/20 とは別型)。7時台通算 = run431 (3/180) + 本 tick run434 (2/60) = 5/240 (~2.1%) の 4 セット低位帯継続候補 - 朝帯 7時台 (traffic 上昇帯) での cold 散発継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向, 日中低温帯 13-17時台 ~2-5% と同水準方向)。ただし全セット「帯内 1 窓即消失」型で帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i
        break
assert idx is not None
lines[idx] = lines[idx] + ev
news="\n".join(lines)

# ---------- 2) insert iter-log entry ----------
ilog = ("- 2026-09-08: falsify 第192回。07:33 JST tick。HEAD b0dcd16 = rank 第190回 (fold 3/180 ~1.7% 3-set low-band, NEXT K-Z3 7時台 n-add run434) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; detached HEAD のため run-pull 不可, fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 32.96-38.19 (gate 7.5 大幅超過) のため local 測定は拒否 - 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※NEXT「K-Z3 7hr n-add run434」の run434 枠として実施 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 07:33:47-07:33:57 JST, 全 80/80 200, secret 不含 - curl のみ): cold(>=0.5s) 1/1/0 per 20 =  2/60 (~3.3%) - run434A cold 単発 1/20 (1.3711s pos1 冒頭) p50 41.1ms / run434B cold 単発 1/20 (0.9296s pos9 散発) p50 49.6ms / run434C cold 0/20 p50 46.2ms, control (kotobase.net/signup) cold  0/20 p50 39.6ms max 254.9ms 完全静穏で control 分離成立, cold 群は search 側に局在。run434A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl のみ + python stats)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 7時台 n 積み増し続行, 次 run ID は run435 使用)。\n")
anchor="## Iteration log\n"
ia=news.find(anchor)
assert ia!=-1
news = news[:ia+len(anchor)] + ilog + news[ia+len(anchor):]

io.open(path,"w",encoding="utf-8").write(news)
print("OK appended_ev_to_L%d ilog_inserted_at_%d"%(idx+1,ia))
print("new_len=%d"%(len(news)))
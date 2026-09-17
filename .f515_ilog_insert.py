import sys

fn = 'query-cosientist.md'
entry = ("-- 2026-09-08: falsify 第228回。23:56 JST tick。HEAD 3132edc = bench 第227回 (23:41, K-Z3 23時台 n-add run514 cold 6/60)"
         " = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; detached HEAD のため fetch 系で取込;"
         " terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由; worktree doc clean 確認 + run515 未使用確認済,"
         " 次 run ID は run515)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は rank 帯 artifact で"
         " true progressive NEXT は iter-log HEAD 連鎖 (rank 第223回 フォールバック「K-Z3 現在時刻帯 n 積み増し続行」で run514 まで達した枠,"
         " 次の独立続行 set が本 tick run515)。live smoke 200 (/, /signup; pre-run 計測)。host load1 111.24–120.05 (23:52 uptime 実測,"
         " gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 23時台 n 積み増し run515A–C を実測"
         " (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50,"
         " 正 endpoint search.kotobase.net/search?q=test, 23:52:36–23:53:18 JST, 全 80/80 200, secret 不含):"
         " cold 7/0/0 per 20 = 7/60 (~11.7%) – run515A heavy 帯内 1 窓集中クラスタ 7/20 (pos1,4,5,12,16,19,20:"
         " 1.2771/1.1876/1.1838/1.8174/0.7522/2.2835/2.1054s) p50 269.3ms / run515B 0/20 p50 157.8ms / run515C 0/20 p50 141.9ms,"
         " control (kotobase.net/signup) cold 0/20 p50 155.8ms max 423.6ms 完全静穏で control 分離成立, cold 群 search 側局在。"
         " 23時台 (9/8) 通算 23/240 (~9.6%) 4 セット – run515A heavy 7/20 は run512A (7/20) / run514A (5/20) に続き"
         " heavy 集中クラスタ再現 (run513 散発 2/60 は 1 窓のみの例外的減衰), 23時台は heavy 集中が支配的パターンの 1 つとして確度を上げ"
         " 深夜帯遷移 (traffic 依存説) 継続支持。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる"
         " (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し続行, 次 run ID は run516)。")

data = open(fn, encoding='utf-8').read().split('\n')
hdr = None
for i, l in enumerate(data):
    if l.strip() == '## Iteration log':
        hdr = i
        break
if hdr is None:
    print("ERROR: iter-log header not found"); sys.exit(1)
# idempotency guard
if 'falsify 第228回' in data[hdr + 1] or 'run515' in data[hdr + 1]:
    print("ALREADY INSERTED (第228回 present at top) - abort"); sys.exit(2)
data.insert(hdr + 1, entry)
open(fn, 'w', encoding='utf-8').write('\n'.join(data))
buf = open(fn, encoding='utf-8').read()
clean = buf.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '').replace('\ufeff', '')
if clean != buf:
    open(fn, 'w', encoding='utf-8').write(clean)
    print("SCRUBBED zero-width chars")
print("INSERTED at", hdr + 1)
c = open(fn, encoding='utf-8').read().count('falsify 第228回')
print("falsify 第228回 occurrence count:", c)
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p).readlines()
anchor = lines[207]
assert anchor.rstrip().endswith('status 判定は rank に委ねる (rank 専門)。'), anchor[-100:]
add = " bench 2026-09-06 (第87回, K-Z3 14時台 n 積み増し run211A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 14:14–14:15 JST, 全 80/80 200, host load1 90–102 (高負荷 tick) は production HTTP 実測のため gate 外): run211A cold(>=0.5s) 1/20 (0.916s 単発) p50 110ms / run211B cold 0/20 p50 97ms / run211C cold 0/20 p50 123ms — cold 1/60 (~1.7%), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 96ms max 154ms と静穏で control 分離成立、cold 群は search 側に局在。run210A 型冒頭集中クラスタは即時非再現 (帯内 1 窓即消失パターンの追加支持)。本 tick p50 96–123ms は host load 高騰 tick (~100) の全体的上振れ気味だが cold 濃度判定 (1/60) には影響なし。14時台通算は 9/5 run152 (5/60 ~8.3%) + 本 tick (1/60) で 6/120 (~5%) の低位帯寄り。status 判定は rank に委ねる (rank 専門)。"
lines[207] = anchor.rstrip('\n') + add + '\n'
new_entry = "- 2026-09-06: bench 第87回。14:11 JST tick。HEAD ce85639 = fetch 後 net-kotobase/main 先端一致 (ancestor rc 0, 乖離 0; git pull --ff-only は silent 失敗のため fetch + rev-parse 比較で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 90.66→101.60 (gate 7.5 大幅超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 14時台 n 積み増し run211A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 14:14–14:15 JST, 全 80/80 200): cold 1/60 (0.916s 単発), p50 96–123ms, control (kotobase.net/signup) cold 0/20 p50 96ms max 154ms 静穏で control 分離成立 — run210A 型冒頭集中クラスタは即時非再現。14時台通算 6/120 (~5%) 低位帯寄り (9/5 run152 5/60 と合算)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n"
lines.insert(len(lines), new_entry)  # chronological append at end (after rank 第86回 14:05 entry)
open(p,'w').writelines(lines)
print('OK')

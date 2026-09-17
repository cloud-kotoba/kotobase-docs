import io, sys

path = 'query-cosientist.md'
with io.open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# --- evidence append to K-Z3 row (line index 278) ---
ev = (" bench 2026-09-08 (第218回, K-Z3 20時台帯初計測 run499A–C — iter-log HEAD bench 第217回 NEXT 委ねる → "
      "フォールバック K-Z3 現在時刻帯 20時台 (次 run ID 499; pre-run monitor NEXT「23時台」は stale 帯 artifact), "
      "同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
      "正 endpoint search.kotobase.net/search?q=test, 20:09–20:11 JST, 全 80/80 200, "
      "host load1 43.35→47.27 (20:09/20:11 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
      "secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 "
      "- run499A cold 0/20 p50 0.1363s max 0.2813s / run499B cold 0/20 p50 0.0926s max 0.3450s "
      "/ run499C cold 0/20 p50 0.1496s max 0.4841s, control (kotobase.net/signup) cold 0/20 p50 0.1170s max 0.2722s "
      "完全静穏で control 分離成立, search/control とも 0 cold. run499 全 0/60 完全静穏で 20時台(9/8)帯初計測 = 0/60 "
      "- 19時台 (9/240 ~3.8% 4set) に続く晩側低位窓継続, 日中 high 帯 (17時台 ~11.7% / 18時台 ~9.7%) からの晩側減弱方向, "
      "traffic 依存説の観測支持続行, 深夜帯 ~26-31% 平坦パターンとの対比不変. 「帯内 1 窓即消失」散発型の非再現窓 "
      "(heavy クラスタ run487A 7/20 系は再現なし). 帯初 n=1 セットで帯水準確定・機構判断は rank 追加 n を要する. "
      "status 判定は rank に委ねる (rank 専門).")

lines[278] = lines[278].rstrip('\n') + ev + '\n'

# --- iter-log: insert new entry right after '## Iteration log' header ---
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip('\n') == '## Iteration log':
        hdr_idx = i
        break
if hdr_idx is None:
    sys.exit('header not found')

entry = ("- 2026-09-08: bench 第218回。20:11 JST tick。HEAD 071728b = rank 第216回 / cosientist 第149回 を含む "
         "最新 commit 群 = remote net-kotobase/main 一致 (fetch + rev-measuring, worktree diff HEAD 空, "
         "terminal stdout 空=既知のためファイル書出経由; 作業中に sibling の worktree 編集 (rank 第216回 iter 行) を観測するも "
         "HEAD は 071728b のまま worktree clean 整合). pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は "
         "stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (bench 第217回 NEXT 委ねる → フォールバック "
         "K-Z3 現在時刻帯 20時台 n 積み増し, 次 run ID 499)。host load1 43.35→47.27 (20:09/20:11 uptime 実測, gate 7.5 大幅超過) "
         "は production HTTP 実測のため gate 外で実施。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200)。"
         "K-Z3 20時台帯初 run499A-C を実測 (同測定法 n=20 × 3 + landing control, 別 curl, cold>=0.5s, nearest-rank p50, "
         "正 endpoint search.kotobase.net/search?q=test, 20:10:00-20:11:40 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
         "cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - run499A 0/20 p50 0.1363s max 0.2813s / run499B 0/20 p50 0.0926s max 0.3450s "
         "/ run499C 0/20 p50 0.1496s max 0.4841s, control (kotobase.net/signup) cold 0/20 p50 0.1170s max 0.2722s 完全静穏分離成立 "
         "(search/control とも 0 cold)。20時台帯初計測 0/60 完全静穏 - 19時台 (9/240 ~3.8%) に続く晩側低位窓, 日中 high 帯 "
         "(17時台 ~11.7% / 18時台 ~9.7%) から晩側減弱, traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。"
         "帯内 1 窓即消失の非再現窓 (heavy run487A 7/20 系再現なし)。帯初 n=1 セットで帯水準確定・機構判断は rank 追加 n を要する。"
         "status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret 不含。")

lines.insert(hdr_idx + 1, entry + '\n')

with io.open(path, 'w', encoding='utf-8', newline='') as f:
    f.writelines(lines)

print('OK appended')
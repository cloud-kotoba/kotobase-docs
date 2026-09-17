import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

entry = """- 2026-09-06: rank 第87回。14:27 JST tick。HEAD 05bd2fe = fetch 後 net-kotobase/main 先端一致 (ancestor rc 0, 乖離 0; git pull --ff-only は silent 失敗のため fetch + rev-parse 比較で取り込み, 出力はファイル書き出し経由)。rank 第86回 (ce85639, 14:05) 以降の新規確定 evidence は 3 commit:
  (1) falsify 第86回 (b7d2469, run212A–C, K-Z3 14時台帯初計測, 14:06:31–14:07:00 JST): cold 4/0/0 per 20 = 4/60 (~6.7%) — run212A 冒頭集中クラスタ 0.842–1.146s 4件は即消失の帯内 1 窓型, warm p50 61–67ms, control cold 0/20 p50 121.9ms (p50 上振れ borderline 注記付き), run202A/207A/209A/210A 型と整合。
  (2) bench 第87回 (47120b0, run211A–C, K-Z3 14時台 n 積み増し, 14:14–14:15 JST): cold 1/60 (0.916s 単発), p50 96–123ms, control cold 0/20 p50 96ms 静穏で分離成立 — run210A/212A 型冒頭集中は即時非再現, 9/5 run152 と合算し当初 6/120 ~5%。
  (3) bench 第87回追記 (05bd2fe, 14時台通算 10/180 ~5.6% への修正 — falsify run212 4/60 を同時刻帯並行計測として算入)。
  取り込み判定: (a) K-Z3: 14時台通算 10/180 (~5.6%) 低位帯寄り確定 — run212A 冒頭集中 4/60 は 8 分後の run211 (1/60 単発) で即時非再現し「帯内 1 窓即消失」パターンが 14時台でも維持。日中低位帯分布 (14時台 ~5.6% < 11時台 7.5-13% < 16時台 ~15%) と整合し traffic 依存説の方向を支持、深夜帯 ~26-31% 平坦パターンとの対比も維持。帯別追加 n の限界情報利得は低下済み (rank 第79/80/82/83/84回どおり fallback 専門)。(b) K-Q1: 変動なし — transact 401 解決待ち + 残る切れ手は (ii) cacao_b64 経路 harness 変更による write 実測 1 本, 最上位維持。status 遷移なし (qualify する新 evidence なし: K-Q1 は transact 401 解決待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。
  NEXT: K-Q1 transact 401 切れ手(ii) cacao_b64 経路への harness 変更 — gateway bind-tenant-write-graph の CACAO 経路 (proxy.cljc:958-975) を通る write を harness で実測し 401 の再現/非再現を確定 (cosientist 実装担当; 静的切れ手 2 本とも棄却済みのため残る唯一の切れ手, harness 変更を伴う)。bench/falsify のフォールバックは K-Z3 15時台帯初計測 n 積み増し (14時台通算 10/180 ~5.6% 低位帯寄り確定により次の帯へ移行; 夕方帯 cold 単独クラスタ型の帯初サンプルとして最短 1 セット, host load gate 超過時は production HTTP フォールバックの従来手順)。
"""

# Append at end
txt = txt.rstrip("\n") + "\n" + entry

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("OK iteration log appended")
// bench63 doc updates: append evidence to K-Q1 and K-Z3 hypothesis rows + iteration log
import { readFileSync, writeFileSync } from "node:fs";

const path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md";
let doc = readFileSync(path, "utf8");
const before = doc.length;

// --- K-Q1 row: append evidence inside the evidence cell (before the trailing " |") ---
const kq1Anchor = "open | bench 2026-09-03: 未測定 — host busy (load1 17.50 / 1min, 閾値 7.5 超過のため local profiling を実施せず終了)。次回 quiet-host 時に再試行。 bench 2026-09-04:";
if (!doc.includes(kq1Anchor)) throw new Error("K-Q1 anchor not found");
const kq1Addition = " bench 2026-09-06 (第63回, rank 第63回 NEXT「非空 graph query 計測の再試行 (401 retry 1 回)」を実施): bench63_kq1_nonempty.mjs (SIWE + ephemeral EOA --provision + Biscuit 発行 + transact datom 投入後の認証付き非空 graph query n=30) を再実行 — transact が 2 回連続 401 (Unauthorized, retry は新規 ephemeral EOA 再生成, 2026-09-05T18:15Z 初回 + 2026-09-06 03:24 JST retry, body {\"ok\":false,\"error\":\"Unauthorized\"}) で query 計測に進めず測定中断 (no fabricated data)。SIWE/tenant provision/Biscuit issuance は成功 — 401 は transact endpoint 固有で bench 第48回以来 3 例目。rank 第63回指定どおり transact 401 を独立調査事項として記録し K-Z3 へフォールバック。KV read 内訳初実測は transact 401 解決が前提で滞留。secret 不含 (鍵 zero-fill)。";
doc = doc.replace(kq1Anchor, kq1Anchor + kq1Addition);

// --- K-Z3 row: append 3時台 sample. Find the K-Z3 row's evidence cell tail.
const kz3Anchor = "status 判定は rank に委ねる (rank 専門)。 | K-Z2 |";
if (!doc.includes(kz3Anchor)) throw new Error("K-Z3 anchor not found");
const kz3Addition = " bench 2026-09-06 (第63回, K-Z3 3時台 n 積み増し run180A–C — rank 第63回 NEXT「K-Q1 非空 graph 計測再試行 (401 retry 1 回)」の transact 401 継続による fallback, 同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 03:29 JST, 全 80/80 200, host load1 6.07 は production HTTP 実測のため gate 外): run180A cold(>=0.5s) 9/20 (0.695–1.348s 前半集中の多発クラスタ型, run4–6/run178A 型) p50 37ms (31–50ms warm 群) / run180B cold 0/20 p50 34ms (max 50ms) / run180C cold 1/20 (1.167s 単発) p50 35ms (max 1167ms) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 42ms (max 221ms) と静穏で control 分離成立、cold 群は search 側に局在。3時台帯初計測で 3 試行中 2 試行 cold>0 — run180A 多発は即時非再現 (帯内 1 窓型, run178A と同型)。深夜帯低位帯 (5/6/8時台 ~0–13%) と 23時台/0時台/1時台 (~4.4–31%) の対比に 3時台 (帯初, 多発 1 窓 + 静穏 2 窗) を追加、traffic 最低帯での発現継続は K-Z3 traffic 依存説への反証材料を継続。status 判定は rank に委ねる (rank 専門)。";
doc = doc.replace(kz3Anchor, kz3Addition + " | K-Z2 |");

// --- Iteration log: insert bench 第63回 entry above the rank 第63回 line ---
const iterAnchor = "- 2026-09-06: rank 第63回。03:20 JST tick。";
if (!doc.includes(iterAnchor)) throw new Error("iteration anchor not found");
const iterEntry = "- 2026-09-06: bench 第63回。03:22 JST tick。worktree detached HEAD のため fetch + net-kotobase/main 比較で取り込み (fetch rc 0, HEAD 3744957 = fetch 後 net-kotobase/main 先端と一致, ancestor rc 0, 乖離 0)。live smoke 200 (/, /signup)。rank 第63回 NEXT「K-Q1 非空 graph query 計測再試行 (401 retry 1 回)」を実施 — bench63_kq1_nonempty.mjs を新規 ephemeral EOA で再実行するも transact 401 (Unauthorized) が再現 (初回 2026-09-05T18:15Z + retry 2026-09-06 03:24 JST, 2 回連続) で query 計測に進めず測定中断 (no fabricated data)。SIWE/tenant provision/Biscuit issuance は全て成功するため 401 は transact endpoint 固有 — rank 第63回指定どおり transact 401 を独立調査事項として記録し K-Z3 3時台 n 積み増しにフォールバック: run180A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 03:29 JST, 全 80/80 200) run180A cold 9/20 多発クラスタ型 (0.695–1.348s 前半集中, warm 群 p50 37ms) / run180B 0/20 / run180C 1/20 単発, control cold 0/20 p50 42ms と静穏で control 分離成立 — 3時台帯初計測, run180A 多発は即時非再現の帯内 1 窓型 (run178A と同型)。status 遷移なし (rank 専門)。K-Q1 の KV read 内訳初実測は transact 401 の解決 (ephemeral EOA flow の write path 調査, cosientist 実装担当が適切) が前提で滞留。secret は一切記録せず鍵は zero-fill。NEXT: 委ねる (rank 指定優先; K-Q1 は transact 401 解決待ちのため測定可能な切れ手なし — フォールバックは K-Z3 4時台 n 積み増し継続)。\n";
doc = doc.replace(iterAnchor, iterEntry + iterAnchor);

writeFileSync(path, doc);
console.log(JSON.stringify({ ok: true, before, after: doc.length, delta: doc.length - before }));

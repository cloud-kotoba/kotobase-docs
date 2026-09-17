import { readFileSync, writeFileSync } from "node:fs";

const doc = "query-cosientist.md";
let text = readFileSync(doc, "utf8");

// 1) K-Z3 evidence 追記 (K-Z3 行末尾に 1 行追記 — run188 行の直後の bench run エントリ群の末尾に追加)
const kz3Anchor = "bench 2026-09-05 (第41回, K-Z3 6時台 n 積み増し run117A–C";
if (!text.includes(kz3Anchor)) throw new Error("kz3 anchor not found");
const kz3New =
  " bench 2026-09-06 (第70回, K-Z3 6時台 n 積み増し run189A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 06:36–06:37 JST, 全 80/80 200, host load1 61.94 は production HTTP 実測のため gate 外): run189A cold(>=0.5s) 0/20 p50 43ms (max 180ms) / run189B cold 0/20 p50 117ms (max 172ms) / run189C cold 0/20 p50 101ms (max 172ms) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 51ms (max 293ms) と静穏で control 分離成立。run186A 群発 (9/20) は 3 tick 連続非再現。status 判定は rank に委ねる";
text = text.replace(kz3Anchor, kz3New + "\n" + kz3Anchor);

// 2) Iteration log 末尾に entry 追記 (ファイル末尾)
const logEntry = "\n- 2026-09-06: bench 第70回。06:36 JST tick。git pull --ff-only (Already up to date, HEAD 85ec4c9 = main 先端一致)。falsify 第70回 (run188A–C, 06:33 JST) を取り込み済み確認 — 本 tick 分は run ID 衝突回避のため run189A–C として記録。live smoke 200 (/, /signup; pre-run 計測)。host load1 61.94 (gate 7.5 超過) のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 6時台 4セット目 run189A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 06:36–06:37 JST, 全 80/80 200): cold 0/0/0 per 20 = 0/60, warm p50 43–117ms, control cold 0/20 p50 51ms 静穏で control 分離成立 — run186A の突発群発 (9/20) は 3 tick 連続非再現で run100A/116A 型短時間窓パターンを追加支持。status 遷移なし (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 6時台 n 積み増し継続)。\n";
text = text + logEntry;

writeFileSync(doc, text);
console.log("appended ok");

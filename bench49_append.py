#!/usr/bin/env python3
"""bench49 (第49回): query-cosientist.md に bench evidence を追記する。

- Iteration log 末尾に bench 第49回エントリを 1 行追記
- K-Q1 行の evidence 欄末尾に追記
"""
import io
import re
import sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

BENCH_ENTRY = (
    "bench 2026-09-05 (第49回, K-Q1 deploy 後計測の前提再確認 — rank 第48回 NEXT の "
    "x-kotobase-kv-stats header 読み取り付き同測定法に先立つ deploy 判別, production HTTP 実測のため gate 外, secret 不含): "
    "(a) engine repo 実査 — fetch net-kotobase 後の net-kotobase/main 先端は 7dc6249 で PR #3 "
    "(bot/cosient-20260905-kq1-kvstats, c3c508f) は main マージ済み (merge-base --is-ancestor: YES, "
    "merge commit 7dc6249 確認, bench 第48回時点の 0d04d00 から進行)。"
    "(b) deploy 判別プローブ (docs/bench49_reprobe.mjs + bench49_reprobe2.mjs, K-Q2 harness flow 踏襲, "
    "ephemeral EOA, 各 3 リクエスト = 計 6 query, 16:04–16:11 JST): "
    "認証済み datomic.q は全 6/6 で 200 を返すが x-kotobase-kv-stats header は全 6 リクエストで不在 (deployed: false) — "
    "engine repo の main に merge は完了しているが production deploy は未実施と実測確定 "
    "(cosientist 第50回記載の deploy は backend.kotobase.net 向け version 485fd2dc で、"
    "PR #3 計装込み build とは別バージョンの可能性が高い、この整合は cosientist/rank 判断に委ねる)。"
    "(c) transact 401 継続 — ephemeral EOA + Biscuit (data:read/data:write) での認証済み datomic.transact が "
    "3 プローブすべて HTTP 401 {ok:false, error:\"Unauthorized\"} で失敗 (bench 第48回 (c) の harness flow では "
    "同一 flow が 200 を返していたため本 tick からの新規退行の可能性、query path は影響を受けていない)。"
    "→ K-Q1 header 読み取り付き同測定法 (n=30+3 warmup 除外) は production deploy 完了まで実施不可、"
    "代替として transact なし (空 graph) の warm query 実測を実施: "
    "docs/bench49_kq1_warmquery.mjs (n=30+3 warmup 除外, nearest-rank, Node 26, Tokyo, 16:12 JST): "
    "authenticated warm query p50 299.94ms / p95 592.50ms / p99 693.74ms / min 270.98 / max 693.74 / mean 340.11 "
    "(200 30/30, x-kotobase-kv-stats header 不在 30/30) — bench 第48回 (c) の 683.90ms (n=5) より低いが "
    "n と時刻が違い、かつ transact 401 により datom 未投入の空 query path であるため "
    "退行改善とは判断できない (not-separated)。"
    "docs/bench49_kq1_warmquery2.mjs (同測定法, 16:13 JST): p50 309.81ms / p95 448.89ms / max 553.62ms "
    "(200 30/30, header 不在 30/30) — 2 試行平均 p50 ~305ms は falsify 第3段 (683.73ms) より有意に低いが "
    "空 query path と時刻差が混在し機構切分けは不可 (not-separated)。"
    "(d) transact 401 の継続は K-Q1 退行とは別の新規障害の可能性 — query 200 / transact 401 の分離は "
    "cosientist/rank 側の調査事項として記録。NEXT は rank 指定を優先し、本 bot は K-Z3 14時台 n 積み増し継続をフォールバック。"
)

KQ1_APPEND = (
    " bench 2026-09-05 (第49回): PR #3 (c3c508f) は net-kotobase/main に merge 済み (7dc6249) だが "
    "production では x-kotobase-kv-stats header 不在 6/6 (deployed: false 実測) — deploy 未反映。"
    "代替計測 (transact 401 により空 graph, n=30+3 warmup 除外, nearest-rank, Node 26, Tokyo, 16:12–16:13 JST): "
    "warm query p50 299.94ms / 309.81ms (2 series), p95 592.50ms / 448.89ms — bench 第48回 683.90ms (n=5) と "
    "falsify 第3段 683.73ms より低位だが 空 query path + 時刻差が混在し 退行改善判定は not-separated。"
    "別途 transact 401 (Unauthorized) が ephemeral EOA flow で新規に継続発生 (bench 第48回時点は 200) — "
    "query 200 / transact 401 の分離は K-Q1 とは別の調査事項。status 判定は rank に委ねる。"
)


def append_iteration_log(text: str, entry: str) -> str:
    lines = text.split("\n")
    # find last non-empty line index
    last = len(lines) - 1
    while last >= 0 and lines[last].strip() == "":
        last -= 1
    lines.insert(last + 1, entry)
    return "\n".join(lines)


def append_kq1_evidence(text: str, addition: str) -> str:
    # K-Q1 row is the table row starting with "| K-Q1 |"
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("| K-Q1 |"):
            stripped = line.rstrip()
            if stripped.endswith("|"):
                lines[i] = stripped[:-1] + addition + " |"
            else:
                lines[i] = stripped + addition + " |"
            return "\n".join(lines)
    raise RuntimeError("K-Q1 row not found")


def main() -> None:
    with io.open(PATH, "r", encoding="utf-8") as f:
        text = f.read()
    if "bench 2026-09-05 (第49回" in text:
        print("already applied, skipping")
        return
    text = append_kq1_evidence(text, KQ1_APPEND)
    text = append_iteration_log(text, BENCH_ENTRY)
    with io.open(PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("appended bench49 evidence to K-Q1 row and iteration log")


if __name__ == "__main__":
    sys.exit(main())

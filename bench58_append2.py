import subprocess, time

r = subprocess.run(["git", "pull", "--ff-only"], capture_output=True, text=True)

path = "query-cosientist.md"
lines = open(path).read().splitlines(keepends=True)
idx = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 | worker |")]
assert len(idx) == 1, idx
target_idx = idx[0]

entry = (" bench 2026-09-05 (第58回, K-Z3 21時台 n 積み増し run170A–C — rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」だが "
         "cron 実行時刻が 21時台のため帯待機不可能, run105/run116 前例に従い 21時台として記録・算入可否は rank 判定に委ねる, "
         "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 21:07–21:09 JST, 全 80/80 200, "
         "host load1 92.38 は production HTTP 実測のため gate 外): "
         "run170A cold(>=0.5s) 2/20 (1.034s 2番目, 1.094s 8番目 — 散発) p50 0.200s / run170B cold 0/20 p50 0.176s / "
         "run170C cold 0/20 p50 0.176s (warm max 0.426s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は "
         "cold 0/20 p50 0.222s (0.179–0.424s) と静穏で control 分離成立、cold 群は search 側に局在。"
         "run170A は run100A/104A 型の薄い cold 単独クラスタ (warm p50 上振れなし)。ただし本 tick の search p50 (0.176–0.200s) は "
         "host load1 92 という極端な高負荷 tick で landing control p50 も 0.222s と同程度に上振れしており "
         "日中〜夜帯の通常 p50 水準 (~40–100ms) と乖離 — cold 2/20 の機構判定は host 由素混入可能性を分離できず "
         "not-separated 注記付き。21時台は 2026-09-04 通算 (run92–94, cold>0 9/36 試行 ~25%) に対し本 tick は薄散発 1/3 試行。"
         "status 判定は rank に委ねる (rank 専門)。")

row = lines[target_idx].rstrip("\n")
assert row.endswith(" |"), row[-40:]
assert "run170" not in row, "already appended"
lines[target_idx] = row[:-2] + entry + " |\n"
open(path, "w").write("".join(lines))
print("pull:", r.stdout.strip() or r.stderr.strip())
print("appended at line", target_idx + 1)

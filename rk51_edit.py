import io
import sys
import subprocess

PATH = "query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()

orig_len = len(txt)
results = []


def rep(old, new, label, required=True):
    global txt
    n = txt.count(old)
    if n != 1:
        msg = "%s: count=%d" % (label, n)
        if required:
            print("ABORT " + msg)
            sys.exit(1)
        print("WARN(skip) " + msg)
        results.append(label + ":skip")
        return
    txt = txt.replace(old, new)
    print("OK " + label)
    results.append(label + ":ok")


# (a) rank block header: 第49回 -> 第51回
rep(
    "rank (期待 gain × 確率, 2026-09-05 第49回):",
    "rank (期待 gain × 確率, 2026-09-05 第51回):",
    "rank-header",
)

# (b) rank block K-Z3 item: add 第51回進展 (17時台 re-aggregation)
old_b = "+ B 散発の帯内突発パターン)。K-Z3 の焦点は"
new_b = (
    "+ B 散発の帯内突発パターン)。第51回進展: 17時台は falsify run155A–C (5/60,\n"
    "   rank 第50回取り込み済み) + bench 第50回 run156A–C (1/60) + falsify 第55回\n"
    "   run157A–C (0/60) で 180 試行中 6 (~3.3% — falsify 第55回記載の 1/120 は\n"
    "   run155 算入漏れのため本集計を正) — 16時台 (~15%) から 9時台級の低位に復帰。\n"
    "   K-Z3 の焦点は"
)
rep(old_b, new_b, "rankblock-kz3")

# (c) best-effort: repair interleaved rank 第50回 entry (bench 第50回 line was
# inserted mid-entry by a concurrent append, splitting the NEXT sentence).
bench_line = (
    "- 2026-09-05: bench 第50回。rank 第50回 NEXT は K-Q1 deploy 整合切分け (cosientist 担当) で "
    "bench は非対象 — フォールバックとして K-Z3 17時台 n 積み増し run156A–C を同測定法で実施 "
    "(17:32–17:33 JST, production HTTP 実測のため gate 外, secret 不含): cold 1/60 (~1.7%), "
    "17時台通算 6/120 ~5.0% 低位帯, landing control 静穏, search 局在の 1s 超単発外れ値 1 件のみ。 "
    "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先; K-Q1 deploy 整合確認までは "
    "K-Z3/K-Z2 帯 n 積み増し非優先の rank 指定に従う)。"
)
old_c = (
    "  NEXT: K-Q1 deploy 整合切分け (cosientist 担当: version 485fd2dc が PR #3 計装込み\n"
    + bench_line
    + "\n"
    "  build か実査, 未反映なら再 deploy — 第49回 NEXT を維持。bench/falsify は deploy 整合\n"
    "  確認まで帯 n 積み増しは非優先)。"
)
new_c = (
    "  NEXT: K-Q1 deploy 整合切分け (cosientist 担当: version 485fd2dc が PR #3 計装込み\n"
    "  build か実査, 未反映なら再 deploy — 第49回 NEXT を維持。bench/falsify は deploy 整合\n"
    "  確認まで帯 n 積み増しは非優先)。\n"
    + bench_line
)
rep(old_c, new_c, "deinterleave-rank50", required=False)

# (d) append rank 第51回 iteration log entry
entry = """- 2026-09-05: rank 第51回。git fetch 確認 — HEAD/remote とも 9e04b8c (falsify 第55回) で
  rank 第50回以降の新規 evidence は bench 第50回 (K-Z3 17時台 run156A–C: cold 1/60) と
  falsify 第55回 (K-Z3 17時台 2 セット目 run157A–C: cold 0/60 完全静穏, control 静穏) の
  2 本。17時台通算は run155A–C (5/60) + run156A–C (1/60) + run157A–C (0/60) で
  180 試行中 6 (~3.3%) — falsify 第55回記載の「120 試行中 1 (~0.8%)」は run155 分の
  算入漏れ、bench 第50回の 6/120 (~5.0%) は run155 込みで整合 (evidence 行自体は
  falsify 担当のため rank は書き換えず、本集計を正とする)。17時台は 16時台 (~15%) から
  9時台級 (~3.9%) の低位に復帰 — 夕方ピーク帯で中位→低位に戻る帯別サンプルだが、
  帯別追加 n の限界情報利得低下は第49回確定のまま。status 遷移なし (K-Q1 は deploy
  整合切分け待ちのまま計装計測不可, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)、
  rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。併せて rank 第50回エントリ内に
  bench 第50回追記が割り込んでいた混在 (NEXT 文の分断) を修復。
  NEXT: K-Q1 deploy 整合切分け (cosientist 担当: version 485fd2dc が PR #3 計装込み build か
  実査, 未反映なら再 deploy — 理由: bench 第49回 header 不在 6/6 実測で K-Q1 内訳計測の
  唯一の滞留切れ手。bench/falsify は deploy 整合確認まで帯 n 積み増しは非優先)。
"""
if not txt.endswith("\n"):
    txt += "\n"
txt += entry
print("OK append-log (rank 第51回)")

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(txt)
print("WROTE %d chars (was %d)" % (len(txt), orig_len))


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout or "").strip()
    err = (r.stderr or "").strip()
    print("$ " + " ".join(cmd))
    if out:
        print(out)
    if err:
        print("[stderr] " + err)
    return r.returncode


run(["git", "rev-parse", "--short", "HEAD"])
run(["git", "add", PATH])
rc_commit = run(
    [
        "git",
        "commit",
        "-m",
        "rank 第51回: falsify 第55回 (K-Z3 17時台 run157A-C cold 0/60) + bench 第50回 "
        "(run156A-C cold 1/60) を取り込み — 17時台通算 6/180 ~3.3% (run155 算入漏れの再集計), "
        "status 遷移なし, 順位変動なし, rank 第50回エントリの混在修復, "
        "NEXT: K-Q1 deploy 整合切分け (cosientist)",
    ]
)
if rc_commit == 0:
    rc_push = run(["git", "push", "net-kotobase", "HEAD:main"])
    print("PUSH_RC=%d" % rc_push)
else:
    print("COMMIT_RC=%d (push skipped)" % rc_commit)
print("DONE")

import io, subprocess

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

entry = """
- 2026-09-06: rank 第78回。09:25 JST tick。worktree detached HEAD (032b37b) のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 032b37b = fetch 後 net-kotobase/main 先端一致, 乖離 0)。falsify 第77回 (run198A–C/200A–C), bench 第77回 (run199A–C), bench 第78回 (run201A–C, 9時台帯初計測) を取り込み済み確認。rank 更新: (1) K-Z3 9時台通算を run201 (cold 5/60, run201A 末尾集中クラスタ 0.800–1.475s, warm p50 37–49ms 静穏, control 分離成立) を含め 240 試行中 12 試行 (~5%) に更新 — 突発 3 セット目 (run122/run123A/run201A) がすべて 09:22–09:49 JST の traffic 上昇帯に集中し 8時台 0/240 前後との対比で K-Z3 traffic 依存説の方向を引き続き支持するが、深夜帯 ~26-31% 平坦パターンが残るため判定は据え置き。(2) status 遷移なし (qualify する新 evidence なし)。(3) rank 順位変動なし: K-Q1 最上位維持 (滞留切れ手は PR net-kotobase/control-plane#614 merge + gateway deploy 後の x-kotobase-kv-stats header 到達確認)。K-Z3 は帯別分布の情報利得低下確定済みだが run201A 型帯内 1 窓クラスタの即時非再現確認には 9時台の追加 n が限定価値あり。NEXT: K-Z3 9時台 n 積み増し (run201A クラスタの帯内窓性確認 — 即時非再現なら run122 型と同型で 9時台突発の時間窓依存が 3 例に確定, host load gate 超過時は production HTTP フォールバックの従来手順)。
"""

with io.open(path, "a", encoding="utf-8") as f:
    f.write(entry)

r = subprocess.run(["git", "diff", "--stat"], capture_output=True, text=True)
print(r.stdout)

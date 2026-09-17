import io

P = "query-cosientist.md"
s = io.open(P, encoding="utf-8").read()

old = "NEXT: K-Z3 現在時刻帯 18時台 n 積み増し継続 (rank 第97回 NEXT を維持 — 18時台は falsify 第100回 run230 1 セット 1/60 のみ・control 分離 weak のため帯確定には追加 n 要。低温帯継続確認で traffic 依存説の方向支持の追加 n。"
new = "NEXT: K-Z3 現在時刻帯 18時台 n 積み増し継続 (rank 第97回 NEXT を維持 — 18時台は falsify run230 (1/60) + bench run231 (3/60) = 4/120 ~3.3% 低位帯候補済み、control 分離は bench 第95回 run231 で成立 (run230 borderline は非再現) だが帯確定にはなお追加 n 要。低温帯継続確認で traffic 依存説の方向支持の追加 n。"
assert s.count(old) == 1, "old count={}".format(s.count(old))
s = s.replace(old, new, 1)

io.open(P, "w", encoding="utf-8").write(s)
print("OK applied3")
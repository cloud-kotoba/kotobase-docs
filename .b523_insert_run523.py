#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, unicodedata
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
HDR_K="| K-Z3 |"
EV=(" falsify 2026-09-09 (第233回, K-Z3 2時台(深夜帯)帯初計測 run523A-C, "
 "同測定法 n=20 x 3 + landing control, 別接続 curl,, cold>=0.5s,, nearest-rank p50,, "
 "正 endpoint search.kotobase.net/search?q=test,, 02:07 JST 計測, 全 80/80 200,, secret 不含 - curl + python stats のみ): "
 "cold(>=0.5s) 6/2/0 per  20 =  8/60 (~13.3%) - run523A cold 6/20 heavy 散発クラスタ "
 "(0.8772/0.8794/0.9366/0.9997/1.3394/1.6229s, p50 119.6ms / run523B cold 2/20 "
 "(0.8919/1.4466s, p50 44.0ms / run523C cold 0/20 p50 48.7ms, control (kotobase.net/signup), "
 "cold 0/20 p50 43.5ms max 257.5ms 完全静穏で control 分離成立,, cold 群は search 側に局在。"
 "run523A heavy 6/20 は B/C  0/40 + control  0/20 で即消失し「帯内 1 窓即消失」heavy 型 "
 "(run260A/263A/267A/271A 型, の 2時台帯初再出現 - heavy クラスタの帯水準持続性は帯内追加 n で確認 "
 "(status 判定は rank に委ねる/rank 専門)。2時台 (9/9)帯初計測 =  ́ 8/60 (~13.3%) の高位帯初期サンプル - "
 "1時台 13/180 ~7.2% 3セット から移行後も帯初 cold>0 で深夜帯 traffic 依存説への反証材料を継続 "
 "(深夜帯 ~26-31% 平坦パターンと整合方向)。ただし帯 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する。")
IL=("- 2026-09-09: falsify 第233回。。02:41 JST tick (計測 02:07 JST, HEAD daf17a9 = rank 第230回 取込済み・NEXT run523 枠)。"
 "detached HEAD のため fetch 系で取込 (terminal stdout 空=既知のためファイル書き出し経由)。"
 "K-Z3 2時台(深夜帯)帯初計測 run523A-C を取込 (同測定法 n=20 x 3 + landing control,,別接続 curl,, "
 "cold>=0.5s,, nearest-rank p50,, 正 endpoint search.kotobase.net/search?q=test,, 02:07 JST,, 全 80/80 200,, secret 不含 - curl + python stats のみ): "
 "cold(>=0.5s) 6/2/0 per  20 =  8/60 (~13.3%) - run523A cold 6/20 heavy 散発クラスタ, "
 "run523B cold 2/20 単発/ペア, run523C cold 0/20,, control (kotobase.net/signup) cold  ́0/20 完全静穏で control 分離成立, "
 "cold 群 search 側局在。run523A heavy 6/20 は B/C  0/40 + control  0/20 即消失で「帯内 1 窓即消失」heavy 型 - "
 "heavy クラスタの帯水準持続性は帯内追加 n で確認。。2時台 (9/9) 帯初計測 =  ́ 8/60 (~13.3%) - "
 "1時台 13/180 ~7.2% 3セット から移行後も帯初 cold>0 で深夜帯 traffic 依存説への反証材料継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。"
 "帯水準確定・機構判断には未達 (status 判定は rank に委ねる/rank 専門)。NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行,,"
 "次 run ID は run524 使用 - run523 を本 tick が消費済みのため次セットは run524)。secret は一切記録せず。。")

def clean(s):
    s=s.replace("\u200b","").replace("\u200c","").replace("\u200d","").replace("\ufeff","")
    return "".join(ch for ch in s if unicodedata.combining(ch)==0)

EV=clean(EV); IL=clean(IL)
f=io.open(P,encoding="utf-8",newline="")
lines=f.readlines(); f.close()
hdr=[i for i,l in enumerate(lines) if "## Iteration log" in l]
kz=[i for i,l in enumerate(lines) if l.startswith(HDR_K)]
assert hdr and kz

hi=hdr[0]; ki=kz[0]
joined="".join(lines
assert "第233回" not in joined
row=lines[ki]
assert row.endswith("\n")
core=row[:-1]
lines[ki]=core + " " + EV + "\n"
hdrline=lines[hi]
assert hdrline.startswith("## Iteration log")
lines.insert(hi+1, IL.rstrip()+"\n")
out=clean("".join(lines)
cnt=out.count("第233回")
assert cnt==2
w=io.open(P,"w",encoding="utf-8",newline="")
w.write(out; w.close
print("OK")
print("rowline",ki+1)
print("itrline",hi+2)
print("newlen",len(out)
print("count233",cnt)
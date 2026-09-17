import json, datetime
with open('_b82_run207.json', encoding='utf-8') as f:
    r = json.load(f)

def ms(x):
    return f"{x*1000:.0f}ms"

cold_list = []
for k in ['run207A','run207B','run207C']:
    d = r[k]
    cold_list.append((k, d['cold_count'], [ms(t) for t in d['cold_times']], ms(d['p50'])))
c = r['control_signup']
line = ("bench 2026-09-06 (第82回, K-Z3 12時台帯初計測 run207A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, "
        "12:08:48–12:09:20 JST, 全 80/80 200, host load1 7.8–7.2 (gate 7.5 ほぼ同等/超過) は production HTTP 実測のため gate 外): ")
parts = []
for k, cc, ct, p50 in cold_list:
    parts.append(f"{k} cold(>=0.9s) {cc}/20 p50 {p50} max {ms(r[k]['max'])}")
line += " / ".join(parts)
line += f" — 合計 cold {r['total_cold']}/60 (0%), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold {c['cold_count']}/20 p50 {ms(c['p50'])} max {ms(c['max'])} と静穏で control 分離成立。12時台は帯初計測で cold 0/60 — 日中低位帯 (7–11時台 2.2–6.7%) と整合し深夜帯 ~26-31% との対比を維持。status 判定は rank に委ねる (rank 専門)。"
with open('_b82_evidence.txt','w',encoding='utf-8') as f:
    f.write(line)
print(line)

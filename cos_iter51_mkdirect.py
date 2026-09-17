import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench49_kq1_warmquery.mjs").read()
src = src.replace('const API = "https://kotobase.net";', 'const API = "https://backend.kotobase.net";')
src = src.replace('"schema": "kotobase.benchmark.biscuit-auth-query.v1.bench49"',
                  '"schema": "kotobase.benchmark.biscuit-auth-query.v1.bench49-direct-backend"')
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_kq1_backenddirect.mjs", "w").write(src)
print("written")

old = '''(defn- public-upstream-json-headers [resp]
  (let [headers (js/Headers. #js {"content-type" "application/json"})
        retry-after (.. resp -headers (get "retry-after"))]
    (when (and (= 409 (.-status resp)) (string? retry-after)
               (re-matches #"[0-9]{1,4}" retry-after)
               (<= 1 (js/parseInt retry-after 10) 3600))
      (.set headers "retry-after" retry-after))
    (when-let [receipt-cid (read-audit-receipt-cid resp)]
      (.set headers "x-kotobase-read-audit-cid" receipt-cid))
    (when-let [statement-cid (read-audit-witness-statement-cid resp)]
      (.set headers "x-kotobase-read-audit-witness-statement-cid"
            statement-cid))
    headers))'''
new = '''(defn- public-upstream-json-headers [resp]
  (let [headers (js/Headers. #js {"content-type" "application/json"})
        retry-after (.. resp -headers (get "retry-after"))]
    (when (and (= 409 (.-status resp)) (string? retry-after)
               (re-matches #"[0-9]{1,4}" retry-after)
               (<= 1 (js/parseInt retry-after 10) 3600))
      (.set headers "retry-after" retry-after))
    (when-let [receipt-cid (read-audit-receipt-cid resp)]
      (.set headers "x-kotobase-read-audit-cid" receipt-cid))
    (when-let [statement-cid (read-audit-witness-statement-cid resp)]
      (.set headers "x-kotobase-read-audit-witness-statement-cid"
            statement-cid))
    ;; K-Q1 engine 内訳計測 (cosientist 第51回): pass through the engine's
    ;; per-request block-fetch summary (l1=..;l2=..;pack=..;b2=..;miss=..;
    ;; distinct=..). Counts only -- no CID values, no block bytes, no secrets.
    (when-let [kv-stats (.. resp -headers (get "x-kotobase-kv-stats"))]
      (when (re-matches #"[\\w;=]{1,200}" kv-stats)
        (.set headers "x-kotobase-kv-stats" kv-stats)))
    headers))'''
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/kotobase-api-gateway-cljs/src/kotobase/proxy.cljc"
s = open(p).read()
assert s.count(old) == 1, "old block count=%d" % s.count(old)
open(p, "w").write(s.replace(old, new))
print("patched")

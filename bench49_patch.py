path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/authn/scripts/live_biscuit_query_bench.mjs"
src = open(path).read()
old = '''    const query = await sample("authenticated query", SAMPLE_COUNT, () =>
      xrpc("datomic.q", { graph, db_name: runId, query_edn: queryEdn }),
    );'''
new = '''    const firstKvStats = firstQuery.response.headers.get("x-kotobase-kv-stats");
    const kvStatsSamples = [];
    const queryOnce = async () => {
      const result = await xrpc("datomic.q", { graph, db_name: runId, query_edn: queryEdn });
      if (result.response.ok) {
        kvStatsSamples.push({
          durationMs: Number(result.durationMs.toFixed(2)),
          kvStats: result.response.headers.get("x-kotobase-kv-stats"),
        });
      }
      return result;
    };
    await queryOnce();
    const query = await sample("authenticated query", SAMPLE_COUNT, queryOnce);'''
if old not in src:
    print("OLD NOT FOUND")
else:
    src2 = src.replace(old, new)
    src2 = src2.replace('        readAuditReceiptCid: readAuditCid,', '        readAuditReceiptCid: readAuditCid,\n        firstKvStats,')
    src2 = src2.replace('        authenticatedWarmQuery: query,', '        authenticatedWarmQuery: query,\n        kvStatsSamples,')
    open(path, "w").write(src2)
    print("PATCHED")

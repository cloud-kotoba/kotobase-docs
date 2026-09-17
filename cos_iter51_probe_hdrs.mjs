// Probe: does the deployed production Worker emit x-kotobase-kv-stats on any
// route reachable through the kotobase.net edge? Counts only, no secrets.
const BASE = "https://kotobase.net";
async function probe(label, path, init) {
  const r = await fetch(BASE + path, init);
  const h = r.headers.get("x-kotobase-kv-stats");
  console.log(label, r.status, "kv-stats:", h === null ? "ABSENT" : h);
  return h !== null;
}
let hits = 0;
hits += await probe("landing GET /", "/", { method: "GET" });
hits += await probe("q POST no-auth", "/xrpc/ai.gftd.apps.kotobase.datomic.q",
  { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({}) });
hits += await probe("search GET", "/xrpc/app.bsky.feed.searchPosts?q=test", { method: "GET" });
hits += await probe("health", "/health", { method: "GET" });
console.log("header_hits:", hits, "/ 4");

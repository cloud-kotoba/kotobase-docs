// cosient71 — transact 401 hypothesis tests (production HTTP, no local build).
// H-A (401 is the edge's bare "Unauthorized"): transact WITHOUT credentials.
// H-B (Biscuit viewer lacks data:write at edge): /xrpc/com.atproto.server.getSession (no data:write)
//      and /xrpc/app.bsky.feed.getTimeline (read) with the same Biscuit.
// H-C (nonce replay): two identical CACAO-transact posts are not possible without a CACAO minter;
//      skipped — H-A/B wire shapes suffice for the primary split.
// secret 不含。鍵は zero-fill (本スクリプトは鍵を生成しない — no credentials, wire shape only)。
const API = "https://kotobase.net";

async function step(name, path, headers, body) {
  const t0 = performance.now();
  let status, text;
  try {
    const r = await fetch(API + path, { method: "POST", headers, body: body ?? "{}" });
    status = r.status;
    text = await r.text();
  } catch (e) { status = -1; text = String(e).slice(0, 200); }
  const ms = Math.round((performance.now() - t0) * 100) / 100;
  console.log(JSON.stringify({ step: name, path, status, ms, body: text.slice(0, 300) }));
}

const json = { "content-type": "application/json" };
// minimal well-formed Biscuit-shaped header (NOT a real token — wire shape probe only)
const biscuitShape = "Biscuit " + "A".repeat(120);

await step("H-A-transact-noauth", "/xrpc/ai.gftd.apps.kotobase.datomic.transact", json,
  JSON.stringify({ db_name: "cosient71-ha", tx_edn: '[{ :db/id "x" :cosient71/probe "a" }]' }));
await step("H-B-biscuit-shape-getSession", "/xrpc/com.atproto.server.getSession", { ...json, authorization: biscuitShape }, "{}");
await step("H-B-biscuit-shape-timeline", "/xrpc/app.bsky.feed.getTimeline", { ...json, authorization: biscuitShape }, "{}");
await step("H-B-noauth-getSession", "/xrpc/com.atproto.server.getSession", json, "{}");
await step("control-landing-GET", "/api/auth/me", { ...json, authorization: biscuitShape }, "{}");
process.exit(0);

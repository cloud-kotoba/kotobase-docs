#!/usr/bin/env node
// K-Q1 companion: gateway auth-only check (authn verify hop) timing in same window
const API = "https://kotobase.net";
const AUTHN = "https://auth.kotobase.net";
const N = 30, WARM = 3;
async function timed(url, init = {}) {
  const t0 = performance.now();
  const res = await fetch(url, init);
  const text = await res.text();
  return { status: res.status, text, ms: performance.now() - t0 };
}
function pct(sorted, p) { return sorted[Math.max(0, Math.ceil(p * sorted.length) - 1)]; }
function stat(values) {
  const v = [...values].sort((a, b) => a - b);
  return { n: v.length, p50: +pct(v, 0.5).toFixed(2), p95: +pct(v, 0.95).toFixed(2), max: +v.at(-1).toFixed(2) };
}
const main = async () => {
  // unauth /api/auth/me (gateway auth short-circuit without valid biscuit → 401/403 response but same path)
  const gateway = [];
  for (let i = 0; i < WARM + N; i++) {
    const r = await timed(`${API}/api/auth/me`, { headers: { authorization: "Biscuit zzz" } });
    gateway.push(r.ms);
  }
  const authn = [];
  for (let i = 0; i < WARM + N; i++) {
    const r = await timed(`${AUTHN}/v1/session`, { headers: { authorization: "Biscuit zzz" } });
    authn.push(r.ms);
  }
  const out = {
    observedAt: new Date().toISOString(),
    gatewayAuthMeUnauth: stat(gateway.slice(WARM)),
    authnSessionUnauth: stat(authn.slice(WARM)),
  };
  console.log(JSON.stringify(out, null, 1));
};
main();

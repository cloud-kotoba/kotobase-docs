// K-Q1 切れ手(b): graph-for per-request 解決の local 実測
// client_api.cljc:81-85 graph-for = kotobase.graph/graph-cid-from-name の
// 忠実 port (sha2-256 via WebCrypto + base32 lower no-pad, I/O なし)。
// 測定法: claim contract 同形 (3 warmup 除外 + 30 sequential, nearest-rank)。
const te = new TextEncoder();
const B32 = "abcdefghijklmnopqrstuvwxyz234567";

function base32LowerNoPad(bytes) {
  const n = bytes.length;
  let bits = 0, value = 0, out = "";
  for (let i = 0; i < n; i++) {
    value = (value << 8) | bytes[i];
    bits += 8;
    while (bits >= 5) {
      out += B32[(value >>> (bits - 5)) & 31];
      bits -= 5;
    }
  }
  if (bits > 0) out += B32[(value << (5 - bits)) & 31];
  return out;
}

async function graphCidFromName(name) {
  const buf = await crypto.subtle.digest("SHA-256", te.encode(name));
  const hash = new Uint8Array(buf);
  const cid = new Uint8Array(36);
  cid[0] = 0x01; cid[1] = 0x71; cid[2] = 0x12; cid[3] = 0x20;
  cid.set(hash, 4);
  return "b" + base32LowerNoPad(cid);
}

const WARMUP = 3, N = 30;
// 合成 tenant 名 (secret 不含, 実 DID 形式のみ模倣)
const NAME = "kotobase/db/did:kotoba:bench0000000000000000/kq1-local-bench-db";

function nearestRank(sorted, p) {
  return sorted[Math.max(0, Math.ceil(p * sorted.length) - 1)];
}
const r3 = (v) => Number(v.toFixed(3));

const out = [];
out.push(`start ${new Date().toISOString()}`);
out.push(`node ${process.version}`);
out.push(`target: graph-cid-from-name replica (sha2-256 WebCrypto + base32), name len=${NAME.length}`);

// 自己検証: CID 形状 (bafyrei + 52 chars of a-z2-7)
const sample = await graphCidFromName(NAME);
const shapeOk = /^bafyrei[a-z2-7]{52}$/.test(sample);
out.push(`selfcheck: cid=${sample} shapeOk=${shapeOk}`);
if (!shapeOk) { console.error(out.join("\n")); process.exit(1); }

// 1) digest 単体
{
  const samples = [];
  for (let i = 0; i < WARMUP + N; i++) {
    const t0 = performance.now();
    await crypto.subtle.digest("SHA-256", te.encode(NAME));
    const dt = performance.now() - t0;
    if (i >= WARMUP) samples.push(dt);
  }
  const s = [...samples].sort((a, b) => a - b);
  out.push(`sha256-digest-only: n=${N} p50=${r3(nearestRank(s, 0.5))}ms p95=${r3(nearestRank(s, 0.95))}ms min=${r3(s[0])}ms max=${r3(s[N - 1])}ms`);
}

// 2) graph-for 全体 (= graph-cid-from-name: digest + base32)
{
  const samples = [];
  let cid = null;
  for (let i = 0; i < WARMUP + N; i++) {
    const t0 = performance.now();
    cid = await graphCidFromName(NAME);
    const dt = performance.now() - t0;
    if (i >= WARMUP) samples.push(dt);
  }
  const s = [...samples].sort((a, b) => a - b);
  out.push(`graph-for-full: n=${N} p50=${r3(nearestRank(s, 0.5))}ms p95=${r3(nearestRank(s, 0.95))}ms min=${r3(s[0])}ms max=${r3(s[N - 1])}ms`);
  out.push(`cid(final)=${cid}`);
}

out.push(`end ${new Date().toISOString()}`);
console.log(out.join("\n"));

import subprocess
r = subprocess.run(["gh", "pr", "create", "-R", "net-kotobase/docs",
                    "--base", "main", "--head", "cosient-sync-60",
                    "--title", "cosientist 第60回: K-Z3 22時台 run173A-C evidence + K-Q1 deploy run queued 継続確認",
                    "--body", "cosientist 第60回 tick (22:26–22:46 JST)。\n\n- K-Z3: 22時台 n 積み増し run173A–C を bench 第59回 run172 と同一測定法 (n=20 × 3 run + landing control, 別接続 curl, Tokyo) で実施。cold 1/0/0 = 1/60, control 静穏で分離成立。22時台通算 run172+173 で 120 試行中 6 試行 (~5%)。\n- K-Q1: deploy run 33964821723 (control-plane, workflow_dispatch) を gh 実査 — status=queued のまま (createdAt 2026-09-05T12:00:23Z, updatedAt 同一, jobs 空) で約 2.5 時間滞留。data plane の datomic.kotobase.net / には x-kotobase-kv-stats header 未到達を実測。次 tick 以降で failure 確定時は手動 wrangler deploy が代替経路 (rank 第58回記載どおり)。\n\nstatus 遷移なし (rank 専門)。"],
                    capture_output=True, text=True)
print("rc=", r.returncode)
print(r.stdout.strip()[:500])
print(r.stderr.strip()[:500])

cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "falsify 133: K-Z3 3hr(deep-night) first-measure run291A-C cold 2/60 ~3.3% (run291A single scatter 0.9367s #9, run291B single scatter 1.6194s #13, C 0/20 immediate-vanish, control 0/20 p50 42.3ms max 55.1ms completely-quiet sep established cold localized search; 3hr band-first 2/60, deep-night cum run275..291 24/1080 ~2.2% 18-set, heavy non-reproduced run271A+18, traffic-independence counter-evidence continues; status/rank to rank)"
git push net-kotobase HEAD:main
echo "push_rc=$?"
git fetch net-kotobase main
git rev-parse HEAD
git rev-parse net-kotobase/main
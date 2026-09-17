{
  pwd
  echo ===
  git rev-parse HEAD
  git rev-parse net-kotobase/main
  echo ===STATUS===
  git status --short
  echo ===LOG===
  git log --oneline -5
} > /tmp/rank_tick_probe.txt 2>&1

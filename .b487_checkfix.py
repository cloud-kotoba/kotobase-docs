import io
for path in [
  "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b487_append.py",
  "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b487_ilog.py",
]:
    with open(path, encoding="utf-8") as f:
        s = f.read()
    print(path, "日光帯 count:", s.count("日光帯"), "日中帯 count:", s.count("日中帯"))
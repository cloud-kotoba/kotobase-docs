for path in [
  "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b487_append.py",
  "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b487_ilog.py",
]:
    with open(path, encoding="utf-8") as f:
        s = f.read()
    a = s.count("日光帯")
    s = s.replace("日光帯", "日中帯")
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    print(path, "replaced", a)
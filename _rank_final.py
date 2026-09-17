import io
path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_rank_clean_out.txt'
with io.open(path, encoding='utf-8') as f:
    print(f.read())
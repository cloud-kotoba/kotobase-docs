import datetime
t0 = 1788843291.164105000
t1 = 1788843304.772986000
def jst(ts):
    return datetime.datetime.fromtimestamp(ts, datetime.timezone(datetime.timedelta(hours=9))).strftime('%H:%M:%S')
print("start JST", jst(t0))
print("end   JST", jst(t1))
print("elapsed_s %.1f" % (t1 - t0))
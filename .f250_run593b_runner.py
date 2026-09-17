import subprocess, time, math
URL='https://search.kotobase.net/search?q=test'
CTL='https://kotobase.net/signup'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'
def curl(url):
    t0=time.time()
    p=subprocess.run(['curl','-sA',UA,'-o','/dev/null','-w','%{http_code}',url],capture_output=True,text=True)
    return (time.time()-t0)*1000, p.stdout.strip()
res=[]
for label,url,fn in [('search',URL,'/tmp/fal_run593_B.ttfb'),('control',CTL,'/tmp/fal_run593_ctl2.ttfb')]:
    for i in range(20):
        ms,code=curl(url)
        with open(fn,'a') as f:
            f.write(f'{i+1}\t{code}\t{ms:.1f}\n')
        time.sleep(0.25)
def st(fn):
    rows=[l.split('\t') for l in open(fn).read().split('\n') if l.strip()]
    ms=sorted(float(r[2]) for r in rows if r[1]=='200')
    cold=[m for m in ms if m>=500]
    p50=ms[math.ceil(0.5*len(ms))-1]
    return f'n200={len(ms)}/20 cold={len(cold)} p50={p50:.1f} max={ms[-1]:.1f} coldv={[round(m,4) for m in cold]}'
print('search B:', st('/tmp/fal_run593_B.ttfb'))
print('control :', st('/tmp/fal_run593_ctl2.ttfb'))
print('time:', time.strftime('%H:%M:%S'))

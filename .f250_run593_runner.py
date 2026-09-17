import subprocess, time, json
URL='https://search.kotobase.net/search?q=test'
CTL='https://kotobase.net/signup'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36'
def curl(url):
    t0=time.time()
    p=subprocess.run(['curl','-sA',UA,'-o','/dev/null','-w','%{http_code}',url],capture_output=True,text=True)
    return (time.time()-t0)*1000, p.stdout.strip()
for label,url,fn in [('search',URL,'/tmp/fal_run593_A.ttfb'),('control',CTL,'/tmp/fal_run593_ctl.ttfb')]:
    for i in range(20):
        ms,code=curl(url)
        with open(fn,'a') as f:
            f.write(f'{i+1}\t{code}\t{ms:.1f}\n')
        time.sleep(0.25)
print('done')

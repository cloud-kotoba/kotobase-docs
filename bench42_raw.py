import hashlib
data = open("bench42_out.txt","rb").read()
print(len(data), hashlib.sha256(data).hexdigest()[:16])
print(repr(data))

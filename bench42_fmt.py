COLD = 0.5
print("fmt: cold(>=%.1fs)" % COLD)
print("f-string:", "cold(>=%.1fs)".__mod__(COLD))
import sys
print("python:", sys.version)
print("float hex:", float(COLD).hex())

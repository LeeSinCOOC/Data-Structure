import sys
old = sys.getrecursionlimit()
print(old)

sys.setrecursionlimit(10000)
new = sys.getrecursionlimit()
print(new)

def norm(v,p):
    lp = 0
    for i in v:
        lp += i**p
    return pow(lp,(1/p))

v = [3,4]
a = norm(v,3)
print(a)
        

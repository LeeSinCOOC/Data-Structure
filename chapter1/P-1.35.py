from random import randrange

count_s = 0
count_l = 0
l = []
n = 0
for i in range(1000):
    while n < 23:
        l.append(randrange(1,365))
        n += 1
    s = set(l)
    if len(s) < len(l):
        count_s += 1
    else:
        count_l += 1
print(count_s/(count_s+count_l))

#循环1000次后，此结论就十分逼近了，所以生日悖论不是悖论

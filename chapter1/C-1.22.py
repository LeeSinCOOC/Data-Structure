def dot(a,b):
    c = []
    i = 0
    while i < len(a):
        c.append(a[i]*b[i])
        i += 1
    return c

a = [1,2,3]
b = [1,2,3]

x = dot(a,b)
print(x)
        
        

def minmax(data):
    s = str(data)
    min_d = int(s[0])
    max_d = int(s[0])
    for i in s:
        if min_d > int(i):
            min_d = int(i)
        if max_d < int(i):
            max_d = int(i)
    return (min_d,max_d)

a = minmax(312)
print(a)
            
        

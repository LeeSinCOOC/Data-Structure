def findmax(data,n):
    max_ = data[0]
    for i in data[1:]:
        if i > max_:
            max_ = i
    return max_

def max_(data,n):
    if n < 2:
        return data[0]
    if n == 2:
        return data[0] if data[0] > data[1] else data[1]
    return data[0] if data[0] > max_(data[1:],n-1) else max_(data[1:],n-1)

S = [1,2,3,5,1,2,1]
n = len(S)

a = max_(S,n)
print(a)
        
    
    

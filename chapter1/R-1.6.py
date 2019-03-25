def squ_o(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 :
            sum += i*i
    return sum

a = squ_o(4)
print(a)
    

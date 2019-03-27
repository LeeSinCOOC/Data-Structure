def recursion_sum(S,n):
    if n == 0:
        return 0
    else:
        return recursion_sum(S,n-1) + S[n-1]

S = [1,2,3,4]
n = len(S)

a = recursion_sum(S,n)
print(a)
    

def isabel(A,B):
    n = len(A)//2
    for i in range(n):
        B.append(A[2*i] + A[2*i + 1])
    if len(A) % 2 == 1:
        B.append(A[-1])
    if len(B) == 1:
        return B[0]
    else:
        C = []
        return isabel(B,C)
        


A = list(range(101))
B = []
a = isabel(A,B)
print(a)

# 重点阅读，自己都不知道怎么莫名其妙写出了的

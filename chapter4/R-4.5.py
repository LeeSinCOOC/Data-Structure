from itertools import combinations,permutations

k = 3
S = []
U = ['a','b','c','d']

for i,j,k in permutations(U,3):#排列
    print(i,j,k)

print('*'*10)

for i,j,k in combinations(U,3):#组合
    print(i,j,k)


# 递归？

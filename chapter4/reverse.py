def reverse(S,start,stop):
    if start < stop-1:
        S[start],S[stop-1] = S[stop-1],S[start]
        reverse(S,start+1,stop-1)
    return S

# 注意可变不可变 S =  'abcdefg' 因为字符串不可变，此处报错不能迭代
S = [1,2,3,4,5,6]
a = reverse(S,0,len(S))
print(a)

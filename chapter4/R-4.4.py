def reverse(S,start=0,end=5):
    if start >= end-1:
        return S[start]
    S[start],S[end-1] = S[end-1],S[start]
    reverse(S,start+1,end-1)
    return S
    
S = [4,3,6,2,6]
a = reverse(S,0,5)
print(a)

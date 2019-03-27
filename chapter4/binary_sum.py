def binary_sum(S,start,stop):
    if start == stop:
        return 0
    elif start == stop-1:
        return S[start]
    else:
        mid = (stop+start)//2
        return binary_sum(S,start,mid) + binary_sum(S,mid,stop)

S = [1,2,3,4,5,6]
a = binary_sum(S,0,len(S))
print(a)

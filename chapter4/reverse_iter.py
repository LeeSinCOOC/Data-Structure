def reverse_iter(S):
    start = 0
    stop = len(S)-1
    while start < stop:
        S[start],S[stop] = S[stop],S[start]
        start += 1
        stop -= 1
    return S

S = [1,2,3,4,5]
a = reverse_iter(S)
print(a)

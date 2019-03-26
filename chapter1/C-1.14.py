def mul_diff(n_list):
    l = []
    for i in n_list:
        if i%2 == 1:
            l.append(i)
    l = list(set(l))
    if len(l) >= 2:
        return True
    return False
        

n_list = [1,2,3,4,5]
a = mul_diff(n_list)
print(a)

    

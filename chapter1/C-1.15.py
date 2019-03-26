def N_diff(n_list):
    a = len(n_list)
    b = len(set(n_list))

    if a == b:
        return True
    return False

n_list = [1,2,3,4,5,1]
a = N_diff(n_list)
print(a)

def is_even(k):
    if int(bin(k)[-1]):
        return False
    return True


a = is_even(1.1)
print(a)
        

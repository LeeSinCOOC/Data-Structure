def only1(s):
    for i in s[1:]:
        if s[0] == i:
            return False
    return True
def main(s):
    if len(s) == 1:
        return True
    if only1(s):
        main(s[1:])
        return True
    return False
        
s = [1,2,3,4,5,1,5,5]
a = main(s)
print(a)

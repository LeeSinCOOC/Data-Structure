def count(s):
    a = ['a','e','i','o','u']
    count = 0 
    s = s.lower()
    for i in s:
        if i in a:
            count += 1
    return count

s = 'Abcd Efg'
a = count(s)
print(a)

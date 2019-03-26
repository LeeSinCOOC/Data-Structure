n = int(input('输入大于2的正整数:'))
count = 0
if n <= 2:
    print('输入错误')
while True:
    if n <= 2:
        break
    n //= 2
    count += 1

print(count)

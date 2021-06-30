a = int(input())
counter = 0
while a != 0:
    num = a % 10
    if num == 1:
        counter += 1
    a = a // 10
if counter > 0:
    print('YES')
else:
    print('NO')
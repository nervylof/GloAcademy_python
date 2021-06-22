a = int(input())
b = a
total = 0
while a != 0:
  last_digit = a % 10
  total += last_digit
  a = a // 10
#print(b)
if b % total == 0:
  print('YES')
else:
  print('NO')

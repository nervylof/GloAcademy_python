n = int(input())
counter = 0
for i in range(n):
  num = int(input())
  if num % 2 == 1:
    counter += 1
if counter == n:
  print('YES')
else:
  print('NO')


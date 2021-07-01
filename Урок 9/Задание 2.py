a = int(input())
counter = 0
for i in range(1, a + 1):
  if a % i == 0:
    counter += 1
if counter == 2:
  print ('YES')
else:
  print('NO')
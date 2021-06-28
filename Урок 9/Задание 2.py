from typing import Counter


a = int(input())
counter = 0
for i in range(1, 100):
  if a % i == 0:
    counter += 1
if counter == 2:
  print ('YES')
else:
  print('NO')

num = int(input())
flag_1 = 0
flag_2 = 0
if num > 0:
  flag_1 += 1
if num < 0:
  flag_2 += 1
while num != 0:
  num = int(input())
  if num > 0:
    flag_1 += 1
  if num < 0:
    flag_2 += 1
total = flag_1 * flag_2
print(total)

num = int(input())
f = 0
while num != 0:
  num = int(input())
  if num < 10:
    continue
  elif num > 100:
    break
  if num > 10 and num < 100:
    f = num 
print(f)
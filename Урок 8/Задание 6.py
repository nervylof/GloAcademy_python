num = int(input())
total = 0
counter = 0
while num != 0:
  total += num
  counter += 1
  num = int(input())
total = total // counter
print(total)

def num_goods(num):
  counter = 100
  if num == 1:
    counter = counter
  elif num > 1:
    for i in range(num - 1):
      counter += 50
  return counter
delivery = int(input())
print(num_goods(delivery))
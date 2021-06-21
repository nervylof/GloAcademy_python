n = int(input())
maximum = n
minimum = n
if n == 2 or n > 2:
  for i in range(n):
    num = int(input())
    if num > maximum:
      maximum = num
    elif num < minimum:
      minimum = num
  print('Максимум равен', maximum)
  print('Минимум равен', minimum)
    
    
      

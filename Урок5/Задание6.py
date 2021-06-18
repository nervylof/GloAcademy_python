num = int(input())
if num < 0 or num > 36:
  print('Ошибка ввода!')
elif num == 0:
  print('ZERO!')
elif num > 0 and num < 11 and num % 2 == 0:
  print('BLACK!')
elif num > 18 and num < 29 and num % 2 == 0:
  print('BLACK!')
elif num > 10 and num < 19 and num % 2 == 1:
  print ('BLACK!')
elif num > 28 and num < 37 and num % 2 == 1:
  print('BLACK!')
else:
  print('READ!')






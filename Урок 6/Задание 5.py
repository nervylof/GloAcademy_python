print('Введите ваш email:')
email = input()
if '@' in email and '.' in email:
  print('Корректный')
else:
  print('Некорректный')
def max_digits(list):
  max_num = 0
  for i in range(len(list)):
    if int(list[i]) > max_num:
      max_num = int(list[i])
  return max_num

numbers_1 = input(print('Ввод числел через пробел: ', end=''))
numbers_2 = input(print('Ввод числел через пробел: ', end=''))
numbers_1 = numbers_1.split()
numbers_2 = numbers_2.split()
print(max_digits(numbers_1), max_digits(numbers_2))
print(max_digits(numbers_1) * max_digits(numbers_2))

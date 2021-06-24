num = int(input())
maximum = 1
minimum = 9
while num == 10 or num > 10:
  last_digit = num % 10
  num = num // 10
  if last_digit > maximum:
    maximum = last_digit
  if minimum > last_digit:
    minimum = last_digit
print('Максимальная цифра равна', maximum)
print('Минимальная цифра равна', minimum)
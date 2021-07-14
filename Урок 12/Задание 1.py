def rem_digits(num):
  counter = 0
  while num != 0:
    num % 10
    counter += 1
    num = num // 10
  return counter
num1 = int(input())
num2 = int(input())
print(rem_digits(num1) * rem_digits(num2))
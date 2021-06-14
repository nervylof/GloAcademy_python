num_ticket = int(input())
a = (num_ticket // 100000)
b = (num_ticket // 10000 % 10)
c = (num_ticket // 1000 % 10)
#print(a, b, c)
a_1 = (num_ticket // 100 % 10)
b_1 = (num_ticket // 10 % 10)
c_1 = (num_ticket // 1 % 10)
#print(a_1, b_1, c_1)
num_1 = (a + b + c)
num_2 = (a_1 + b_1 + c_1)
if num_1 == num_2:
  print('Билет', num_ticket, 'счастливый')
else:
  num_1 != num_2
  print('Билет', num_ticket, 'несчастливый')
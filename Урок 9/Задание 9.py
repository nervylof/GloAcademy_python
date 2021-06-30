n = int(input())
total_1 = 0
total_2 = 0
while n != 0:
    num_1 = n % 10
    total_1 += num_1
    n = n // 10
while total_1 != 0:
    num_2 = total_1 % 10
    total_2 += num_2
    total_1 = total_1 // 10
print(total_2)
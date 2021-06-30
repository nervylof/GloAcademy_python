n = int(input())
counter = 0
for i in range(1, n + 1):
    num = i % 10
    if num == 5:
        counter += 1
print(counter)

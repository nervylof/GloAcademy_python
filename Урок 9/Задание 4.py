n = int(input())
for i in range(1, n + 1):
    if i > 1 and i < 9:
        continue
    if i > 127 and i < 257:
        continue
    if i > 1023 and i < 2049:
        continue
    print(i)

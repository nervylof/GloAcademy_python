while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    elif num > 10 or num < 101:
        a = num
    num = int(input())
    print(a)

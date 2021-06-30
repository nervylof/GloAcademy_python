for h in range(25):
    for m in range(60):
        for s in range(61):
            if h < 10:
                print(0, h, sep='', end='')
            else:
                print(h, end='')
            print(':', end='')
            if m < 10:
                print(0, m, sep='', end='')
            else:
                print(m, end='')
            print(':', end='')
            if s < 10:
                print(0, s, sep='', end='')
            else:
                print(s, end='')
                
            print()


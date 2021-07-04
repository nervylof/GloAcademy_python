sym = input()
if ord(sym) == ord('A') or ord(sym) == ord('Z') or ord(sym) > ord('A') and ord(sym) < ord('Z'):
    print(sym.lower())
elif ord(sym) == ord('a') or ord(sym) == ord('z') or ord(sym) > ord('a') and ord(sym) < ord('z'):
    print(sym.upper())
else:
    print(sym)
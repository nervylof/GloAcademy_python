sym = input()
flag_1 = 0
flag_2 = 0
#for i in range(ord('A'), ord('Z') + 1):
if ord(sym) == ord('A') or ord(sym) == ord('Z') or ord(sym) > ord('A') and ord(sym) < ord('Z'):
  flag_1 += 1
#for a in range(ord('a'), ord('z') + 1):
if ord(sym) == ord('a') or ord(sym) == ord('z') or ord(sym) > ord('a') and ord(sym) < ord('z'):
  flag_2 += 1
if flag_1 > 0:
  print(sym.lower())
elif flag_2 > 0:
  print(sym.upper())
else:
  print(sym)
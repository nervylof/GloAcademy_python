sym_1 = input()
sym_2 = input()

for b in range(ord(sym_2), ord(sym_1) + 1):
  print(chr(b), end=' ')
for i in range(ord(sym_1), ord(sym_2) + 1):
  print(chr(i), end=' ')
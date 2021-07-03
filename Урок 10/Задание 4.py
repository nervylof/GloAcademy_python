sym = input()
flag_1 = 0
flag_2 = 0
for i in range(ord('A'), ord('Z') + 1):
  if sym == chr(i):
    flag_1 += 1
  for a in range(ord('a'), ord('z') + 1):
    if sym == chr(a):
      flag_2 += 1
if flag_1 > 0:
  print(sym.lower())
elif flag_2 > 0:
  print(sym.upper())
else:
  print(sym)
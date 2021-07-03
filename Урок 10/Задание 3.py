n = input()
if ord(n) == ord('A') or ord(n) > ord('A') and ord(n) == ord('Я') or ord(n) < ord('Я'):
  print('YES')
else:
  print('NO')
#counter = 0
#for i in range(ord('А'), ord('Я') + 1):
  #if n == chr(i):
    #counter += 1
#if counter > 0:
  #print('YES')
#else:
  #print('NO')
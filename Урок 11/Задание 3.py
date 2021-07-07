s = input()
id = s.split('.')
if len(id) > 4:
  print('False')
elif int(max(id)) >= 256:
  print('NO')
else:
  print('YES')
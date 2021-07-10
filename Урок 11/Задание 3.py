s = input()
flag = 0
id = s.split('.')
if len(id) != 4:
  print('False')
for i in range(len(id)):
  if int(id[i]) < 0 or int(id[i]) >= 256:
    flag += 1
  else:
    continue
if flag >= 1:
  print('NO')
else:
  print('YES')
#elif int(max(id)) >= 256:
  #print('NO')
#else:
  #print('YES')
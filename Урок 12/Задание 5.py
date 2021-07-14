def star_date(list):
  list = list.split('.')
  if len(list) > 3:
    print('False')
  total = int(list[0]) * int(list[1])
  if total != (int(list[2]) % 100):
    False
  else:
    True
  return
date = input()
print(star_date(date))

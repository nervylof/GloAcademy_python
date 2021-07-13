num = int(input())
list = []
for i in range(num):
  string = input()
  #s = string.lower()
  list.append(string)
print(list)
query = input()
for a in range(len(list)):
  if list[a].lower().count(query):
    print(list[a])
  #print(list[a])


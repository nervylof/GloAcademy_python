s = input()
new_s = ''
for i in range(len(s)):
    if s[i].isdigit():
        new_s += s[i]
    else:
        continue
print(new_s)


article_1 = (input())
article_2 = (input())
article_3 = (input())
num_1 = len(article_1)
num_2 = len(article_2)
num_3 = len(article_3)
#print(num_1)
#print(num_2)
#print(num_3)
print('В данной статье больше симвлов:')
if num_1 > num_2 and num_1 > num_3:
  print(article_1)
elif num_2 > num_3:
  print(article_2)
else:
  print(article_3)





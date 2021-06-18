article_1 = str(input())
article_2 = str(input())
article_3 = str(input())
num_1 = len(article_1)
num_2 = len(article_2)
num_3 = len(article_3)
#print(num_1)
#print(num_2)
#print(num_3)
if num_1 > num_2 and num_1 > num_3:
  print(article_1)
elif num_2 > num_1 and num_2 > num_3:
  print(article_2)
elif num_3 > num_1 and num_3 > num_2:
  print(article_3)





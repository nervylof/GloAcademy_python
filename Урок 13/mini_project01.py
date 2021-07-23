import random
print('Hello, you came to play the game "Guess the number"')

print('Enter the number to which you would like to guess :) :', end=' ')

n = int(input())

def is_valid(user_input):
    global n
    if user_input.isdigit():
        user_number = int(user_input)

        if user_number >= 1 and user_number <= n:
            return True
        else:
            return False
    else:
        return False


secret_num = random.randint(1, n)
counter = 0
while True:
    print('Enter the number:', end=' ')
    user_input = input()
    if not is_valid(user_input):
        continue
    user_number = int(user_input)
    counter += 1
    if secret_num > user_number:
        print('The guessed number is greater than the entered number, try again:')
    elif secret_num < user_number:
        print('The guessed number is less than the entered number, try again:')
    if secret_num == user_number:
        print('Victory!')
        print('You ve got it over with', counter, 'attempts!')
        user = int(input('One more time ? if yes then send 1, if not then 0: '))
        if user == 1:
            print('Enter the number to which you would like to guess :) :', end=' ')
            n = int(input())
            counter = 0
            secret_num = random.randint(1, n)
            continue
        else:
            print('Goodbye! Waiting for you again!')
            break
    



        


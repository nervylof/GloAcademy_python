import random
import string

def update_user_word(secret_word, user_word, char):

    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word

def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1:
            return True
        else:
            return False
    else:
        return False

def valid_user_char(user_char):
    count = 0
    for i in range(ord('А'), ord('я') + 1):
        if (user_char) == chr(i):
            count += 1

    if count > 0:
        return True
    if user_char == ' ':
        return True

           
secret_words = []
user_word = ''

print('Привет это игра "Поле чудес", запиши следующим сколько бы слов ты бы хотел угадывать')

while True:
    num_word = input()
    if not is_valid(num_word):
        print('Введите пожалйуста цифру')
        continue
    else:
        num_word = int(num_word)
        
    for i in range(num_word):
        print('Запиши', i + 1, 'слово, которе мы добавим в список угадываемых')
        word = input()
        secret_words.append(word)
        
    secret_word = random.choice(secret_words)
    
    for i in range(len(secret_word)):
        user_word += '*'

    break



print('Ваше загаданное слово состоит из', len(secret_word), 'букв')

count = 0

while True:
    secret_word = secret_word.lower()
    print('Введите пожалуйста одну букву!')
    user_char = input()
    if not valid_user_char(user_char):
        print('Эта буква не русского алфавита')
        continue  
    user_char = user_char.lower()
    if len(user_char) != 1:
        continue
    new_user_word = update_user_word(secret_word, user_word, user_char)

    if user_word == new_user_word:
        print('К сожалению, такой буквы нет в слове')
    else:
        print('Поздравляю, такая буква есть')
        count += 1

    user_word = new_user_word

    print(user_word.capitalize())

    if user_word == secret_word:
        print('Ура, вы отгадали слово!')
        print('Вы отгадали слово за', count, 'попыток')
        print('Хотите сыграть еще раз? Ответьте "Да" или "Нет"')
        repid = input()
        repid = repid.capitalize()
        if repid == 'Да':
            print('Ну чтож, поехали еще раз)')
            continue
        else:
            print('Пока, буду рад еще раз с тобой сыграть)')
            break
import random

def is_valid(user_input):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1:
            return True
        else:

            return False
    else:
        return False

def ask_question(question):
    print(question, 'Нажмите Да или Нет')
    answer = input()
    answer = answer.capitalize()
    if answer == 'Да':
        return True
    else:
        return False

def generate_pass(len_pas, chars):
    password = ''
    if len(chars) < 1:
        print('Вы ничего не выбрали!')
        return False
    else:
        for i in range(len_pas):
            random_index = random.randint(0, len(chars) - 1)
            password += chars[random_index]
        return password


print('Привет я генератор паролей. Сейчас я задам несколько вопрос что бы сгенерировать удобный для тебя пароль)')
while True:
        print('Сколько паролей ты бы хотел сгенерировать?')
        num_password = input()
        if not is_valid(num_password):
            print('Введи пожалуйста число больше 0)')
            continue
        while True:
            print('Введите длину пароля')
            user_input = input()
            if not is_valid(user_input):
                print('Это не корректное число!')
                continue

            len_pas = int(user_input)


            latin_lower_enabled = ask_question('Включать ли латинские буквы нижнего регистра?')
            latin_upp_enabled = ask_question('Включать ли латинские буквы верхнего регистра?')
            rus_lower_enabled = ask_question('Включать ли русские буквы нижнего регистра?')
            rus_upp_enabled = ask_question('Включать ли русские буквы верхнего регистра?')
            digits_enabled = ask_question('Включать ли цифры?')
            punctuation_enabled = ask_question('Включать знаки пунктуации?')
            

            enabled_chars = ''

            digits = '0123456789'
            latin_lower_letters = 'abcdefghijklmnopqrstuvwxyz'
            latin_upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            rus_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            rus_upper_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            punctuation = '!#$%&*-+=?@^_'

            if digits_enabled:
                enabled_chars += digits

            if latin_lower_enabled:
                enabled_chars += latin_lower_letters

            if latin_upp_enabled:
                enabled_chars += latin_upper_letters

            if rus_lower_enabled:
                enabled_chars += rus_lower_letters

            if rus_upp_enabled:
                enabled_chars += rus_upper_letters

            if punctuation_enabled:
                enabled_chars += punctuation


            for i in range(int(num_password)):
                password = generate_pass(len_pas, enabled_chars)
                
                print(password)


            print('Если данные пароли тебя не устраивают, то ты можешь запустить генерацию второй раз. Ответь 1 или 0')
            while True:
                user = input()
                if user != '1' and user != '0':
                    print('Введите 0 или 1!')
                    continue
                else:
                    user = int(user)
                    break
            break
        if user == 1:
            print('Привет! Придется ответить на вопросы еще раз)')
            continue
        else:
            print('Прощай! Буду рад помочь в следующий раз!')
            break


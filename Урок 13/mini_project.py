import random
print('������, �� ����� �������� � ���� "������ �����"')

print('����� ����� �� �������� �� �� ������ ���������:) :', end=' ')


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
    print('������� �����:', end=' ')
    user_input = input()
    if not is_valid(user_input):
        continue
    user_number = int(user_input)
    counter += 1
    if secret_num > user_number:
        print('���������� ����� ������ ��� ���������, �������� ��� ���:')
    elif secret_num < user_number:
        print('���������� ����� ������ ��� ���������, �������� ��� ���:')
    if secret_num == user_number:
        print("������")
        print('� ���� ���������� �', counter, '�������!')
        user = int(input("��� ����� ? ���� �� �� ������� 1, ���� ��� �� 0: "))
        if user == 1:
            print('����� ����� �� �������� �� �� ������ ���������:) :', end=' ')
            n = int(input())
            counter = 0
            secret_num = random.randint(1, n)
            continue
        else:
            print('������! ��� ���� �����!')
            break
    



        


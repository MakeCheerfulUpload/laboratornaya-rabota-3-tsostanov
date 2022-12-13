import re

my_isy_number = 367550
# 1 часть
print('Задание 1')
print('Мой вариант:', my_isy_number % 6, my_isy_number % 4, my_isy_number % 7, '\n')
my_smile = 'X-{)'
with open('input.txt', 'r', encoding='utf-8') as f:
    for current_string in f.readlines():
        print(f'Количество вхождений искомого смайлика {my_smile} в сообщении:',
              ''.join(re.findall(r'[^\n]', current_string)), '-', (len(re.findall(r"X-\{\)", current_string))))

# 2 часть
print('\n' + 'Дополнительное задание 1')
print('Мой вариант:', my_isy_number % 6, '\n')
with open('thesis.txt', 'r', encoding='utf-8') as f:
    for current_thesis in f:
        default_thesis = current_thesis
        current_thesis = re.sub(r'[-.,!?<>\s]', ' ', current_thesis)
        current_thesis = re.sub(r' {2,}', ' ', current_thesis)
        answer = set()
        # for length in range(5):
        #     pattern = ''.join(['\\bВТ\\b(?:[\s\-,]+\w+){', str(length), '}[\s\-,]+\\bИТМО\\b'])
        #      answer.update(re.findall(pattern, current_thesis))
        #  answer = sorted(answer, key=len)
        #  I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE = ''
        #  for i in answer:
        #      I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE += f'{i};'
        #  print(f'В сообщении "{default_thesis.strip()}" встречаются следующие подстроки: '
        #        + I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE[:-1])
        # Не учитывает строчки с наложением
        for index in range(len(re.findall(r'\bВТ\b', current_thesis))):
            current_thesis = re.sub(r'.*?\bВТ', '-', current_thesis, 1)
            words = current_thesis.split()
            delta_thesis = 'ВТ'
            for i in range(1, min(4, len(current_thesis.split()))):
                delta_thesis += ' ' + (current_thesis.split())[i]
                if re.fullmatch(r'.+\bИТМО', delta_thesis):
                    answer.add(delta_thesis)
        answer = sorted(answer, key=len)
        I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE = ''
        for i in answer:
            I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE += f'{i};'
        print(f'В сообщении "{default_thesis.strip()}" встречаются следующие подстроки: '
              + I_REALLY_WANT_TO_STAY_AT_YOUR_HOUSE[:-1])

# 3 часть
print('\n' + 'Дополнительное задание 2')
print('Мой вариант:', my_isy_number % 5, '\n')
with open('emails.txt', 'r', encoding='utf-8') as f:
    for current_email in f.readlines():
        current_server = re.findall(r'((?:\w|\.)+@([A-Za-z]+\.[A-Za-z]+))', current_email)
        try:
            print('Неверный формат ввода!' if (current_server[0][0] != current_email.strip()) else
                  f'У почтового адреса {current_email.strip()} почтовый сервер - {current_server[0][1]}')
        except:
            print('Неверный формат ввода!')

''' Дополнительное задание с защиты
string = 'asq <af wqfwg webadgni>Бagea > qqh  pavf GRG'
print(*re.findall(r'<(.*?)>', string))
'''

print('Вы поедете на бал?')
answer = input('Ответ: ').lower()

if answer not in ('да', 'нет'):
    print('Верно')
else:
    print('Неверно')

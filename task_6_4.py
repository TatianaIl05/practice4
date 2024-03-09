first_team, second_team = map(int, input('Введите счёт: ').split(':'))
if first_team > second_team:
    print(1)
elif second_team > first_team:
    print(2)
else:
    print(0)

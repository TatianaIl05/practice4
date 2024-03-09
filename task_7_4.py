kirill_res, arina_res, sergei_res = map(int, input('Введите рекорды Кирилла, Арины и Сергея: ').split())
if kirill_res >= arina_res:
    if sergei_res >= kirill_res:
        print(sergei_res)
    else:
        print(kirill_res)
elif sergei_res >= arina_res:
    print(sergei_res)
else:
    print(arina_res)

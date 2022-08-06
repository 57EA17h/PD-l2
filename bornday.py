typed_bornyear = int(input('Type born year of Pushkin'))


if typed_bornyear == 1799:
    typed_bornday = int(input('Type born day of Pushkin'))
    if typed_bornday == 6:
        print('Верно')
    else:
        print('Неверный день рождения')

else:
    print('Неверный год')

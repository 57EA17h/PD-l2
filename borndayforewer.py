

while True:
    typed_bornyear = int(input('Type born year of Pushkin'))
    if typed_bornyear == 1799:
        while True:
            typed_bornday = int(input('Type born day of Pushkin'))
            if typed_bornday == 6:
                print('Верно')
                break
            else:
                print('Incorrect.')
        break
    else:
        print('Incorrect.')

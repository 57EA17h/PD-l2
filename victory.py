# Tolstoy 1883
byear_tolstoy = 1883
# Mendeleev 1834
byear_mendeleev = 1834
# Popov 1859
byear_popov = 1859
# Gagarin 1934
byear_gagarin = 1934
# Gogol 1809
byear_gogol = 1809

a_correct = 0
a_incorrect = 0

while True:
    print('Welcome to quiz!')
    a_tolstoy = int(input('Type born year of L. Tolstoy'))
    if a_tolstoy == byear_tolstoy:
        a_correct += 1
    else:
        a_incorrect += 1

    a_mendeleev = int(input('Type born year of D. Mendeleev'))
    if a_mendeleev == byear_mendeleev:
        a_correct += 1
    else:
        a_incorrect += 1

    a_popov = int(input('Type born year of A. Popov'))
    if a_popov == byear_popov:
        a_correct += 1
    else:
        a_incorrect += 1

    a_gagarin = int(input('Type born year of Yu. Gagarin'))
    if a_gagarin == byear_gagarin:
        a_correct += 1
    else:
        a_incorrect += 1

    a_gogol = int(input('Type born year of N. Gogol'))
    if a_gogol == byear_gogol:
        a_correct += 1
    else:
        a_incorrect += 1

    print('You results:')
    print('Right answers:', a_correct, 'answers.', (a_correct / (a_correct + a_incorrect))*100, 'percents')
    print('Wrong answers:', a_incorrect, 'answers.', (a_incorrect / (a_correct + a_incorrect))*100, 'percents')

    want_retry = input('Would you like to try again? type "yes" for start, press enter for exit')

    if want_retry == 'yes':
        a_correct = 0
        a_incorrect = 0
    else:
        break

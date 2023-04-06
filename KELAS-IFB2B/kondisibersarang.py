
menu = input('Mau makan apa = ')

if menu == 'nasi campur':
    
    warung = input('Mau makan di mana = ')

    if warung == 'pontianak':
        print('Enak kah di situ...')

    else:
        print('warungnya tidak ada')

elif menu == 'rawon':
    
    warung = input('Mau makan di mana = ')

    if warung == 'pak de':
        print('boleh juga...')

    elif warung == 'budeh':
        print('enak di situ..')
    else:
        print('warungnya tidak ada')
else:
    print('menunya tidak tersedia')

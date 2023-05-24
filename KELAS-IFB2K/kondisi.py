#kondisi tungaal cuma 1 IF

# jika anda pilih makan iya maka silahkan ke dapur ambil makan
#jika anda tidak makan maka anda duduk di sini aja
'''
pilihan = 't'

if pilihan == 'iya':
    print('SIlahkan ke dapur ambil makan')
else:
    print('anda duduk di sini aja')
'''

#if jamak
warung = ''
menu = input('Silahkan Pilih Menu = ')

if menu == 'nasi goreng':
    #print('Kita makan di warung arema')
    warung = input('Mau makan di warung mana = ')

    if warung == 'arema':
        print('Kita makan di warung arema')
    elif warung == 'tegal':
        print('Kita makan di warung tegal')
    else:
        print(f'maaf.. Warung {warung} tidak menyediakan menu {menu}..')

elif menu == 'bakso':
    warung = input('Mau makan di warung mana = ')
    if warung == 'wardoyo':
        print('Kita makan di warung wardoyo')
    elif warung == 'kolor ijo':
        print('Kita makan di warung kolor ijo')
    else:
        print(f'maaf.. Warung {warung} tidak menyediakan menu {menu}..')

else:
    print('Maaf.. menu tersebut tidak tersedia')


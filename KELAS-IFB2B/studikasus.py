
# menu 
print('===== MENU MAKANAN =====')
print('1. Nasi goreng \n\t1.1 nasi goreng seafood \n\t1.2 nasi goreng mawut')
print('2. Bakso \n\t2.1 Bakso Popye \n\t2.2 Bakso Beranak ')

keterang = ''
ketMenu = ''
pilihMenu = ''
harga = 0

menu = input('Silahkan Pilih Menu = ')

if menu == 'NASI GORENG':
    print('====LIST NASI GORENG ====')
    print('1. nasi goreng seafood 2. nasi goreng mawut')

    pilihMenu = input('Pilih Nasi Goreng Apa = ')
    if pilihMenu == 'NASI GORENG SEAFOOD':
         harga = 30000
    elif pilihMenu == 'NASI GORENG MAWUT':
         harga = 25000
    else:
         ketMenu = 'Nasi Goreng Yang Anda Mau tidak ada'

elif menu == 'BAKSO':
    print('==== LIST BAKSO ====')
    print('1.Bakso Popye 2.Bakso Beranak ')

    pilihMenu = input('Pilih Bakso Apa = ')
    if pilihMenu == 'BAKSO POPY':
         harga = 20000
    elif pilihMenu == 'BAKSO BERANAK':
         harga = 25000
    else:
         ketMenu = 'Bakso Yang Anda Mau tidak ada'
else:
     ketMenu = menu, 'Tidak Tersedia'

print('=== Output ===')
print('Menu = ',menu)
print('Pilih Menu = ',pilihMenu)
print('Harga = Rp. ',harga)
print('Keterangan Menu = ',ketMenu)





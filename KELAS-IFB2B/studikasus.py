# menu 
print('===== MENU MAKANAN =====')
print('1. Nasi goreng \n\t1.1 nasi goreng seafood \n\t1.2 nasi goreng mawut')
print('2. Bakso \n\t2.1 Bakso Popye \n\t2.2 Bakso Beranak ')

keterang = ''
ketMenu = ''
pilihMenu = ''
harga = 0
totalBayar = 0
kemabalian = 0

menu = input('Silahkan Pilih Menu = ')

if menu == 'NASI GORENG':
    print('====LIST NASI GORENG ====')
    print('1. nasi goreng seafood 2. nasi goreng mawut')

    pilihMenu = input('Pilih Nasi Goreng Apa = ')
    Jumlah = int(input('Mau Berapa Porsi = '))
    if pilihMenu == 'NASI GORENG SEAFOOD':
         harga = 30000
         totalBayar = Jumlah * harga
    elif pilihMenu == 'NASI GORENG MAWUT':
         harga = 25000
         totalBayar = Jumlah * harga
    else:
         ketMenu = 'Nasi Goreng Yang Anda Mau tidak ada'

elif menu == 'BAKSO':
    print('==== LIST BAKSO ====')
    print('1.Bakso Popye 2.Bakso Beranak ')

    pilihMenu = input('Pilih Bakso Apa = ')
    Jumlah = int(input('Mau Berapa Porsi = '))
    if pilihMenu == 'BAKSO POPY':
         harga = 20000
         totalBayar = Jumlah * harga
    elif pilihMenu == 'BAKSO BERANAK':
         harga = 25000
         totalBayar = Jumlah * harga
    else:
         ketMenu = 'Bakso Yang Anda Mau tidak ada'
else:
     ketMenu = menu, 'Tidak Tersedia'

print('Total Bayar = Rp. ',totalBayar)
uangTunai = int(input('Terima Uang Tunai = Rp. '))
kemabalian = uangTunai - totalBayar

print('=== Output ===')
print('Menu = ',menu)
print('Pilih Menu = ',pilihMenu)
print('Harga = Rp. ',harga)
print('Jumlah Porsi = ',Jumlah)
print('Total Bayar = Rp. ',totalBayar)
print('Terima Uang = Rp. ',uangTunai)
print('Kembalian = Rp. ',kemabalian)
print('Keterangan Menu = ',ketMenu)

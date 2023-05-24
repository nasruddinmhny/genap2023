
menu = input('Silahkan Pilih Menu = ')
jumPorsi = int(input('Jumlah porsi = '))

if menu == 'bakso':
    harga = 15000
elif menu == 'mie ayam':
    harga = 17000
else:
    harga = 0

TotalBayar = harga * jumPorsi
print('Total Bayar = Rp.',TotalBayar)
terimaUang = int(input('Terima Uang Sebesar = Rp. ',))
angsul = terimaUang - TotalBayar

print('==== STRUK ====')
print('Menu = ',menu)
print('Jumlah = ',jumPorsi)
print('Total Bayar = Rp.',TotalBayar)
print('Terima Uang = Rp. ',terimaUang)
print('Uang Kembalian = ',angsul)

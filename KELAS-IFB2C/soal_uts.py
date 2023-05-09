
jawab = 'y'

names = []
jumlah = []
harga = []
totalbayar = []
while True:
    nama = input('Nama Pelanggan : ')
    names.append(nama)

    jum = int(input('Jumlah = '))
    jumlah.append(jum)

    hrg = int(input('Harga = Rp. '))
    harga.append(hrg)


    jawab = input('Masi Input Lagi [y/t] = ')
    if jawab == 't':
        break

print('\n === Data Transaksi ===')
for i in range(len(names)):

    totbyr = harga[i] * jumlah[i]
    totalbayar.append(totbyr)
    print('\t No        = ',i)
    print('\t Nama      = ',nama[i])
    print('\t Jumlah    = ',jumlah[i])
    print('\t Harga     = Rp. ',harga[i])
    print('\t Total Bayar = Rp. ',totalbayar[i])
    print('----------------------------\n')



   


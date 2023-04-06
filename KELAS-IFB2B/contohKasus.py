'''
1. datang ke warung
2. lihat menu
3. memesan
4. duduk cari tempat
5. menunggu makanan datang
6. menikamti hidangan
7. transaksi
8. selesai

pertanyaan

mau makan apa -> makanan
mau berapa porsi -> JumlahProsiMkanan
minumnya apa -> minuman
mau pesan berapa -> jumlahPorsiMinuman
transaksi -> total bayar 

bakso 
3
15000 - Harga
es teh
3
7
total = ?

totalbayar = jumlahPorsiMakanan * hargaamakana + jumlahPorsiMinuman * hargaMinuman

output = 
makana = Bakso
Jumlah Prosi = 3
Harga = 15000
Minuman = es teh
Jumlah Prosi = 3
Harga = 7000
Total Bayar = Rp. 66000
'''

makanan = input('Mau makan apa = ')
JumMakanan = int(input('Mau berapa Porsi = '))
hargaMkanan = int(input('Harga makanan = Rp. '))
minuman = input('Mau Minum Apa = ')
jumMinuman = int(input('Mau pesan minum berapa = '))
hargaMinuman = int(input('Harga Minuman = Rp. '))

totalBayar = (JumMakanan * hargaMkanan) + (jumMinuman * hargaMinuman)

print('==== Struk Pembayaran ====')
print('Makanan = ',makanan)
print('Jumlah Porsi = ',JumMakanan)
print('Harga Makanan = Rp. ',hargaMkanan)
print('Minuman = ',minuman)
print('Jumlah Minuman = ',jumMinuman)
print('Harga Minuman = Rp. ',hargaMinuman)
print('Total Bayar = Rp. ',totalBayar)


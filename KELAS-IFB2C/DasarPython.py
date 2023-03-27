'''
#string
print('Saya sedang belajar')
print('Python')

#variable adalah tempat menyimpan nilai sementara
kalimat = 'Saya sedang belajar'
print(kalimat)

#menggabung variable dengan string 
namaMhs = input('Masukkan Nama = ')
nim = input('Masukkan Nim = ')
jurusan = input('Masukkan Jurusan = ')
print('Nama = ',namaMhs)
print('Nim = ',nim)
print('Jurusan = ',jurusan)
'''

makanan = input('Mau makan apa = ')
jumlahMakanan = int(input('Mau berapa porsi = '))
hargamakanan = int(input('Harga Makanan Rp. = '))
minuman = input('Mau minum apa = ')
jumlahMinuman = int(input('mau pesan berapa = '))
hargaminuman = int(input('Harga minuman Rp. = '))

totalharga = (jumlahMakanan * hargamakanan) + (jumlahMinuman * hargaminuman)

print(totalharga)

# append = menambahkan string ke dalam varibale list

jumlahNama = int(input('Input Jumlah = '))

namaMhs = []
for i in range(jumlahNama):
    nama = input('Silahkan Input nama = ')
    namaMhs.append(nama)

print('=== Nama Mahasiswa ====')
for n in namaMhs:
    print(n)

cariNama = input('Cari nama = ')

if cariNama in namaMhs:
    print('nama ',cariNama, ' ditemukan')
else:
    print('nama ',cariNama, 'tidak ada')

#soalnya menghapus nama pada variabel namaMhs

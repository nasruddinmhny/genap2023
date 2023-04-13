

# for variabel in range(nilai awal, nilai akhir, kelipatan):
# statement
# 1 2 3 4 5

# jika terdapat angka 1,2,3,4 maka angka ditemukan selain itu angka tidak ditemukan

# [1,2,3,4]

angka = ['1','2','3','4']
cari = input('Cari angka = ')
konvertTolist = list(cari)
jumlahItem = len(konvertTolist)

for i in range(jumlahItem):
    if cari[i] in angka:
        print('Angka ditemukan')
    else:
        print('angka tidak di temukan')
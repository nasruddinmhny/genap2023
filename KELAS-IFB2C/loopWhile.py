'''
jumlahData = int(input('Input Jumlah Data = '))
namahs = []

for i in range(jumlahData):
    nama = input('Input nama Mahasiswa = ')
    namahs.append(nama)

print('==== NAMA MAHASISWA ====')
for nama in namahs:
    print(nama)
    '''

JawabUlang = 'y'
namaMhs = []
namaMK = []
nilaiMk = []
ket = []

while(True):
    nama = input('Nama Mahasiswa = ')
    namaMhs.append(nama)

    namaMkuliah = input('Nama Matakuliah = ')
    namaMK.append(namaMkuliah)

    nilaiMkuliah = int(input('Nilai Matakuliah = '))
    nilaiMk.append(nilaiMkuliah)

    JawabUlang = input('Masi Mau input data lagi. input [y/t] = ')
    if JawabUlang == 't':
      break

print('==== NAMA MAHASISWA ====')
for i in range(len(namaMhs)):
    
    if nilaiMk[i] >= 80:
       keterangan = 'Anak Pintar'
    elif nilaiMk[i] >= 60:
       keterangan = 'terlalu main hp'
    elif nilaiMk[i] >= 50:
       keterangan = 'Kurang baca buku'
    else:
       keterangan = 'Jangan Main Hape terus'

    print('Nama = ',namaMhs[i])
    print('Matakuliah = ',namaMK[i])
    print('Nilai Matakuliah = ',nilaiMk[i])
    print('Keterangan = ',keterangan,'\n')

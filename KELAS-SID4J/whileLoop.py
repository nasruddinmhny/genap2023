
'''
jumlahData = int(input('Input Jumlah Data = '))
namaMhs = []
for i in range(jumlahData):
    nama = input('Input Nama = ')
    namaMhs.append(nama)

print('==== NAMA MAHASISWA ====')
for nama in namaMhs:
    print(nama)
'''

ulang = 'y'
namaMhs = []
namaMK = []
nilaiMk = []
while(True):
    nama = input('Input Nama = ')
    namaMhs.append(nama)

    namaMkuliah = input('Input Matakuliah = ')
    namaMK.append(namaMkuliah)

    nilaiMkuliah = int(input('Input Nilai Matakuliah = '))
    nilaiMk.append(nilaiMkuliah)

    ulang = input('Masi mau input data lagi. [y=lanjut / t=berhenti] = ')
    if ulang == 't':
        break

print('==== NAMA MAHASISWA ====')
for i in range(len(namaMhs)):

    if nilaiMk[i] >= 80:
        keterangan = 'Anak Pintar'
    elif nilaiMk[i] >= 60:
        keterangan = 'Anak Pandai'
    elif nilaiMk[i] >= 50:
        keterangan = 'Anak Perlu bimbingan'
    else:
        keterangan = 'Anak Butuh Di awasin'
    


    print('Nama = ',namaMhs[i])
    print('Nama Matakuliah = ',namaMK[i])
    print('Nilai Matakuliah = ',nilaiMk[i])
    print('Keterangan = ',keterangan,'\n')

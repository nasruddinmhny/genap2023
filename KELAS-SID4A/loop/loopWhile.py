'''
namaMhs = []
jumlahData = int(input('Input Jumlah Data = '))
for i in range(jumlahData):
    nama = input('Nama = ')
    namaMhs.append(nama)

for n in namaMhs:
    print(namaMhs)
'''
ulang = 'ya'
namaMhs = []
namaMk = []
nilaiMk = []
keterangan = []
while(True):
    nama = input('Silahkan Input Nama Temannya = ')
    namaMhs.append(nama)
    namaMatakuliah = input('Input Matakuliah = ')
    namaMk.append(namaMatakuliah)
    nilaiMatakuliah = int(input('Input Nilai Matakuliah = '))
    nilaiMk.append(nilaiMatakuliah)

    ulang = input('Apakah Mau input Data lagi.. input [y/t] = ')
    if ulang == 't':
        break

print('[===== LIST nama Teman saya =====')
for i in range(len(namaMhs)):
    if nilaiMk[i] >= 50:
        keterangan = 'Tuntas'
    else:
        keterangan = 'Tidak Tuntas'

    print('Nama = ',namaMhs[i])
    print('Nama Matakukiah = ',namaMk[i])
    print('Nilai Matakuliah = ',nilaiMk[i])
    print('Keterangan = Matakuliah ',keterangan,'\n')







#fungsi yang tidak menggunakan paramter dan tidak mengembalikan nilai
def cetak():
    print('hello world..')

#fungsi dengan parameter
def cetakNama(nama,nim):
    print('Nama Mahasiswa = ',nama)
    print('Nim = ',nim)

#cetakNama('nasruddin','210452')

def Tambah(nilaiA,nilaiB):
    hasil = nilaiA + nilaiB
    return hasil

def InputNilai():
    
    nA = int(input('Input Nilai A = '))
    nB = int(input('Input Nilai B = '))

    hasil = Tambah(nA,nB)
    print('Haisl tambah ',nA,' + ',nB,' = ',hasil)


InputNilai()
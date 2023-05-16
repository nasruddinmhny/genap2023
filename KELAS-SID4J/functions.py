
#menggunakan parameter dan ada juga yang tidak menggunakan parameter
#menggunakan parameter dan bisa mengembalikan nilai dengan kata return
#menggunakan parameter tetapi tidak bisa mengembalikan niali
#tidak menggunakan parameter dan tidak bisa mengembalikan nilai

#fungsi yang tidak memiliki paramter dan tidak bisa mengembalikan nilai
def Panggil():
    print('Semua mahasiswa kelas SID4J maju ke depan..')

def PanggilKelas(kelas):
    print('Semua mahasiswa kelas',kelas, ' maju ke depan..')



def Tambah(nA,nB,nC):
    hasil = nA + nB + nC
    return hasil

def Pengurangan(nA,nB,nC):
    hasil = nA - nB - nC
  
    return hasil

def inputData():
    nilaiA = int(input('Input Nilai A = '))
    nilaiB = int(input('Input Nilai B = '))
    nilaiC = int(input('Input Nilai C = '))
    hasil = Tambah(nilaiA,nilaiB,nilaiC)
    hasilPengurangan = Pengurangan(nilaiA,nilaiB,nilaiC)
    print('Hasil Tambah = ',hasil)
    print('Hasil Kurang = ',hasilPengurangan)

inputData()
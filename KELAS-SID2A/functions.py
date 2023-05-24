
# function yg bisa mengembalikan nilai dgn kata return dan menggunakan parameter
def Tambah(nilai1,nilai2):
    hasil = nilai1 + nilai2
    return hasil

def Kurang(nilai1,nilai2):
    hasil = nilai1 - nilai2
    return hasil
    
def Cetak(judul):
    print(f'=== Operasi {judul} ===')



def InputData():
    #bil1 = 6
    bil1 = int(input('Input Bilangan 1 = '))
    bil2 = int(input('Input Bilangan 2 = '))

    hasil = Tambah(bil1,bil2)
    hasilKurang = Kurang(bil1,bil2)

    keterangan = input('Keterangan = ')

    Cetak(keterangan)
    print('Hasil = ',hasil)
    print('Hasil Kurang = ',hasilKurang)

InputData()
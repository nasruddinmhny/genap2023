
#function parameter 

def Tambah(bil1,bil2):
    hasil = bil1 + bil2
    return hasil

def cetak():
    print('==== INFORMASI ====')

def Keterangan(judul):
    print(f'Kegiatan Hari ini adalah {judul}')

nilai1 = 4
nilai2 = 5

hasil = Tambah(nilai1,nilai2)
hasilTambh = Tambah(10,3)

Keterangan('Penjumlahan')
cetak()
print('HASIL = ',hasil)
print('Hasil Tambah = ',hasilTambh)
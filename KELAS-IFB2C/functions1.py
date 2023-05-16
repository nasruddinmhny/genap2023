
'''
nilaiA = 3
nilaiB = 5
Na = 5
Nb = 4

hasilTambah = nilaiA + nilaiB
hasilPerkalian = nilaiA * nilaiB
hasilPembagian = nilaiA // nilaiB
hasilPengurangan = nilaiA - nilaiB
hasilTambahNilai = Na + Nb

print('Hasil Tambah = ',hasilTambah)
print('Hasil Perkalian = ',hasilPerkalian)
print('Hasil Pembagian = ',hasilPembagian)
print('Hasil Pengurangan = ',hasilPengurangan)

'''

def Tambah(nA,nB):
    hasil = nA + nB
    return hasil

def Perkalian(nA,nB):
    hasil = nA * nB
    return hasil


nilaiA = int(input('Input Nilai A = '))
nilaiB = int(input('Input Nilai B = '))

hasilTambah = Tambah(nilaiA,nilaiB)
hasilPerkalian = Perkalian(nilaiA,nilaiB)

print('Hasil = ',hasilTambah)
print('Hasil = ',hasilPerkalian)



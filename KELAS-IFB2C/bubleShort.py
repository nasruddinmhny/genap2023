
def BubleShort(angka):
    for i in range(0,len(angka)-1):
        for a in range(0,len(angka)-1):
            if nilaiAngka[a] > nilaiAngka[a+1]:
                kosong = nilaiAngka[a]
                nilaiAngka[a] = nilaiAngka[a+1]
                nilaiAngka[a+1] = kosong
        
    return angka

JumlahData = int(input('Jumlah Data = '))
nilaiAngka = []


for i in range(JumlahData):
    angka = int(input('Input Bilangan = '))
    nilaiAngka.append(angka)

print('Value Nilai Angka sebelum Di urutkan = ',nilaiAngka)
nilaiSetelahDiurutkan = BubleShort(nilaiAngka)
print('Value Nilai Angka Setelah Di urutkan = ',nilaiSetelahDiurutkan)





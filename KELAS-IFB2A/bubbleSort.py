
def bubbleSort(nilai):

    for i in range(0,len(nilai)-1):
        for a in range(0,len(nilai)-1):
            if bilangan[a] > bilangan[a + 1]:
                tempatBru = bilangan[a]
                bilangan[a] = bilangan[a + 1]
                bilangan[a + 1] = tempatBru
    return nilai

jumlahData = int(input('Banyaknya Data = '))
bilangan = []

for i in range(jumlahData):
    bil = int(input('Input Bilangan = '))
    bilangan.append(bil)

print('==== Sebelum ====')
print('Nilai Variabel Bilangan = ',bilangan)

bilUrut = bubbleSort(bilangan)
print('==== Setelah ====')

print('Nilai Variabel Bilangan = ',bilUrut)




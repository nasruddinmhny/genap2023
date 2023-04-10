
# huruf vokal = aeiou AEIOU
# saya sedang makan
# fungsi dari append

kalimat = input('Input Kalimat = ')
konvertKalimatTOList = list(kalimat)
jumlahKarakter = len(konvertKalimatTOList)

hurufVokal = ['A','E','I','O','U','a','e','i','o','u']
hasilHurufVokal = []
hasilNonVokal = []
jumlahHurufVokal = 0
jumlahHurufNonVokal = 0

for v in range(0,jumlahKarakter):
    if konvertKalimatTOList[v] in hurufVokal:
        hasilHurufVokal.append(konvertKalimatTOList[v])
        jumlahHurufVokal += 1
    else:
        #konvertKalimatTOList[v] not in hurufVokal
        hasilNonVokal.append(konvertKalimatTOList[v])
        jumlahHurufNonVokal += 1


print('==== output ====')
print('Kalimat = ',kalimat)
print('Kalimat Konver to list = ',konvertKalimatTOList)
print('Jumlah Karakter = ',jumlahKarakter)
print('Huruf Vokal = ',hasilHurufVokal)
print('Jumlah Huruf Vokal = ',jumlahHurufVokal)
print('Huruf Non Vokal = ', hasilNonVokal)
print('Jumlah Huruf Non Vokal = ',jumlahHurufNonVokal)
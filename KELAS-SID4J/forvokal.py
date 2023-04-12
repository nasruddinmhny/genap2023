
# menampilkan huruf vokal yang di input
# huruf vokal = a e i o u
# belajar

hurufVokal = ['a','e','i','o','u','A','E','i','O','U']
hasilHurufVokal = []
hasilHurufNonVokal = []
JumlahHurufVokal = 0
jumlahHurufNonVokal = 0
kalimat = input('input Kalimat = ')
konvertKalimatToList = list(kalimat)
jumlahKarakterKalimat = len(konvertKalimatToList)

for i in range(jumlahKarakterKalimat):
    
    if konvertKalimatToList[i] in hurufVokal:
        hasilHurufVokal.append(konvertKalimatToList[i])
        JumlahHurufVokal += 1
    else:
        hasilHurufNonVokal.append(konvertKalimatToList[i])
        jumlahHurufNonVokal += 1



print('======= output =======')
print('Kalimat = ',kalimat)
print('Konver Kalimat to List = ',konvertKalimatToList)
print('Jumlah Karakter = ',jumlahKarakterKalimat)
print('Huruf Vokal = ',hasilHurufVokal)
print('Jumlah Huruf Vokal = ',JumlahHurufVokal)
print('huruf Non Vokal = ',hasilHurufNonVokal)
print('Jumlah Huruf Non Vokal = ',jumlahHurufNonVokal)
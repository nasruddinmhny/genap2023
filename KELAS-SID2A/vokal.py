
hurufVokal = ['a','e','i','o','u','A','E','I','O','U']

kalimat = input('Masukkan Kalimat = ')
konvertKalimatToList = list(kalimat)
jumlahKarakter = len(konvertKalimatToList)

hasilHurufVokal = []
hasilHurufBukanVokal = []
JumlahKarakterVokal = 0
JumlahKarakterBukanVokal = 0

for i in range(jumlahKarakter):

    if konvertKalimatToList[i] in hurufVokal:
        hasilHurufVokal.append(konvertKalimatToList[i])
        JumlahKarakterVokal += 1
    else:
        hasilHurufBukanVokal.append(konvertKalimatToList[i])
        JumlahKarakterBukanVokal += 1


print('===== OUTPUT =====')
print('Kalimat = ', kalimat)
print('Hasil Konvert Ke List = ',konvertKalimatToList)
print('Jumlah Karakter = ',jumlahKarakter)
print('Huruf Vokal = ',hasilHurufVokal)
print('Jumlah Huruf Vokal = ',JumlahKarakterVokal)
print('Huruf bukan Vokal = ',hasilHurufBukanVokal)
print('Jumlah Karakter Bukan Vokal = ',JumlahKarakterBukanVokal)
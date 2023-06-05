
# a e i o u A E I O U

hurufVokal = ['a','e','i','o','u','A','E','I','O','U']
kalimat = input('Kalimat = ')
konvertKalimatKeList = list(kalimat)
jumlahKarakter = len(konvertKalimatKeList)
tempatHurufVokal = []
tempatBukanHurufVokal = []

for i in range(jumlahKarakter):
    if konvertKalimatKeList[i] in hurufVokal:
        tempatHurufVokal.append(konvertKalimatKeList[i])
    else:
        tempatBukanHurufVokal.append(konvertKalimatKeList[i])


print('===== OUTPUT =====')
print('Kalimat = ',kalimat)
print('Konvert Kalimat Ke list  = ',konvertKalimatKeList)
print('Jumlah Karakter = ',jumlahKarakter,' - karakter')
print('huruf Vokal = ',tempatHurufVokal)
print('JUmlah Huruf Vokal = ',len(tempatHurufVokal))
print('Bukan Huruf Vokal = ',tempatBukanHurufVokal)
print('Jumlah Bukan Huruf Vokal = ',len(tempatBukanHurufVokal))




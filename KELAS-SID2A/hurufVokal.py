
# a e i o u A E I O U

# jika huruf vokal maka ini huruf vokal selain itu ini bukan huruf vokal
#saya sedang belajar

hurufVokal = ['a','e','i','o','u','A','E','I','O','U']
tampungHuruf = input('Masukkan Huruf (a - z / A - Z) = ')
konverTampungHurufToList = list(tampungHuruf)
JumlahKarakter = len(konverTampungHurufToList)

for i in range(JumlahKarakter):
    if konverTampungHurufToList[i] in hurufVokal:
        kalimat = 'Ini Huruf Vokal'
    else:
        kalimat = 'Ini Bukan Huruf Vokal'

print('====== output ======')
print('Huruf = ',tampungHuruf)
print('Konvert Tampung Huruf = ',konverTampungHurufToList)
print('Jumlah Karakter = ',JumlahKarakter)
print('Keterangan = ',kalimat)

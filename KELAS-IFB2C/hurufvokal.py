
# a e i o u A E I O U
hurufVokal = ['a','e','i','o','u','A','E','I','O','U'] # variable hurufVokal menampung huruf vokal
kalimat = input('Kalimat = ') # menerima inputan dari keyboard/user
konvertToList = list(kalimat) # variabel kalimat di konvert ke list
JumlahKarakterKalimat = len(kalimat) #len digunakan untuk menghitung jumlah karakter pada variabel kalimat
HasilHurufVokal = [] # inisial variabel bertipe list alias variabel kosong
HasilHurufNonVokal = [] #inisial variabel bertipe list alias variabel kosong
JumlahHurufVokal = 0 #inisial variabel kosong untuk penjumlahan
jumlahHurufNonVokal = 0 #inisial variabel kosong untuk penjumlahan

for i in range(JumlahKarakterKalimat):
    
    if konvertToList[i] in hurufVokal:
        HasilHurufVokal.append(konvertToList[i])
        JumlahHurufVokal += 1 # jumlahhurufvokal = jumlahhurufvokal + 1
    else:
        HasilHurufNonVokal.append(konvertToList[i])
        jumlahHurufNonVokal += 1

print('===== OUTPUT =====')
print('Kalimat = ',kalimat)
print('Konvert Kalimat To List = ',konvertToList)
print('Huruf Vokal = ',HasilHurufVokal)
print('Jumlah Huruf Vokal = ',JumlahHurufVokal)
print('Huruf Non Vokal = ',HasilHurufNonVokal)
print('Jumlah Huruf Non Vokal = ',jumlahHurufNonVokal)


#latihan menampilkan bilnagan genap dan ganjil

# jika bilangan di bagi 2 sisa hasil baginya 0 selain itu bilangan ganjil

#NamaBuah = ['Alpukat','durian','salak'] #alpukat[0] durian[1] salak[2]
kalimat = input('Kalimat = ')
kon = list(kalimat)
jumlahKarakter = len(kon)
print(kon)
print('Jumlah Karakter = ',jumlahKarakter)

for i in range(jumlahKarakter):
    print('kode asci = ',kon[i],'= ',ord(kon[i]))
    
'''
print(kon)
konvert = kalimat.split()
konvertToList = list(konvert)
print(konvert)
print(konvertToList)

#len
for i in range(0,len(NamaBuah)):
    print(NamaBuah[i])


konvertSplit = NamaBuah.split(',')
print(konvertSplit)
'''

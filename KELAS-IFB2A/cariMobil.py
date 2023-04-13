
mobil = ['Nissan','Toyota','Mazda','Subaru','N']
cari = input('Cari Mobil = ')
#konvertList = list(cari)
konvertList = cari.split()
jumlahItem = len(konvertList)
print('Ninlai Variable KonvertTolist = ',konvertList)

for i in range(jumlahItem):
    if konvertList[i] in mobil:
        print('Mobil Tersedia')
    else:
        print('Mobil Tidak Tersedia')
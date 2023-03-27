kalimat = input('Input Kalimat = ')
print(kalimat)

#casting ke list
KonvertToList = list(kalimat)
print('Hasil Konvert Ke List = ',KonvertToList)


#jumlah karakter pada variable konvertToList dengan len()
jumlahKarakter = len(KonvertToList)
print('Jumlah Karakter = ',jumlahKarakter)

# fungsi split memisahkan antara kata
konverToSplit = kalimat.split()
print('hasil konvert ke split = ',konverToSplit)

#join
print(' '.join(konverToSplit))
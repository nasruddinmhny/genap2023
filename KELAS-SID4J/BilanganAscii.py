nama = input('Input nama anda = ')
print('nama = ',nama)

konvertToList = list(nama)
print('Konver To List = ',konvertToList)

hasilTambah = 0
for i in range(0,len(konvertToList)):
    konvertTochar = ord(konvertToList[i])
    hasilTambah += konvertTochar 
    print(konvertToList[i],' = ',ord(konvertToList[i]))
    print(konvertTochar,' = ',chr(konvertTochar))
    print('Haisl = ',hasilTambah)


# A + A = 130


#mengurutkan data dari kecil ke besar..tetapi menggunakan huruf

#inputan = D R E F G a b c

# outputnya
# a b c D E F G R

# ord konvert dari huruf ke angka
# chr konvert dari angka ke huruf



for i in range(1,126):
    print(f'Bilangan AsCII {i} = ',chr(i))


huruf1 = 'F'
huruf2 = '@'

konvertHuruf1 = ord(huruf1)
konvertHuruf2 = ord(huruf2)

if konvertHuruf1 > konvertHuruf2:
    print(konvertHuruf1,' > ',konvertHuruf2)
else:
    print(konvertHuruf1,' < ',konvertHuruf2)



jumlahLiter = int(input('Jumlah Liter = '))

harga = 0
totalharga = 0
if jumlahLiter >= 5 :
    harga = 2000
    totalharga = jumlahLiter * harga
elif jumlahLiter >= 10 :
    harga = 1500
    totalharga = jumlahLiter * harga
else:
    harga = 0
    totalharga = 0

print('Harga = Rp. ',harga)
print('total Harga = Rp. ',totalharga)


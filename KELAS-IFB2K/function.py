
#proses
def Hitung(a1,a2):
    hasil = a1 + a2
    return hasil

def GenapGanjil(hsl):
    ket = ''

    if hsl % 2 == 0:
        ket = 'Bilangan Genap'
    else:
        ket = 'Bilangan Ganjil'
    return ket

#output
def cetak(ang1,ang2,hsl,gg):
    print(f'Hasil {ang1} + {ang2} = {hsl} adalah {gg}')

#input
def inputdata():

    angka1= int(input('Input Nilai 1 = '))
    angka2 = int(input('Input Nilai 2 = '))

    hasil = Hitung(angka1,angka2)
    bilGega = GenapGanjil(hasil)
    cetak(angka1,angka2,hasil,bilGega)

#program utama dipanggil ketika di execute
inputdata()

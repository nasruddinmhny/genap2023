
def Hitung(nilai1,nilai2,nilai3):
    hasil = nilai1 + nilai2 + nilai3
    return hasil

def cetak(nil1,nil2,nil3,hsl,gg):
    print(f'hasil {nil1} + {nil2} + {nil3} = {hsl} adalah bilangan {gg}')

def bilangan(nilaiHasil):
    ket = ''

    if nilaiHasil % 2 == 0:
        ket = 'Genap'
    else:
        ket = 'Ganjil'

    return ket

def inputan():

    n1 = 4
    n2 = 2
    n3 = 4

    hasil = Hitung(n1,n2,n3)
    jenisBilangan = bilangan(hasil)
    cetak(n1,n2,n3,hasil,jenisBilangan)

inputan()



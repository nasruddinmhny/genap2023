
def HitungTOtalBelanja(hrg,jum):
    totalBelanja = hrg * jum
    return totalBelanja

def cetak(menumkn,hrgmkn,jummkm,totbel,dis,totbyar):
    print(f'Menu makanan {menumkn} harga Rp. {hrgmkn} pesan {jummkm} total belanja = Rp. {totbel}')
    print(f'Diskon {dis}')
    print(f'Total Bayar = Rp. {totbyar}')


def diskon(totBelanja):

    discount = 0

    if totBelanja > 50000:
        discount = 0.02
    else:
        discount = 0

    return discount

def HitungTotalBayar(diskount,totBela):
    totbyr = totBela - (diskount * totBela) #(),*,/,+,-
    return totbyr


def inputan():
    menu = input('Input Mneu = ')
    harga = float(input('Input Harga Makanan = '))
    jumlah = int(input('Input Jumlah Pesanan = '))

    totalBelanja = HitungTOtalBelanja(harga,jumlah)
    Diskon = diskon(totalBelanja)
    totalBayar = HitungTotalBayar(Diskon,totalBelanja)
    cetak(menu,harga,jumlah,totalBelanja,Diskon,totalBayar)

inputan()




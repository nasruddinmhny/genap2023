
#total bayar dari pembelian tiket
#Data seperti berikut 
#1. nik
#2. nama
#3. tujuan 
    #a. samarinda = Rp. 45000
    #b. bontang = Rp. 65000
    #c. longkali = Rp. 45000

#. hitung total harga tiket yang harus dibayar + pajak = 10% (0.1)
# harga total tiket itu di tentukan dengan harga tujuan dan jumlah tiket ya ng dibeli

#rumus total harga = harga tiket * jumlah tiket

#dalam function
def HitungTotalHargaTiket(hrgTiket,jumTiket):
    totalHarga =  hrgTiket * jumTiket
    return totalHarga

def HitungTotalPajak(totalHrgTiket,pajak = 0.1):
    totalPajak = totalHrgTiket * pajak
    return totalPajak

def TotalBayar(totalHrgTiket,totpajak):
    totBayar = totalHrgTiket + totpajak
    return totBayar

def Cetak(nk,nm,tj,hrg,jum,tothrgtiket,totpjk,totbyr):
    print('===== STRUK =====')
    print('Nik = ',nk)
    print('Nama = ',nm)
    print('Tujaun = ',tj)
    print('Harga Tiket = Rp. ',hrg)
    print('Jumlah Tiket = ',jum,' - Tiket')
    print('Total Harga Tiket = Rp. ',tothrgtiket)
    print('Total Pajak = Rp. ',totpjk)
    print('Total Bayar = Rp. ',totbyr)


def inputData():
    nik = input('Nik = ')
    nama = input('Nama = ')
    tujuan = input('Tujuan = ')
    jumlah = int(input('Jumlah = '))

    if tujuan == 'samarinda':
        hargaTiket = 45000
    elif tujuan == 'bontang':
        hargaTiket = 60000
    elif tujuan == 'longkali':
        hargaTiket = 45000
    else:
        print('Tujuan Tidak Tesedia..')

    totalHargaTIket = HitungTotalHargaTiket(hargaTiket,jumlah)
    totalPajak = HitungTotalPajak(totalHargaTIket)
    totalBayar = TotalBayar(totalHargaTIket,totalPajak)

    Cetak(nik,nama,tujuan,jumlah,hargaTiket,totalHargaTIket,totalPajak,totalBayar)

inputData()
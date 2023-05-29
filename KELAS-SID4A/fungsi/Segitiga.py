def LuasSegiTiga(nilaiAlas,nilaiTinggi):
    luas = ( nilaiAlas * nilaiTinggi ) / 2
    return luas

def Cetak(nilaiAlas,nilaiTinggi,hasil):
    print('Alas = ',nilaiAlas)
    print('Tinggi = ',nilaiTinggi)
    print('Hasil = ',hasil)


def inputData():

    alas = 10
    tinggi = 15

    hasil = LuasSegiTiga(alas,tinggi)

    Cetak(alas,tinggi,hasil)

inputData()
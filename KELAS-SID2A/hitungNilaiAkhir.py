
def HitungNilaiAkhir(nuts,nuas):
    na = (nuts + nuas) // 2
    return na

def cetak(nimMhs,namaMhs,mk,nuts,nuas,nakhir,nhuruf):
    print('==== Informasi ====')
    print('Nim = ',nimMhs)
    print('Nama = ',namaMhs)
    print('Matakuliah = ',mk)
    print('Nilai UTS = ',nuts)
    print('Nilai UAS = ',nuas)
    print('Nilai AKhir = ',nakhir)
    print('Nilai Huruf = ',nhuruf)

def nilaiHuruf(nakir):
    nh = ''

    if nakir >= 80 and nakir <= 100:
        nh = 'A'
    elif nakir >= 70 and nakir <= 79:
        nh = 'B'
    elif nakir >= 60 and nakir <= 69:
        nh = 'C'
    elif nakir >= 50 and nakir <= 59:
        nh = 'D'
    else:
        nh = 'E'

    return nh

def inputData():

    nim = input('Nim = ')
    nama = input('Nama = ')
    matakuliah = input('Matakuliah = ')
    nilaiUts = float(input('Nilai UTS = '))
    nilaiUas = float(input('Nilai UAS = '))

    nilaiAkhir = HitungNilaiAkhir(nilaiUts,nilaiUas)
    nhuruf = nilaiHuruf(nilaiAkhir)

    cetak(nim,nama,matakuliah,nilaiUts,nilaiUas,nilaiAkhir,nhuruf)

inputData()
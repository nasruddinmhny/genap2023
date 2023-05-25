def hitungNIlaiAkhir(nuts,nuas):
    hasil = (nuts + nuas) // 2
    return hasil

def TentukanNilaiHuruf(nakhir):
    nh = ''

    if nakhir >= 80 and nakhir <= 100:
        nh = 'A'
    elif nakhir >= 70 and nakhir <= 79:
        nh = 'B'
    elif nakhir >= 60 and nakhir <= 69:
        nh = 'C'
    elif nakhir >= 50 and nakhir <= 59:
        nh = 'D'
    else:
        nh = 'E'
    
    return nh

def cetak():
    print('==== INFORMASI ====')

def Output(nimMhs,namaMhs,mk,nuts,nuas,na,nhuruf):
    print('Nim = ',nimMhs)
    print('Nama = ',namaMhs)
    print('Matakuliah = ',mk)
    print('Nilai UTS = ',nuts)
    print('Nilai UAS = ',nuas)
    print('Nilai Akhir = ',na)
    print('Nilai Huruf = ',nhuruf)

def inputData():
    nim = input('Nim = ')
    nama = input('Nama = ')
    matakuliah = input('Matakuliah = ')
    nilaiUts = float(input('Nilai UTS = '))
    nilaiUas = float(input('Nilai UAS = '))

    nilaiAkhir = hitungNIlaiAkhir(nilaiUts,nilaiUas)
    nilaiHuruf = TentukanNilaiHuruf(nilaiAkhir) 
    cetak()
    Output(nim,nama,matakuliah,nilaiUts,nilaiUas,nilaiAkhir,nilaiHuruf)

inputData()



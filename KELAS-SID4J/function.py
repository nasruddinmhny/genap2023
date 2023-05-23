
#nilai uas, nilai tugas, nilai UTS
def HitungNilaiAkhir(nt,nuts,nuas):
    na =  (nt + nuts + nuas) // 3
    return na

def NilaiHuruf(nakhir):
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

def input_data():

    nim = input('Nim = ')
    nama = input('Nama = ')
    matakuliah = input('Matakuliah = ')
    nilaiTugas = float(input('Nilai Tugas = '))
    nilaiUts = float(input('Nilai UTS = '))
    nilaiUas = float(input('Nilai UAS = '))

    nilaiAkhir = HitungNilaiAkhir(nilaiTugas,nilaiUts,nilaiUas)
    nilaiHuruf = NilaiHuruf(nilaiAkhir)

    print('==== Informasi ====')
    print(f'Nim = {nim}')
    print('Nama = ',nama)
    print('Matakuliah = ',matakuliah)
    print('Nilai Tugas = ',nilaiTugas)
    print('Nilai UTS = ',nilaiUts)
    print('Nilai UAS = ',nilaiUas)
    print('NIlai Akhir = ',nilaiAkhir)
    print('NIlai Huruf = ',nilaiHuruf)

input_data()
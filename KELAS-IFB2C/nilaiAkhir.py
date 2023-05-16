

def HitungNilaiAkhir(nilaiUts,nilaiUas):
    hasil = (nilaiUts + nilaiUas)//2
    return hasil

def NilaiHuruf(na):
    nhuruf = ''
    if na >= 80 and na <= 100:
        nhuruf = 'A'
    elif na >= 70 and na <= 79:
        nhuruf = 'B'
    elif na >= 60 and na <= 69:
        nhuruf = 'C'
    elif na >= 50 and na <= 59:
        nhuruf = 'D'
    else:
        nhuruf = 'E'
    
    return nhuruf

def kategori(na):

    keterangan = ''

    if na >= 90 and na <= 100:
        keterangan = 'Good job'
    elif na >= 70 and na <= 89:
        keterangan = 'memuaskan'
    else:
        keterangan = 'Jangan Down'
    
    return keterangan


def inputData():
    nUts = float(input('Nilai UTS = '))
    nUas = float(input('Nilai UAS = '))

    nilaiAkhir = HitungNilaiAkhir(nUts,nUas)
    nilaiHuruf = NilaiHuruf(nilaiAkhir)
    keterangan = kategori(nilaiAkhir)

    print('Nilai Akhir = ',nilaiAkhir)
    print(' Nilai huruf = ',nilaiHuruf)
    print('Keterangan = ',keterangan)


inputData()


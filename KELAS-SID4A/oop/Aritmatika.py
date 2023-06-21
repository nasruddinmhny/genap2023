
#rumus luas segitiga 1/2 * alas * tinggi
'''
def HitungLuas(als,tggi):
    hasil = (als * tggi) / 2
    return hasil
alas = 2
tinggi = 4

hasil = HitungLuas(alas,tinggi)

print(hasil)
'''

class SegiTiga:

    def __init__(self,inputAlas,inputTinggi):
        self.alas = inputAlas
        self.tinggi = inputTinggi

    def HitungLuas(self):
        return (self.alas * self.tinggi) / 2
    
    def Cetak(self):
        print(f'Nilai Alas {self.alas} dan Nilai Tinggi {self.tinggi}')
        print(f'Luas Segitiga = {sg1.HitungLuas()}')

NilaiAlas = float(input('Input Nilai Alas = '))
NilaiTinggi = float(input('Input Nilai Tinggi = '))

sg1 = SegiTiga(NilaiAlas,NilaiTinggi)
sg1.Cetak()


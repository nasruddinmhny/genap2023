
#mencari luas segitiga
#rumus luas = 1/2 * alas * tinggi
# tingkatan dalam matematika (), * , / , + , -
print('==== Cara 1 ====')
alas = 20
tinggi = 30

luas = (alas * tinggi) / 2

print(f'luas Segitiga  = {luas}')

print('===== Cara 2 ====')
def hitungLuasSg(al,ti):
     hasil = (al * ti)/2
     return hasil

hasil = hitungLuasSg(alas,tinggi)
print('Hasil  = ',hasil)

print('=== cara 3 ====')
class Segitiga:
     
    def __init__(self,inputAlas,inputTinggi):
          self.alas = inputAlas
          self.tinggi = inputTinggi

    def HitungLuas(self):
         return (self.alas * self.tinggi) / 2
    
    def cetak(self):
         print(f'Luas Segitiga = {self.HitungLuas()}')

sg = Segitiga(alas,tinggi)
sg.cetak()

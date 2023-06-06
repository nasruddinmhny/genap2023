
# attribut dari dosen = nidn,nama,jk,alamat
# attribut dari mahasiswa = nim,nama,jk,alamat

class Dosen:
    #varibel class
    #alamat = ''
    #variabel instance
    def __init__(self,InputNidn,InputNama,InputJk,InputAlamat):
        self.nidn = InputNidn
        self.nama = InputNama
        self.jk = InputJk
        self.alamat = InputAlamat

    #methode tanpa parameter
    def cetak(self):
        print(f'Nama saya adalah {self.nama}',
            f'jenis kelamin {self.jk}',f'dan Nidn {self.nidn}')
        print('Alamat = ',self.GetAlamat())
        

    #methode dengan parameter
    def SetAlamat(self,almt):
        self.alamat = almt
    
    # methon dengan return
    def GetAlamat(self):
        return self.alamat
        

nim = input('Nim = ')
nama = input('Nama = ')
jk = input('jenis Kelamin = ')
almt = input('Alamat = ')

dosen1 = Dosen(nim,nama,jk,almt)
dosen1.cetak()


#print('NIDN = ',dosen2.nidn)
#print(f'NAMA = {dosen2.nama}')
#print(f'Jenis Kelamin = {dosen2.jk}')

        
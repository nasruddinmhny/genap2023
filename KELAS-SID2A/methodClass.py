

class Mahasiswa:
    #variabel class
    jenjang = ''
    #attribut informasi yg bisa didapatkan dari class
    #namaMahasiswa,nim,jurusan
    #variabel instance
    def __init__(self,nmMhs,nimMhs,jurMhs,jenjangPdk,mk):
        self.namaMahasiswa = nmMhs
        self.nimMahasiswa = nimMhs
        self.jurusan = jurMhs
        Mahasiswa.jenjang = jenjangPdk
        self.makuliah = mk

    def cetak(self):
        print(f'Nama Mahasisaw = {self.namaMahasiswa}')
        print(f'Nim Mahasiswa = {self.nimMahasiswa}, jurusan = {self.jurusan},Jenjang = {Mahasiswa.jenjang}')
        print(f'Matakuliah = {self.matakuliah()}')

    def matakuliah(self):
        return self.makuliah


print('===== Mahasiswa ke 1 ======')
Ridwan = Mahasiswa('Ridwan','2214020','SIstem Informasi-D3','Sarjana Terapan','OOP')
Ridwan.cetak()




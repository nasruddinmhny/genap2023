
class Mahasiswa:
    # varibale class
    semester = 0
    #instance variable
    def __init__(self,InputNim,InputNama,InputJurusan):
        self.nim = InputNim
        self.nama = InputNama
        self.jurusan = InputJurusan
        Mahasiswa.semester = 4

mhs1 = Mahasiswa('2114001','Rani','Sistem INformasi - D3')
print('Nim = ',mhs1.nim)
print(f'Nama = {mhs1.nama}')
print('Jurusan = ',mhs1.jurusan)
print('Semester = ',Mahasiswa.semester)

mhs2 = Mahasiswa('2114002','Rana','Sistem Informasi-D3')
print('NIm = ',mhs2.nim, ',nama = ',mhs2.nama,', Jurusan = ',mhs2.jurusan)


    
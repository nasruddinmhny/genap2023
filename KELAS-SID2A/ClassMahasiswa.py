
class Mahasiswa:
    #variabel class
    jenjang = ''
    #attribut informasi yg bisa didapatkan dari class
    #namaMahasiswa,nim,jurusan
    #variabel instance
    def __init__(self,nmMhs,nimMhs,jurMhs,jenjangPdk):
        self.namaMahasiswa = nmMhs
        self.nimMahasiswa = nimMhs
        self.jurusan = jurMhs
        Mahasiswa.jenjang = jenjangPdk

print('===== Mahasiswa ke 1 ======')
Ridwan = Mahasiswa('Ridwan','2214020','SIstem Informasi-D3','Sarjana Terapan')

print(f'Nama Mahasisaw = {Ridwan.namaMahasiswa}')
print(f'Nim Mahasiswa = {Ridwan.nimMahasiswa}, jurusan = {Ridwan.jurusan},Jenjang = {Mahasiswa.jenjang}')

print('===== Mahasiswa ke 2 ======')
Adi = Mahasiswa('Adi','2214015','Hukum','Sarjana')
print(f'Nama Mahasisaw = {Adi.namaMahasiswa}')
print(f'Nim Mahasiswa = {Adi.nimMahasiswa}, jurusan = {Adi.jurusan}, Jenjang = {Mahasiswa.jenjang}')

Awal = Mahasiswa('Awaluddin','2214016','PGPAUD','Sarjana')
print(f'Nama Mahasisaw = {Awal.namaMahasiswa}')
print(f'Nim Mahasiswa = {Awal.nimMahasiswa}, jurusan = {Awal.jurusan}, Jenjang = {Mahasiswa.jenjang}')

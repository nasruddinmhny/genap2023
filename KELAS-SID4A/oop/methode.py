

class Mahasiswa:
    # varibale class
    #semester = 0
    #instance variable
    def __init__(self,InputNim,InputNama,InputJurusan,InputSemester):
        self.nim = InputNim
        self.nama = InputNama
        self.jurusan = InputJurusan
        self.sem = InputSemester 
       # Mahasiswa.semester = 4

    #methode tanpa parameter
    def siapa(self):
        print('Saya Mahasiswa dengan nim ',self.nim,' nama = ',self.nama, ' Jurusan = ',self.jurusan)

    def semester(self,sems):
        self.sem = sems

    def getSemester(self):
        return self.sem
        

mhs1 = Mahasiswa('2114001','Rani','SI-D3','3')
mhs2 = Mahasiswa('2114002','Rana','SI-S1','4')

print(mhs1.siapa(),'Semester = ',mhs1.getSemester())
print(mhs2.siapa(), ' Semester = ',mhs2.getSemester())
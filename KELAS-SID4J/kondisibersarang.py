
email = input('Email = ')
emailTerdaftar = 'nasruddin@gmail.com'
pwd = '123'

if email == emailTerdaftar:
    password = input('Password = ')
    if password == pwd :
        print('Login Sukses....')
    else:
        print('Password anda salah')
else:
    print('Email Tidak Terdaftar..')
    
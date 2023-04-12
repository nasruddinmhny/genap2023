
hurufVokal = ['a','e','i','o','u','A','E','i','O','U']
huruf = input('Input Huruf = ')

for i in range(len(huruf)):
    
    if huruf[i] in hurufVokal:
        print('huruf = ',ord(huruf[i]),' Adalah Huruf Vokal')
    else:
        print('huruf = ',ord(huruf[i]),' Bukan Huruf Vokal')

#menampilkan angka bilangan genap dan ganjil

# bilangan yang dibagi 2 memiliki sisa hasil 0 itu adalah bilangan genap

#input = 1236945875

#output
#bilangan genap = 2 6 4 8 -> 2 4 6 8
#bilangan ganjil = 1 3 9 5 7 5 -> 1 3 5 5 7 9


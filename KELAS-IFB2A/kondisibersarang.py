

'''
    jika saya beli baju
        jika saya beli baju olahraga maka saya akan berolahraga
        jika saya beli baju tidur maka saya akan tidur
        jika saya beli baju kerja maka saya akan kerja
        selain dari itu saya tidak akan membeli baju
    jika saya beli tas


'''

pilihan = input('Mau beli apa = ')

if pilihan == 'baju':

    pilihanBaju = input('Mau beli baju apa = ')

    if pilihanBaju == 'olahraga':
        print('saya akan olahraga')
    elif pilihanBaju == 'tidur':
        print('saya akan tidur')
    elif pilihanBaju == 'kerja':
        print('saya akan kerja')
    else:
        print('baju tidak tersedia')

elif pilihan == 'tas':
    pilihanTas = input('Mau beli tas apa = ')

    if pilihanTas == 'ransel':
        print('tasnya saya pake kuliah')
    else:
        print('tas tidak tersedia')
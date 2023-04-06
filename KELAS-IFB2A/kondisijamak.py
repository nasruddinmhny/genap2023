
uangAnda = int(input('Input jumlah nominal uang anda = '))

if uangAnda >= 35000 and uangAnda <= 50000 :
    print('Uangnya cocok untuk beli kaos')

elif uangAnda >= 51000 and uangAnda <= 60000:
    print('Uang cocok untuk beli jilbab')

elif uangAnda >= 61000 and uangAnda <= 100000:
    print('Uang cocok untuk beli tas')

else:
    print('Maaf uangnya tidak cukup')



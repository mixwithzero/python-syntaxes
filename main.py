"""
menunjukan semua sintaxes python
"""
from geometry.segitiga import hitung_luas_segitiga
from geometry.persegi_panjang import hitung_luas_persegi_panjang
from geometry_class.segitiga import segitiga

print('hello world')

# menghitung luas segitiga
alas = 10
tinggi = 3
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)
# menggunakan logika percabangan
if luas_segitiga < 30:
    print('kecil')
elif luas_segitiga == 30:
    print('cukupan')
else:
    print('besar bianget')
    #membuat perulangan
print('1' , luas_segitiga)
print('2' , luas_segitiga)
print('3' , luas_segitiga)
print('4' , luas_segitiga)
print('5' , luas_segitiga)
print('6' , luas_segitiga)
print('7' , luas_segitiga)
print('8' , luas_segitiga)
print('9' , luas_segitiga)
print('10', luas_segitiga)

#...Dengan Cara Seperti ini
print('dengan For')
for i in range(0 , 10):
    print(i+1 , luas_segitiga)


    # MODULARISASI TAHAP PERTAMA PEMBUATAN FUNGSI
print('segitiga 1')
alas = 10
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)

print('segitiga 2')
alas = 7
tinggi = 8
luas_segitiga = alas * tinggi / 2
print(luas_segitiga)



print(hitung_luas_segitiga('segitiga 1' , 10, 5))
print(hitung_luas_segitiga('segitiga 2' , 7, 8))

#MODULARISASI TAHAP KEDUA PEMBUATAN PACKAGE
print(hitung_luas_persegi_panjang('persegi1' , 10 , 11))
print(hitung_luas_persegi_panjang('persegi2' , 11 , 5))

segitiga1 = segitiga ('segitiga 1 as class' , 6 , 10)
print(segitiga1.title)
print(segitiga1.hitung_luas())
segitiga2 = segitiga ('segitiga 2 as class' , 8 , 10)
print(segitiga2.title)
print(segitiga2.hitung_luas())

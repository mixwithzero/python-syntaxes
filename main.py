"""
menunjukan semua sintaxes python
"""
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

def hitung_luas_segitiga(title, alas, tinggi):
    print(title)
    return alas * tinggi / 2

print(hitung_luas_segitiga('segitiga 1', 10, 5))
print(hitung_luas_segitiga('segitiga 2', 7, 8))
import math

def luas_lingkaran(r):
    return math.pi * r * r

def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_segitiga(a, t):
    return 0.5 * a * t

def luas_persegi(s):
    return s * s

print("Menghitung Luas dan Keliling Lingkaran")
r = float(input("Masukkan jari-jari lingkaran: "))
print("Luas lingkaran: ", luas_lingkaran(r))
print("Keliling lingkaran: ", keliling_lingkaran(r))

print("Menghitung Luas Segitiga")
a = float(input("Masukkan alas segitiga: "))
t = float(input("Masukkan tinggi segitiga: "))
print("Luas segitiga: ", luas_segitiga(a, t))

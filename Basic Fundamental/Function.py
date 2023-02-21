# def nama_fungsi():
#   print("Hello World")

# Cara memanggil fungsi
# nama_fungsi()

def salam(ucapan):
  print(ucapan)

for i in range(10):
  salam("Selamat Pagi sabil")

# Fungsi dengan return value
def luas_segitiga(alas, tinggi):
  luas = alas * tinggi / 2
  return luas

print(luas_segitiga(10, 6))
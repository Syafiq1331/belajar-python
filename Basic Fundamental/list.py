# Membuat list kosong

list_kosong = []

# Membuat list dengan isi

hobi = ["Membaca", "Menulis", "Menggambar"]

# Membuat list dengan berbagai tipe data

laci = ["Buku", 10, 3.14, True]

# Mengambil data dari list

print(hobi[0]) # Membaca
print(laci[2]) # 3.14

# Mengubah data dari list
laci[2] = 2.71


# Menambahkan item pada list
# append(item) => Menampilkan isi list dari belakang
# insert(index, item) => Menampilkan isi list dari index tertentu

hobi.append("Menggambar")
hobi.insert(1, "Menggambar")

print(hobi)


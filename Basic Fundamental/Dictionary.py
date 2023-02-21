# Fungsi dari tipe data dictionary di dalam python itu seperti sebuah object di dalam javascript

# nama_dict = {
#     "key": "value"
# }

nama_siswa = {
    "nama": "Rizky",
    "kelas": "XI RPL 1",
    "umur": 16,
    "alamat" : "Jl. Raya Cibaduyut",
    "hobi": ["Membaca", "Menulis", "Menggambar"],
    "menikah": False,
    "nilai": {
        "matematika": 90,
        "bahasa indonesia": 80,
        "bahasa inggris": 70,
        "ipa": 85
    }
}

# Print semua data yang ada di dalam dictionary
print(nama_siswa)

# Print data berdasarkan key
print("Print data berdasarkan key")
print("Nama Siswa: ", nama_siswa["nama"])
print("Kelas: ", nama_siswa["kelas"])
print("Umur: ", nama_siswa["umur"])

# Print data dengan menggunakan method get()
print("Print data dengan menggunakan method get()")
print("Alamat: ", nama_siswa.get("alamat"))

# Print dengan data yang sudah di looping
print("Print dengan data yang sudah di looping")
for key in nama_siswa:
    print(key, ":", nama_siswa[key])
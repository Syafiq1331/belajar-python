total_belanja = input("Total Belanja: Rp ")

bayar = total_belanja

barang = int(total_belanja)

if barang >= 100000:
    bayar = barang - (barang * 0.1)

print  ("Total Bayar: Rp", bayar)

inputData = input("Angka yang kamu masukkan : ")
if inputData != int :
    print("Inputan harus berupa angka")
else :
    if inputData % 2 == 0 :
        print("Angka yang kamu masukkan adalah bilangan genap")
    else :
        print("Angka yang kamu masukkan adalah bilangan ganjil")

#Menentukan Kelulusan
teori = float(input("Masukan nilai teori anda :"))
praktek = int(input("Masukan nilai praktek anda :"))
if teori>=70 and praktek>=70 :
    print("Selamat, anda lulus!")
elif teori>=70 and praktek<70:
    print("Anda harus mengulang ujian praktek")
elif teori<70 and praktek>=70:
    print("Anda harus mengulang ujian teori")
else :
    print("Anda harus mengulang ujian teori dan praktek") 
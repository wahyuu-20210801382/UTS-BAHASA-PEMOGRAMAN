from tkinter import Menu, Menubutton

print("data pelanggan")

NAMA = input("MASUKKAN NAMA :")
NIM = input ("MASUKKAN NIM :")
ALAMAT = input ("MASUKKAN ALAMAT :")

print("\n\n\nnama :", NAMA)
print("nim :",NIM)
print("alamat :",ALAMAT)

print('\n\t\t selamat datang di cafe ceria')
print('\n\t\t ada yang bisa kami bantu')


MENU ={ "masukkan pilihan  "
    "COKLAT"    : 5000,
    "teh"       : 5000,
    "coffe"     : 8000,
    "Capucino"   : 10000,
    "exit "     : 000,
}    

print("============================== DAFTAR MENU =====================")
print("  cokelat = Rp. 5000")
print("  teh     = Rp. 5000")
print("  coffe   = Rp. 8000")
print("  Capucino = Rp. 10000 ")
print("  exit")
print("===============================================================")
print(" Anda mendapatkan PPN sebesar 10% ")
print(" pembelian diatas Rp. 100.000,- mendapatkan cashback sebesar 15%")
print("=================================================================")

beli = input("PILIH MENU: ") 
jumlah = int(input("jumlah pesanan :"))
ppn = 500

bayar = (jumlah*MENU[beli]+ppn)

if bayar >100000 :
    ppn = bayar+500
    total = bayar

else :
    total = bayar

print("====================Detail Pembayaran =====================")
print("menu yang di pesan               : ", beli)
print("Jumlah yang di pesan             : ", jumlah)
print("PPN                              : ", ppn)
print(" total biaya                     : ", bayar)
print(" Total semua yang harus di bayar : ",total)
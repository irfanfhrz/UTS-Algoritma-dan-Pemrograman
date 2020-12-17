#sistem informasi bank sampah
#muhammad irfan fahriza

def salam():
    print("-----------------------------")
    print("      -Selamat Datang-       ")
    print(" SISTEM INFORMASI BANK SAMPAH")
    print("-----------------------------")
    
    
salam()    

print("         Login                       ")
pengguna = input("Login admin atau nasabah :")

username = input("Username: ")
passwd = input("Password: ")
print("----------------------")

if username == 'admin':
    if passwd == '2468':
        print("Anda Berhasil Login")
    else:
        print("Maaf Username atau Password salah")
elif username == 'nasabah':
    if passwd == '1357':
        print("Anda Berhasil Login")
    else:
        print("Maaf Username atau Password salah")
               
def menu_utama():
    sampah = int(input("berat sampah anda: "))
    print(" Kategori Sampah ")
    print("1.Sampah Organik")
    print("2.Sampah Anorganik")
    print("3.Sampah Campuran")
    daftar = int(input("Kategori sampah anda:"))
    if daftar == 1:
        harga_sampah_organik = sampah * 3500     
        print()
        print("Hasil penjualan: ",harga_sampah_organik)
        print()
    elif daftar == 2:
        harga_sampah_anorganik = sampah * 3000
        print()
        print("Hasil penjualan: ",harga_sampah_anorganik)
        print()
    elif daftar == 3:
        harga_sampah_campuran = sampah * 2500
        print()
        print("Hasil penjualan: ",harga_sampah_campuran)
        print()
        
pilihan = 1
while pilihan!=0:
    print("----------------------")
    print("    Menu Tampilan     ")
    print("1. Macam - macam sampah")
    print("2. Daftar Harga sampah")
    print("3. Setor Sampah")
    print("0. Keluar")
    print("----------------------")
    print()
    pilihan = int(input("Masukkan pilihan tampilan: "))
    if pilihan == 1:
        print("sampah organik :")
        print("1.daun kering   3.buah busuk")
        print("2.kertas bekas  4.minyak goreng bekas")
        print("Harga sampah anorganik : ")
        print("1.plastik       3.botol plastik")
        print("2.ban bekas     4.seng/logam")
    elif pilihan == 2:
        print("Harga sampah")
        print("sampah organik 3500/kg")
        print("sampah anorganik 3000/kg")
        print("sampah campuran 2500/kg")
        print
    elif pilihan == 3:
         menu_utama()

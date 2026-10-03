username = "Ririn"
password = "017"
pin = "017017"

saldo = 5000000
min_transfer = 50000
max_transfer = 1000000

berhasil_login = False
for percobaan in range(1, 4):
    print(f"LOGIN (Percobaan {percobaan}/3)")
    user_input = input("Masukkan username: ")
    pass_input = input("Masukkan password: ")
    if user_input == username:
        if pass_input == password:
            berhasil_login = "ya"
            print("Login berhasil!")
            break
        else:
            print("Login gagal")
    else:
        print("Login gagal")
if berhasil_login == "ya":
    menu = "ya"
    while menu == "ya":
        print("MENU ATM")
        print("1. Transfer Uang")
        print("2. Logout")
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == "1": 
            lagi = "y"
            while(lagi == "y"): 
                print("Saldo saat ini: Rp", saldo)
                penerima = input("Username penerima: ")
                nominal = int(input("Nominal transfer: Rp "))

                if nominal < min_transfer:
                    print("Nominal transfer minimal Rp50.000,00")
                    lagi = "n"
                elif nominal > max_transfer:
                    print("Nominal transfer maksimal Rp1.000.000,00")
                    lagi = "n"
                elif nominal > saldo:
                    print("Nominal tidak boleh melebihi saldo")
                    lagi = "n"
                else:
                    pin_input = input("Masukkan PIN: ")
                    if pin_input == pin:
                        saldo = saldo - nominal
                        print("STRUK BUKTI TRANSFER")
                        print("Pengirim: ", username)
                        print("Penerima: ", penerima)
                        print("Nominal: Rp", nominal)
                        lagi = input("Apakah ingin melakukan transfer lagi? (y/n): ")
                    else:
                        print("PIN salah, transfer dibatalkan")
                        lagi = "n"
        elif pilihan == "2":
            print("Anda telah logout. Terima kasih telah menggunakan layanan kami.")
            menu = "tidak"
        else:
            print("Pilihan tidak valid.")
else:
    print("Akun anda diblokir karena gagal melakukan login sebanyak 3 kali.")
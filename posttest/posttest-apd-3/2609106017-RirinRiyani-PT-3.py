nama = input("Masukkan nama pembeli: ")
umur = int(input("Masukkan umur pembeli: "))
jenis_tiket = input("Masukkan jenis tiket (Reguler/Premium/VIP): ")
status_member = input("Apakah anda member? (Ya/Tidak): ")
uang_bayar = int(input("Masukkan nominal uang bayar: "))

if umur < 13:
    print("mohon maaf, anda belum cukup umur untuk menonton")
else:
    if jenis_tiket == "Reguler":
        harga_tiket = 50000
        print("Tiket Reguler dipilih.")
    elif jenis_tiket == "Premium":
        harga_tiket = 75000
        print("Tiket Premium dipilih.")
    elif jenis_tiket == "VIP":
        harga_tiket = 100000
    else:
        harga_tiket = 0
        print("Jenis tiket tidak valid.")
    print("Harga tiket:", harga_tiket)
    diskon = 0.2 if status_member == "Ya" else 0
    print("Diskon:", diskon)
    nominal_diskon = harga_tiket * diskon
    print("Nominal diskon:", nominal_diskon)
    biaya_admin = 0 if status_member == "Ya" else 2000
    total_bayar = harga_tiket - nominal_diskon + biaya_admin
    print("Total bayar:", total_bayar)
    if jenis_tiket not in ["Reguler", "Premium", "VIP"]:
        print("Transaksi dibatalkan: jenis tiket tidak valid.")
    elif uang_bayar < total_bayar:
        print("Transaksi dibatalkan: uang bayar kurang dari total bayar.")
    else:
        kembalian = uang_bayar - total_bayar
        print("===== STRUK PEMBELIAN =====")
        print("Nama: ", nama)
        print("Umur: ", umur)
        print("Jenis Tiket:", jenis_tiket)
        print("Status Member:", status_member)
        print("Total Bayar:", total_bayar)
        print("Kembalian:", kembalian)
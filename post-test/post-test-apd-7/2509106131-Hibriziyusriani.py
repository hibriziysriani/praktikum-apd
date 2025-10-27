import os
from prettytable import PrettyTable

# ======== VARIABEL GLOBAL ========
data_pemesanan = {
    "Rijie": {"no_hp": "081234567890", "jumlah": 2, "metode_pembayaran": "Transfer Bank"},
    "Luna": {"no_hp": "082145678921", "jumlah": 1, "metode_pembayaran": "QRIS"},
}

data_pengguna = {
    "rijie": {"password": "admin123", "level_akses": "admin"}
}

login_status = False  # Variabel global tambahan

# ======== FUNGSI ========

# Fungsi tanpa parameter (menampilkan seluruh pemesanan)
def tampilkan_pemesanan():
    os.system("cls || clear")
    print("=== Daftar Pemesanan ===")
    if len(data_pemesanan) == 0:
        print("Belum ada Pemesanan")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama", "No HP", "Jumlah Tiket", "Metode Pembayaran"]
        tabel.hrules = 1
        for i, (nama, data) in enumerate(data_pemesanan.items(), start=1):
            tabel.add_row([i, nama, data["no_hp"], data["jumlah"], data["metode_pembayaran"]])
        print(tabel)
    input("\nTekan Enter untuk kembali...")

# Fungsi tanpa parameter (login user)
def login():
    global login_status
    os.system("cls || clear")
    print("==============================")
    print("     LOGIN SISTEM PEMESANAN    ")
    print("==============================")
    username_input = input("Masukkan username: ").lower()
    password_input = input("Masukkan password: ").strip()

    for username, data in data_pengguna.items():
        if username == username_input and data["password"] == password_input:
            print("Login berhasil!")
            login_status = True
            return data["level_akses"]
    print("Login gagal! Username atau password salah.")
    return None

# Fungsi dengan parameter (menambah pemesanan)
def tambah_pemesanan(nama, nomor_hp, jumlah_tiket, metode_pembayaran):
    try:
        if nama in data_pemesanan:
            raise ValueError("Nama sudah terdaftar.")
        if not jumlah_tiket.isdigit() or int(jumlah_tiket) <= 0:
            raise ValueError("Jumlah tiket harus berupa angka positif.")
        data_pemesanan[nama] = {
            "no_hp": nomor_hp,
            "jumlah": int(jumlah_tiket),
            "metode_pembayaran": metode_pembayaran
        }
        print(f"Pemesanan atas nama {nama} berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")

# Fungsi dengan parameter (menghapus pemesanan)
def hapus_pemesanan(nama):
    try:
        if nama not in data_pemesanan:
            raise KeyError("Nama tidak ditemukan dalam data pemesanan.")
        del data_pemesanan[nama]
        print(f"Pemesanan {nama} berhasil dihapus.")
    except KeyError as e:
        print(f"Error: {e}")

# ======== PROSEDUR ========

# Prosedur menampilkan menu
def tampilkan_menu():
    os.system("cls || clear")
    print("\n==============================")
    print("   BOOKING TIKET KONSER THE SIGIT")
    print("==============================")

    table = PrettyTable()
    table.field_names = ["No", "Menu"]
    table.align["No"] = "c"
    table.align["Menu"] = "l"

    table.add_row(["1", "Lihat semua pemesanan"])
    table.add_row(["2", "Tambah pemesanan"])
    table.add_row(["3", "Hapus pemesanan"])
    table.add_row(["4", "Keluar"])
    print(table)

# Prosedur utama menjalankan program
def jalankan_program():
    level_akses = login()
    if not login_status:
        return

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tampilkan_pemesanan()

        elif pilihan == "2":
            os.system("cls")
            print("=== Tambah Pemesanan ===")
            # variabel lokal
            nama = input("Nama: ").strip()
            nomor_hp = input("Nomor HP: ").strip()
            jumlah_tiket = input("Jumlah tiket: ").strip()
            metode = input("Metode pembayaran: ").strip()
            tambah_pemesanan(nama, nomor_hp, jumlah_tiket, metode)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "3":
            os.system("cls")
            print("=== Hapus Pemesanan ===")
            tampilkan_pemesanan()
            nama = input("Masukkan nama yang ingin dihapus: ").strip()
            hapus_pemesanan(nama)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid! Coba lagi.")

# ======== MAIN PROGRAM ========
if __name__ == "__main__":
    jalankan_program()

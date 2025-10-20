import os
from prettytable import PrettyTable

# Mengubah struktur data dari list of tuples menjadi dictionary
data_pemesanan = {
    "Rijie": {"no_hp": "081234567890", "jumlah": 2, "metode_pembayaran": "Transfer Bank"},
    "Luna": {"no_hp": "082145678921", "jumlah": 1, "metode_pembayaran": "QRIS"},
}

data_pengguna = {
    "rijie": {"password": "admin123", "level_akses": "admin"}
}

# ======== LOGIN SYSTEM ========
os.system("cls || clear")
print("==============================")
print("     LOGIN SISTEM PEMESANAN    ")
print("==============================")

username_input = input("Masukkan username: ").lower()
password_input = input("Masukkan password: ").strip()

# Verifikasi login
level_akses = None
for username, data in data_pengguna.items():
    if username == username_input and data["password"] == password_input:
        level_akses = data["level_akses"]
        break

if level_akses is None:
    print("Login gagal! Username atau password salah.")
    exit()

while True:
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
    table.add_row(["3", "Ubah pemesanan"])
    table.add_row(["4", "Hapus pemesanan"])
    table.add_row(["5", "Keluar"])

    print(table)

    # Input pilihan menu
    menu = input("Pilih menu (1-5): ").strip()

    # READ
    if menu == "1":
        os.system("cls")
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

    # CREATE
    elif menu == "2":
        os.system("cls")
        print("=== Tambah Pemesanan ===")
        nama = input("Nama: ").strip()
        if nama in data_pemesanan:
            print("Nama sudah ada, gunakan nama lain.")
        else:
            nomor_hp = input("Nomor HP: ").strip()
            jumlah_tiket_input = input("Jumlah tiket: ").strip()
            metode_pembayaran = input("Metode pembayaran: ").strip()
            if not nama or not nomor_hp or not jumlah_tiket_input or not metode_pembayaran:
                print("Semua data harus diisi.")
            elif not jumlah_tiket_input.isdigit() or int(jumlah_tiket_input) <= 0:
                print("Jumlah tiket harus angka lebih dari 0.")
            else:
                jumlah_tiket = int(jumlah_tiket_input)
                data_pemesanan[nama] = {
                    "no_hp": nomor_hp,
                    "jumlah": jumlah_tiket,
                    "metode_pembayaran": metode_pembayaran
                }
                print("Pemesanan berhasil ditambahkan.")

    # UPDATE
    elif menu == "3":
        print("\n=== UBAH PEMESANAN ===")
        if not data_pemesanan:
            print("Belum ada data untuk diubah.")
        else:
            for i, (nama, data) in enumerate(data_pemesanan.items(), start=1):
                print(f"{i}. {nama} | {data['no_hp']} | {data['jumlah']} Tiket | {data['metode_pembayaran']}")

            pilih = input("Pilih nomor data yang ingin diubah: ").strip()
            if not pilih.isdigit():
                print("Input harus berupa angka!")
            else:
                pilih = int(pilih)
                if not (1 <= pilih <= len(data_pemesanan)):
                    print("Nomor tidak valid!")
                else:
                    nama_lama = list(data_pemesanan.keys())[pilih - 1]
                    nama_baru = input("Nama baru: ").strip()
                    hp_baru = input("No HP baru: ").strip()
                    jumlah_baru_input = input("Jumlah tiket baru: ").strip()
                    bayar_baru = input("Metode pembayaran baru: ").strip()

                    if not nama_baru or not hp_baru or not jumlah_baru_input or not bayar_baru:
                        print("Semua data harus diisi.")
                    elif not jumlah_baru_input.isdigit() or int(jumlah_baru_input) <= 0:
                        print("Jumlah tiket harus angka lebih dari 0.")
                    else:
                        jumlah_baru = int(jumlah_baru_input)
                        # Jika nama berubah, hapus yang lama dan tambah yang baru
                        if nama_baru != nama_lama:
                            del data_pemesanan[nama_lama]
                        data_pemesanan[nama_baru] = {
                            "no_hp": hp_baru,
                            "jumlah": jumlah_baru,
                            "metode_pembayaran": bayar_baru
                        }
                        print("Data berhasil diperbarui!")

    # DELETE
    elif menu == "4":
        print("\n=== HAPUS PEMESANAN ===")
        if not data_pemesanan:
            print("Belum ada data untuk dihapus.")
        else:
            for i, (nama, data) in enumerate(data_pemesanan.items(), start=1):
                print(f"{i}. {nama} | {data['no_hp']} | {data['jumlah']} Tiket | {data['metode_pembayaran']}")

            pilih = input("Pilih nomor data yang ingin dihapus: ").strip()
            if not pilih.isdigit():
                print("Input harus berupa angka!")
            else:
                pilih = int(pilih)
                if not (1 <= pilih <= len(data_pemesanan)):
                    print("Nomor tidak valid!")
                else:
                    nama_hapus = list(data_pemesanan.keys())[pilih - 1]
                    konfirmasi = input(f"Yakin hapus {nama_hapus}? (y/n): ").lower().strip()
                    if konfirmasi == "y":
                        del data_pemesanan[nama_hapus]
                        print("Data berhasil dihapus!")
                    else:
                        print("Batal dihapus.")

    # EXIT
    elif menu == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid, coba lagi!")

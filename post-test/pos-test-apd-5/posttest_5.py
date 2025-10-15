import os
from prettytable import PrettyTable

data_pemesanan = [
    ("Rijie", "081234567890", 2, "Transfer Bank"),
    ("Luna", "082145678921", 1, "QRIS"),
]

data_pengguna = [("rijie", "admin123", "admin")]


# ======== LOGIN SYSTEM ========
os.system("cls || clear")
print("==============================")
print("     LOGIN SISTEM PEMESANAN    ")
print("==============================")

username_input = input("Masukkan username: ").lower()
password_input = input("Masukkan password: ").strip()

# Verifikasi login
for u in data_pengguna:
    if u[0] == username_input and u[1] == password_input:
        level_akses = u[2]

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
        print("=== Daftar  ===")
        if len(data_pemesanan) == 0:
            print("Belum ada Pemesanan")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama", "No hp", "jumlah", "nama pembayaran"]
            tabel.hrules = 1
            for i in range(len(data_pemesanan)):
                nama, noHp, jumlah, bayar = data_pemesanan[i]
                tabel.add_row([i+1, nama, noHp, jumlah, bayar ])
            print(tabel)
        input("\nTekan Enter untuk kembali...")

    elif menu == "2":
            os.system("cls")
            print("=== Tambah Pemesanan ===")
            nama = input("nama :")
            nomor_hp = input("nomor hp : ")
            jumlah_tiket = input("jumlah tiket: ")
            metode_pembayaran = input("metode pembayaran: ")
            data_pemesanan.append([nama, nomor_hp, jumlah_tiket, metode_pembayaran])
            print("n/pemesanan berhasil ditambahkan")



    # UPDATE
    elif menu == "3":
        print("\n=== UBAH PEMESANAN ===")
        if not data_pemesanan:
            print("Belum ada data untuk diubah.")
        else:
            for i, (nama, hp, jumlah, bayar) in enumerate(data_pemesanan, start=1):
                print(f"{i}. {nama} | {hp} | {jumlah} Tiket | {bayar}")

            pilih = input("Pilih nomor data yang ingin diubah: ").strip()
            if not pilih.isdigit():
                print("Input harus berupa angka!")
            else:
                pilih = int(pilih)
                if not (1 <= pilih <= len(data_pemesanan)):
                    print(" Nomor tidak valid!")
                else:
                    nama_baru = input("Nama baru: ").strip()
                    hp_baru = input("No HP baru: ").strip()
                    jumlah_baru_input = input("Jumlah tiket baru: ").strip()
                    bayar_baru = input("Metode pembayaran baru: ").strip()

                    if not nama_baru or not hp_baru or not jumlah_baru_input or not bayar_baru:
                        print(" Semua data harus diisi.")
                    elif not jumlah_baru_input.isdigit() or int(jumlah_baru_input) <= 0:
                        print(" Jumlah tiket harus angka lebih dari 0.")
                    else:
                        jumlah_baru = int(jumlah_baru_input)
                        data_pemesanan[pilih - 1] = (nama_baru, hp_baru, jumlah_baru, bayar_baru)
                        print(" Data berhasil diperbarui!")

    # DELETE
    elif menu == "4":
        print("\n=== HAPUS PEMESANAN ===")
        if not data_pemesanan:
            print("Belum ada data untuk dihapus.")
        else:
            for i, (nama, hp, jumlah, bayar) in enumerate(data_pemesanan, start=1):
                print(f"{i}. {nama} | {hp} | {jumlah} Tiket | {bayar}")

            pilih = input("Pilih nomor data yang ingin dihapus: ").strip()
            if not pilih.isdigit():
                print("Input harus berupa angka!")
            else:
                pilih = int(pilih)
                if not (1 <= pilih <= len(data_pemesanan)):
                    print(" Nomor tidak valid!")
                else:
                    konfirmasi = input(f"Yakin hapus {data_pemesanan[pilih - 1][0]}? (y/n): ").lower().strip()
                    if konfirmasi == "y":
                        del data_pemesanan[pilih - 1]
                        print(" Data berhasil dihapus!")
                    else:
                        print("Batal dihapus.")

    # EXIT
    elif menu == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid, coba lagi!")

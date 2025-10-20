
nama = input("Masukkan nama pelanggan: ")
banyak_bata = int(input("Masukkan jumlah batu bata yang akan dibeli: "))
banyak_semen = int(input("Masukkan jumlah karung semen yang akan dibeli: "))

harga_bata = 100
harga_semen = 100000

total_awal = (banyak_bata * harga_bata) + (banyak_semen * harga_semen)

paket_hemat = (banyak_bata == 500 and banyak_semen == 5)
paket_ultra_mantap = (banyak_bata == 2000 and banyak_semen == 16)

if paket_hemat:
    diskon_persen = 15 / 100
    keterangan_diskon = "Paket Hemat 15%"
elif paket_ultra_mantap:
    diskon_persen = 30 / 100
    keterangan_diskon = "Paket Ultra Mantap 30%"
else:
    diskon_persen = 0
    keterangan_diskon = "Tidak Ada Diskon"

jumlah_diskon = total_awal * diskon_persen
total_akhir = total_awal - jumlah_diskon

print("\n=== RINGKASAN PESANAN ===")
print(f"Nama Pelanggan       : {nama}")
print(f"Jumlah Batu Bata     : {banyak_bata} biji")
print(f"Jumlah Karung Semen  : {banyak_semen} karung")
print(f"Biaya Total Awal     : Rp{total_awal:,}")
print(f"Keterangan Diskon    : {keterangan_diskon}")
print(f"Jumlah Diskon        : Rp{int(jumlah_diskon):,}")
print(f"Total Biaya Akhir    : Rp{total_akhir:,.2f}")

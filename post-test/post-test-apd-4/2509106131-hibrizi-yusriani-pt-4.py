nim = int(input("MASUKAN 3 DIGIT NIM TRAKHIR:"))
nim1 = int(input("MASUKAN 2 DIGIT NIM TRAKHIR:"))
nim2 = int(input("MASUKAN NIM DIGIT TRAKHIR KEDUA:"))

stamina = nim
chakra = 0

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("Misi 1: Menyempurnakan Rasengan")
print(f"Chakra terkumpul: {chakra}")
print(f"Sisa stamina: {stamina}")

if chakra >= 200:
    print("Naruto menyempurnakan Rasengan")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra")


tinggi_menara = nim1
gulungan = 0

for tinggi in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print("Misi 2: Infiltrasi Menara")
print(f"Tinggi menara: {tinggi_menara} meter")
print(f"Gulungan informasi ditemukan: {gulungan}")

koridor = nim2
intel = 0
perangkap = 0

for i in range(1, koridor + 1):
    for r in range(1, 4):
        nomor = (i - 1) * 3 + r
        if nomor % 2 == 1:
            intel += 1
        else:
            perangkap += 1

print("Misi 3: Penyelidikan Markas Rahasia")
print(f"Jumlah koridor: {koridor}")
print(f"Data intelijen ditemukan: {intel}")
print(f"Perangkap peledak dijinakkan: {perangkap}")

print("Naruto berhasil menyelesaikan semua misi")

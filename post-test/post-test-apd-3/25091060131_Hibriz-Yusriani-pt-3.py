nama = input("Masukkan nama karyawan : ")
jabatan = input("Maukkan jabatan karyawan : ")
hari = int(input("Masukkan hari kerja : "))
jam =  int(input("Masukkan jam kerja : "))
jumlah_lembur = int(input("masukkan jumlah lembur : "))


if jabatan == "peracik petasan":
    if hari >= 18 and jam >= 6 and jumlah_lembur >= 2:
        bayaran = 20000
        lembur = 10000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)
    elif hari >= 24 and jam >= 8 and jumlah_lembur >= 4:
        bayaran = 25000
        lembur = 15000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)
    else:
        bayaran = 15000
        lembur = 10000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)
elif jabatan == "pengantar petasan":
    if hari >= 16 and jam >= 5 and jumlah_lembur >= 4:
        bayaran = 20000
        lembur = 15000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)
    elif hari >= 20 and jam >= 7 and jumlah_lembur >= 7:
        bayaran = 25000
        lembur = 20000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)
    else:
        bayaran = 15000
        lembur = 12000
        gaji = (bayaran * jam) * hari + (jumlah_lembur * lembur)

print("PERHITUNGAN GAJI KARYAWAN PT.BOM")        
print(f"Karyawan atas nama: {nama}")
print(f"Jumlah hari kerja: {hari}")
print(f"jumlah jam kerja: {hari}")
print(f"Jumlah lembur: {jumlah_lembur}")
print(f"Bayaran per jam: {bayaran}")
print(f"Bayaran per lembur: {lembur}")
print(f"Dengan jabatan sebagai: {jabatan}")
print(f"Mendapatkan gaji: Rp.{gaji:,.0f}")
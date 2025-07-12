import csv

# Membaca data dari Keuangan.csv
def baca_data():
    with open("Keuangan.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        data = []
        for row in reader:
            # Konversi kolom Pemasukan & Pengeluaran ke int, isi 0 jika kosong
            row["Pemasukan"] = int(row.get("Pemasukan", "0").strip() or 0)
            row["Pengeluaran"] = int(row.get("Pengeluaran", "0").strip() or 0)
            data.append(row)
        return data

# Menampilkan semua data
def lihat_data():
    data = baca_data()
    print("\n=== Data Keuangan ===")
    print("{:<3} {:<12} {:<12} {:<30} {:>12} {:>15}".format(
        "No", "Tanggal", "Jenis", "Keterangan", "Pemasukan", "Pengeluaran"
    ))
    for row in data:
        print("{:<3} {:<12} {:<12} {:<30} {:>12} {:>15}".format(
            row["No"], row["Tgl"], row["Jenis"], row["Keterangan"],
            row["Pemasukan"], row["Pengeluaran"]
        ))

# Menambah data baru
def tambah_data():
    data = baca_data()
    no_baru = int(data[-1]["No"]) + 1 if data else 1
    tgl = input("Tanggal        : ")
    jenis = input("Jenis (Pemasukan/Pengeluaran): ").capitalize()
    ket = input("Keterangan     : ")

    if jenis == "Pemasukan":
        masuk = input("Jumlah Pemasukan  : ") or "0"
        keluar = "0"
    elif jenis == "Pengeluaran":
        keluar = input("Jumlah Pengeluaran: ") or "0"
        masuk = "0"
    else:
        print("Jenis tidak valid!!!")
        return
 
    with open("Keuangan.csv", mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([no_baru, tgl, jenis, ket, masuk, keluar])

    print("Data berhasil ditambahkan!")

# Menampilkan ringkasan saldo
def lihat_ringkasan():
    data = baca_data()
    total_masuk = sum(row["Pemasukan"] for row in data)
    total_keluar = sum(row["Pengeluaran"] for row in data)
    saldo = total_masuk - total_keluar

    print("\n=== Ringkasan Keuangan ===")
    print(f"Total Pemasukan   : Rp{total_masuk:,}")
    print(f"Total Pengeluaran : Rp{total_keluar:,}")
    print(f"Saldo Akhir       : Rp{saldo:,}")

# Menu utama
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Lihat Ringkasan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        lihat_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        lihat_ringkasan()
    elif pilihan == "4":
        print("Program selesai. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1–4.")

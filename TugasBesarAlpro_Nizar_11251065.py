#INI WATERMARK RIYAL NO FEK
#PUNYA NIJAR RIYAL NO FEK
import os
def clear_console():
    os.system('cls') 

#list directories sparepart
sparepart_matic = [
    {"nama": "Oli Mesin", "harga": 35000, "interval": 2000},
    {"nama": "Oli Gardan", "harga": 20000, "interval": 6000},
    {"nama": "V-Belt", "harga": 85000, "interval": 15000},
    {"nama": "Kampas Rem", "harga": 30000, "interval": 8000},
    {"nama": "Busi", "harga": 25000, "interval": 8000},
]
sparepart_gigi = [
    {"nama": "Oli Mesin", "harga": 35000, "interval": 2000},
    {"nama": "Gear Set", "harga": 120000, "interval": 15000},
    {"nama": "Kampas Kopling", "harga": 70000, "interval": 12000},
    {"nama": "Kampas Rem", "harga": 30000, "interval": 8000},
    {"nama": "Busi", "harga": 25000, "interval": 8000},
]
#list sparepart berdasarkan input user
data = []

def create(data):
    clear_console()
    #input kilometer motor
    print("\n=== INPUT DATA PERAWATAN MOTOR ===")
    try:
        km_lalu = int(input("Masukkan KM Servis Terakhir : "))
        km_skrg = int(input("Masukkan KM Motor Saat Ini  : "))
        if km_skrg < km_lalu:
            print("KM saat ini tidak boleh lebih kecil dari KM lalu!")
            input("Tekan ENTER untuk ulang...")
            return data     
        jarak_tempuh = km_skrg - km_lalu
        print(f"Jarak tempuh sejak servis terakhir: {jarak_tempuh} km")
    except ValueError:
        print("Input KM harus berupa angka!")
        input("Tekan ENTER untuk kembali...")
        return data
    #input jenis motor
    print("\nPilih Jenis Motor:")
    print("1. Matic")
    print("2. Motor Gigi / Kopling")
    try:
        tipe = int(input("Masukkan pilihan (1/2): "))
        if tipe not in [1, 2]:
            print("Pilihan tidak valid!")
            return data
    except ValueError:
        print("Input harus berupa angka!")
        return data
    if tipe == 1:
        spare = sparepart_matic
        jenis = "Matic"
    else:
        spare = sparepart_gigi
        jenis = "Motor Gigi"
    perlu_ganti = []
    total = 0
    #proses pembacaan hasil input user
    for s in spare:
        if jarak_tempuh >= s["interval"]:
            perlu_ganti.append(s.copy())
            total += s["harga"]
    data.append({
        "km_lalu": km_lalu,
        "km_skrg": km_skrg,
        "jarak": jarak_tempuh,
        "jenis": jenis,
        "sparepart": perlu_ganti,
        "total": total
    })
    clear_console()
    #pengeluaran data tampilan hasil input user
    print("\n=== HASIL CEK PERAWATAN ===")
    tampilanList(perlu_ganti, total, jenis, km_skrg, km_lalu)
    input("\nData berhasil disimpan! Tekan ENTER untuk kembali...")
    clear_console()
    return data

def read(data):
    clear_console()
    #menampilkan data perawatan yang telah diinput
    print("\n===== DATA PERAWATAN TERSIMPAN =====\n")
    if not data:
        print("Belum ada data perawatan yang tersimpan.")
        input("\nTekan ENTER untuk kembali...")
        clear_console()
        return data
    for i, d in enumerate(data, start=1):
        print(f"\nDATA KE-{i}")
        print(f"{'-'*60}")
        tampilanList(d["sparepart"], d["total"], d["jenis"], d["km_skrg"], d["km_lalu"])
        print("\n")
    input("Tekan ENTER untuk kembali...")
    clear_console()
    return data

def update(data):
    #menambahkan sparepart baru ke data milik user
    clear_console()
    print("\n=== UPDATE DATA (TAMBAH SPAREPART) ===")
    if not data:
        print("Belum ada data riwayat untuk di-update.")
        input("Tekan ENTER untuk kembali...")
        return data
    print("Pilih Data Riwayat yang mau ditambah part-nya:")
    for i, d in enumerate(data, start=1):
        print(f"{i}. {d['jenis']} (KM: {d['km_skrg']}) - Total: Rp {d['total']}")
    try:
        idx = int(input("\nPilih nomor data: ")) - 1
        if idx < 0 or idx >= len(data):
            print("Nomor data tidak ditemukan!")
            input("Tekan ENTER untuk kembali...")
            return data
    except ValueError:
        print("Input harus angka!")
        return data
    print(f"\nMenambah part untuk Data ke-{idx+1}")
    nama_part = input("Masukkan nama sparepart tambahan: ")
    try:
        harga_part = int(input("Masukkan harga sparepart (Rp): "))
    except ValueError:
        print("Harga harus angka!")
        return data
    
    data[idx]["sparepart"].append({
        "nama": nama_part,
        "interval": "-", 
        "harga": harga_part
    })
    data[idx]["total"] += harga_part
    print("\nSparepart tambahan berhasil dimasukkan!")
    print(f"Total Baru: Rp {data[idx]['total']}")
    input("\nTekan ENTER untuk kembali ke menu utama...")
    clear_console()
    return data

def delete(data):
    #menghapus sparepart dari data milik user
    clear_console()
    print("\n=== HAPUS ITEM SPAREPART ===")
    if not data:
        print("Tidak ada data riwayat.")
        input("\nTekan ENTER untuk kembali...")
        clear_console()
        return data
    
    print("Pilih Data Riwayat yang mau diedit sparepart-nya:")
    for i, d in enumerate(data, start=1):
        print(f"{i}. {d['jenis']} (KM: {d['km_skrg']}) - Total: Rp {d['total']}")
    try:
        idx = int(input("\nPilih nomor data riwayat: ")) - 1
        if idx < 0 or idx >= len(data):
            print("Pilihan tidak valid!")
            input("\nTekan ENTER untuk kembali...")
            return data
    except ValueError:
        print("Input harus angka!")
        return data
    
    target_data = data[idx]
    sparepart_list = target_data["sparepart"]

    if not sparepart_list:
        print("\nData ini tidak memiliki list sparepart (kosong).")
        input("Tekan ENTER untuk kembali...")
        return data
    print(f"\nDAFTAR SPAREPART PADA DATA KE-{idx+1}:")
    print("-" * 50)
    for i, s in enumerate(sparepart_list, start=1):
        print(f"{i}. {s['nama']} (Rp {s['harga']})")
    print("-" * 50)
    try:
        part_idx = int(input("Pilih nomor sparepart yang ingin dihapus: ")) - 1
        if part_idx < 0 or part_idx >= len(sparepart_list):
            print("Pilihan sparepart tidak valid!")
            input("\nTekan ENTER untuk kembali...")
            return data
    except ValueError:
        print("Input harus angka!")
        return data
    
    item_hapus = sparepart_list.pop(part_idx)
    target_data["total"] -= item_hapus["harga"] 
    print(f"\nSparepart '{item_hapus['nama']}' berhasil dihapus!")
    print(f"Total Biaya Baru: Rp {target_data['total']}")
    input("\nTekan ENTER untuk kembali ke menu utama...")
    clear_console()
    return data

def tampilanList(sparepart, total, jenis=None, km_skrg=None, km_lalu=None):
    def get_interval(item):
        try:
            return int(item['interval'])
        except (ValueError, TypeError):
            return 0

    # sorting bubble sort berdasarkan interval
    n = len(sparepart)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if get_interval(sparepart[j]) > get_interval(sparepart[j+1]):
                sparepart[j], sparepart[j+1] = sparepart[j+1], sparepart[j]
    print(f"\n{'='*60}")
    if jenis:
        print(f"DATA MOTOR {jenis.upper()}")
        print(f"{'='*60}")
        print(f"Jenis Motor     : {jenis}")
        if km_lalu is not None:
            print(f"KM Lalu         : {km_lalu} km")
        print(f"KM Sekarang     : {km_skrg} km")
        if km_lalu is not None:
             print(f"Jarak Tempuh    : {km_skrg - km_lalu} km")
    else:
        print("DATA SPAREPART")   
    print(f"{'-'*70}")
    print(f"{'No.':<4} {'Nama Sparepart':<20} {'Interval (km)':<15} {'Harga':<15}")
    print(f"{'-'*70}")

    if sparepart:
        for i, s in enumerate(sparepart, start=1):
            interval_str = str(s['interval'])
            print(f"{i:<4} {s['nama']:<20} {interval_str:<15} Rp {s['harga']:<10}")
    else:
        print("   (Tidak ada sparepart / List kosong)")
    print(f"{'-'*70}")
    print(f"{'TOTAL BIAYA':<41}: Rp {total}")
    print(f"{'='*70}")

def menuUtama():
    print("\n===================================")
    print("=== Aplikasi Tracking Perawatan ===")
    print("===           Motor             ===")
    print("===================================")
    print("1. Tambah Data Perawatan (Input Data User)")
    print("2. Lihat Riwayat Data")
    print("3. Update Data (Tambah Part)")
    print("4. Hapus Data (Hapus Part)")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan not in [1, 2, 3, 4, 5]:
            print("Pilihan hanya 1 sampai 5.")
            return 0
        return pilihan
    except ValueError:
        print("Input harus berupa angka.")
        return 0
pilihan = 0
while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
print("Terima kasih sudah menggunakan aplikasi ini!")



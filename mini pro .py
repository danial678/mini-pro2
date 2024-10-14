from prettytable import PrettyTable
from datetime import datetime



# List data kuda dan riwayat transaksi
list_kuda = [
    {"id_kuda": "K001",
        "nama_kuda": "Pablo",
        "jenis_kuda": "Clydesdale",
        "deskripsi": "cocok untuk pekerjaan mengangkut",
        "harga": 75000,
        "tersedia": True},
    {"id_kuda": "K002",
        "nama_kuda": "Piky",
        "jenis_kuda": "Poni Shetland",
        "deskripsi": "Kuda yang imutan, cocok untuk fotografi",
        "harga": 50000,
        "tersedia": True},
    {"id_kuda": "K003",
        "nama_kuda": "Thunder",
        "jenis_kuda": "Arabian",
        "deskripsi": "Kuda kuat dan cepat, cocok untuk pacuan.",
        "harga": 80000,
        "tersedia": True},
    
]
riwayat_transaksi = []

# Fungsi untuk menambah kuda ke dalam list
def tambah_kuda():
    print("===== Tambah Kuda Baru =====")
    id_kuda = input("Masukkan ID kuda: ")
    nama_kuda = input("Masukkan nama kuda: ")
    jenis_kuda = input("Masukkan jenis kuda: ")
    deskripsi = input("Masukkan deskripsi kuda: ")
    harga = float(input("Masukkan harga kuda per jam: Rp"))
    
    kuda_baru = {
        "id_kuda": id_kuda,
        "nama_kuda": nama_kuda,
        "jenis_kuda": jenis_kuda,
        "deskripsi": deskripsi,
        "harga": harga,
        "tersedia": True
    }
    
    list_kuda.append(kuda_baru)
    print(f"Kuda {nama_kuda} berhasil ditambahkan.")

# Fungsi untuk menampilkan daftar kuda
def tampilkan_kuda():
    if list_kuda:
        print("===== Daftar Kuda =====")
        table = PrettyTable()
        table.field_names = ["ID Kuda", "Nama Kuda", "Jenis Kuda", "Status","Deskripsi", "Harga"]

        for kuda in list_kuda:
            status = "Tersedia" if kuda["tersedia"] else "Disewa"
            table.add_row([kuda["id_kuda"], kuda["nama_kuda"], kuda["jenis_kuda"], status,kuda["deskripsi"], kuda["harga"]])
        
        print(table)
    else:
        print("Tidak ada kuda yang terdaftar saat ini.")

# Fungsi untuk menampilkan riwayat transaksi
def tampilkan_riwayat_transaksi():
    if riwayat_transaksi:
        print("===== Riwayat Transaksi =====")
        table = PrettyTable()
        table.field_names = ["ID Kuda", "Nama Kuda", "Jenis Transaksi", "Waktu Transaksi", "Tujuan"]
        
        for transaksi in riwayat_transaksi:
            table.add_row([transaksi["ID Kuda"], transaksi["Nama Kuda"], transaksi["Jenis Transaksi"], transaksi["Waktu Transaksi"], transaksi["Tujuan"]])
        
        print(table)
    else:
        print("Belum ada riwayat transaksi.")

# Fungsi untuk menghapus kuda
def hapus_kuda():
    if list_kuda:
        print("===== Hapus Kuda =====")
        id_kuda = input("Masukkan ID kuda yang ingin dihapus: ")
        for kuda in list_kuda:
            if kuda["id_kuda"] == id_kuda:
                list_kuda.remove(kuda)
                print(f"Kuda dengan ID {id_kuda} berhasil dihapus.")
                return
        print("Tidak ada kuda dengan ID tersebut.")
    else:
        print("Tidak ada kuda yang tersedia untuk dihapus.")

# Fungsi untuk menyewa kuda
def sewa_kuda():
    if list_kuda:
        print("===== Sewa Kuda =====")
        id_kuda = input("Masukkan ID kuda yang ingin disewa: ")
        for kuda in list_kuda:
            if kuda["id_kuda"] == id_kuda and kuda["tersedia"]:
                tujuan = input("Masukkan tujuan penyewaan (misal: fotografi, pekerjaan, transportasi): ")
                kuda["tersedia"] = False
                waktu_sewa = float(input("masukan waktu sewa (jam) = "))
                total_harga = waktu_sewa * kuda["harga"]
                riwayat_transaksi.append({
                    "ID Kuda": id_kuda,
                    "Nama Kuda": kuda["nama_kuda"],
                    "Jenis Transaksi": "Sewa",
                    "Waktu Transaksi": waktu_sewa,
                    "Tujuan": tujuan
                })
                print(f"Kuda {kuda['nama_kuda']} berhasil disewa untuk tujuan {tujuan} degan harga Rp {total_harga}.")
                return
        print("Kuda tidak tersedia atau ID salah.")
    else:
        print("Tidak ada kuda yang tersedia untuk disewa.")

# Fungsi untuk mengembalikan kuda
def kembalikan_kuda():
    if list_kuda:
        id_kuda = input("\nMasukkan ID kuda yang ingin dikembalikan: ")
        for kuda in list_kuda:
            if kuda["id_kuda"] == id_kuda and not kuda["tersedia"]:
                kuda["tersedia"] = True
                waktu_kembali = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                riwayat_transaksi.append({
                    "ID Kuda": id_kuda,
                    "Nama Kuda": kuda["nama_kuda"],
                    "Jenis Transaksi": "Kembali",
                    "Waktu Transaksi": waktu_kembali,
                    "Tujuan": "Pengembalian"
                })
                print(f"Kuda {kuda['nama_kuda']} berhasil dikembalikan.")
                return
        print("Kuda tidak ditemukan atau sudah tersedia.")
    else:
        print("Kuda yang anda ingin kembalikan tidak terdata.")

# Fungsi login
def login():
    users = {
        "admin": {"username": "admin", "password": "admin123", "role": "admin"},
        "user1": {"username": "user1", "password": "user123", "role": "user"},
    }

    print("=== Sistem Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil! Selamat datang, {username}.")
        return users[username]["role"]  # Mengembalikan peran pengguna (admin atau user)
    else:
        print("Login gagal! Username atau password salah.")
        return None

# Menu admin
def admin_menu():
    print("===== Menu Admin =====")
    print("1. Tambah Kuda")
    print("2. Hapus Kuda")
    print("3. Tampilkan Riwayat Transaksi")
    print("4. Lihat Daftar Kuda")
    print("5. Keluar")

# Menu user
def user_menu():
    print("===== Menu User =====")
    print("1. Sewa Kuda")
    print("2. Kembalikan Kuda")
    print("3. Lihat Daftar Kuda")
    print("4. Keluar")

# Fungsi utama
def main():  
    role = login()
    if role == "admin":
        while True:
            admin_menu()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                tambah_kuda()  
            elif pilihan == "2":
                hapus_kuda()  
            elif pilihan == "3":
                tampilkan_riwayat_transaksi()
            elif pilihan == "4":
                tampilkan_kuda()  
            elif pilihan == "5":
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak valid.")
    elif role== "user":
        while True:
            user_menu()
            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                sewa_kuda()
            elif pilihan == "2":
                kembalikan_kuda()
            elif pilihan == "3":
                tampilkan_kuda()
            elif pilihan == "4":
                print("Keluar dari menu user.")
                break
            else:
                print("Pilihan tidak valid.")
    else:
        print("Login gagal. Aplikasi ditutup.")

# Jalankan program utama
main()
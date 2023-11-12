def hitung_total(harga, jumlah):
    return harga * jumlah

def tampilkan_struk(daftar_belanja, total_pembelian):
    print("\n===== Struk Belanja =====")
    for item in daftar_belanja:
        print(f"{item['barang']} - {item['harga']} x {item['jumlah']} = {item['total']}")
    print("=========================")
    print(f"Total Pembelian: {total_pembelian}")

def main():
    print("===== PROGRAM KASIR SEDERHANA =====")

    daftar_belanja = []
    total_pembelian = 0

    while True:
        barang = input("Masukkan nama barang : ")
        if barang.lower() == 'selesai':
            break

        harga = float(input("Masukkan harga per barang: "))
        jumlah = int(input("Masukkan jumlah barang yang dibeli: "))

        total_barang = hitung_total(harga, jumlah)
        total_pembelian += total_barang

        item = {
            'barang': barang,
            'harga': harga,
            'jumlah': jumlah,
            'total': total_barang
        }

        daftar_belanja.append(item)

        opsi = input("Tambah barang lagi? (ya/tidak): ")
        if opsi.lower() != 'ya':
            break

    tampilkan_struk(daftar_belanja, total_pembelian)

if __name__ == "__main__":
    main()

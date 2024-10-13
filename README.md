# Mini-Project-2
**NAMA    : Christian Amsal Asimaro Lumban Tobing**

**KELAS   : SISTEM INFORMASI B24**

**NIM     : 2409116053**

**TUGAS   : MINI PROJECT 2 DDP**

**FLOWCHART**

![MinPro 2 drawio](https://github.com/user-attachments/assets/d6881f06-279a-4e18-b7f3-c04fe20cdc95)

**PENJELASAN**

    from prettytable import PrettyTable

    Datalist = []
    listdatajokiers = []

("from prettytable import PrettyTable" untuk membuat table)

("Datalist = []" & "listdatajokiers = []" untuk menyediakan list kosong)

    def tambahlist():
        table = PrettyTable()
    
        #LIST HARGA
        #"Warrior", "5000/bintang"  
        #"Elite", "7000/bintang"
        #"Master", "10000/bintang"
        #"Grandmaster", "15000/bintang"
        #"Epic", "20000/bintang"
        #"Legend", "5000/bintang"
        #"Mythic", "30000/bintang"
        #"Mythic Honor", "50000/bintang"
        #"Mythic Glory", "75000/bintang"
        "Mythic Immortal", "100000/bintang"

  (untuk catatan harga aja)
    
    table.field_names = ["NO", "Rank", "Harga"]
    listno = input("Masukkan list ke berapa :")
    listrank = input("Masukkan Rank :")
    listharga = input("Masukkan Harga :")
    Datalist.append({"NO": listno, "Rank": listrank, "Harga": listharga})
    print("Data List berhasil ditambahkan")
    PrettyTable()

(Untuk "Menambahkan" data pada list) (CREATE)

    def tampilkandatalist():
        table = PrettyTable()
        table.field_names = ["NO", "Rank", "Harga"]
    
    
        for list in Datalist :
            table.add_row([list["NO"], list["Rank"], list["Harga"]])
            print(table)

(Untuk "Menampilkan" data pada list) (READ)

    def updatedatalist():
        listrank = input("Masukkan List Rank yang ingin di update :")
        for list in Datalist :
            if list["Rank"] == listrank :
                updharga = input("Masukkan Harga Terbaru :")
                list["Harga"] = updharga
                print("Data berhasil di Update")
                return
        print("Data tidak ditemukan")

(Untuk "Mengupdate" atau mengubah data pada list) (UPDATE)

    def hapusdata() :
        listrank = input("Masukkan List Rank yang ingin di hapus :")
        for list in Datalist :
            if list["Rank"] == listrank :
                Datalist.remove(list)
                print("List telah di hapus")
                return
        print("Data tidak ditemukan")

(Untuk "menghapus" data pada list) (DELETE)

    def datajokiers() :
        listrank = input("Masukkan Rank saat ini :")
        for list in Datalist :
            if list["Rank"] == listrank :
                namajokiers = input("Masukkan Nama :")
                harga = list["Harga"]
                idjokiers = len(listdatajokiers) + 1
                listdatajokiers.append({"ID Jokiers": idjokiers, "Nama Jokiers": namajokiers, "Rank Jokiers": listrank, "Harga": harga})
                print(f"Anda Telah Memesan Jasa Dreadersjoki.ID : \n{list["Rank"]} dengan harga {harga}")
                print("Terimakasih Telah menggunakan Jasa dari Dreadersjoki.ID")
                return
        print("Data tidak ditemukan")

(Untuk "Membuat" data Jokiers atau pelanggan)

    def tampilandatajokiers() :
        table = PrettyTable()
        table.field_names = ["Nama Jokiers", "Rank Jokiers", "Rank Tujuan Jokiers", "Harga"]
        for listjokiers in listdatajokiers :
            table.add_row([listjokiers["Nama Jokiers"], listjokiers["Rank Jokiers"], listjokiers["Rank Tujuan"], listjokiers["Harga"]])
        print(table)

(Untuk "Menampilkan" Data Jokiers atau Pelanggan) (READ)

    def main () :
        while True :
            table = PrettyTable()
    
            table.field_names = ["Opsi", "Selamat datang di Dreadersjoki.ID", "DREADERSJOKI.ID"]
    
            table.add_row(["1", "Admin", "DREADERSJOKI.ID"])
            table.add_row(["2", "Jokiers", "DREADERSJOKI.ID"])
            table.add_row(["3", "EXIT", "DREADERSJOKI.ID"])
    
            print(table)
            opsi = input("Masukkan Opsi yang dipilih :")

(Menggunakan while True untuk melakukan pengulangan)

(Memasukkan Table lagi untuk menampilkan opsi)

(Memasukkan Opsi mana yang ingin di pilih)

        if opsi == "1" :
            admtable = PrettyTable()

            admtable.field_names = ["Opsi", "Selamat datang Admin Dreadersjoki.ID", "DREADERSJOKI.ID"]

            admtable.add_row(["1", "Tambah List", "DREADERSJOKI.ID"])
            admtable.add_row(["2", "Tampilkan List", "DREADERSJOKI.ID"])
            admtable.add_row(["3", "Update List", "DREADERSJOKI.ID"])
            admtable.add_row(["4", "Hapus List", "DREADERSJOKI.ID"])
            admtable.add_row(["5", "Tampilkan List Jokiers", "DREADERSJOKI.ID"])
            admtable.add_row(["6", "EXIT", "DREADERSJOKI.ID"])

            print(admtable)
            opsi = input("Masukkan Opsi pilihan :")

(jika opsi 1 terpilih maka akan terbuka lagi table opsi untuk admin)

(Memasukkan opsi yang ingin di pilih pada table opsi admin)

            if opsi == "1" :
                tambahlist()
            elif opsi == "2" :
                tampilkandatalist()
            elif opsi == "3" :
                updatedatalist()
            elif opsi == "4" :
                hapusdata()
            elif opsi == "5" :
                tampilandatajokiers()
            elif opsi == "6" :
                print("Terima Kasih telah berjasa di Dreadersjoki.ID")
                break
            else :
                print("ERROR!! Silahkan Coba lagi.")

(Jika memilih opsi 1, maka akan menampilkan tampilan untuk menambahkan list (CREATE))

(Jika memilih opsi 2, maka akan menampilkan tampilan list data yang sudah di buat (READ))

(Jika memilih opsi 3, maka akan menampilkan tampilan untuk mengubah list (UPDATE))

(Jika memilih opsi 4, maka akan menampilkan tampilan untuk menghapus list (DELETE))

(Jika memilih opsi 5, maka akan menampilkan data para jokiers atau pelanggan (READ))

(Jika memilih opsi 6, maka akan keluar dari sistem)

(Jika tidak memilih opsi yang ada, maka akan eror dan kembali ke tampilan memilih opsi)

        elif opsi == "2" :
            tampilkandatalist()

            joktable = PrettyTable()

            joktable.field_names = ["Opsi", "Selamat datang Jokiers Dreadersjoki.ID", "DREADERSJOKI.ID"]

            joktable.add_row(["1", "Buat Pesanan", "DREADERSJOKI.ID"])
            joktable.add_row(["2", "EXIT", "DREADERSJOKI.ID"])
            
            print(joktable)
            opsi = input("Masukkan Opsi pilihan :")

            if opsi == "1" :
                datajokiers()
            elif opsi == "2" :
                print("Terima Kasih telah menggunakan Dreadersjoki.ID \nSilahkan datang kembali Jokiers")
                break
            else :
                print("ERROR!! Silahkan Coba lagi.")
        
        elif opsi == "3" :
            print("Terima Kasih, silahkan datang kembali")
            break

(ini jika saat memilih opsi 2 saat tampilan opsi masuk sebagai apa, maka akan muncul tampilan Jokiers atau pelanggan)

(jika memilih opsi 3, maka akan keluar dari sistem)

if __name__ == "__main__":
    main()

(Untuk memanggil fungtion "Main()"

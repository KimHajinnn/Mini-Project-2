from prettytable import PrettyTable

Datalist = []
listdatajokiers = []

def tambahlist():
    table = PrettyTable()

    table.field_names = ["NO", "Rank", "Harga"]
    listno = input("Masukkan list ke berapa :")
    listrank = input("Masukkan Rank :")
    listharga = input("Masukkan Harga :")
    Datalist.append({"NO": listno, "Rank": listrank, "Harga": listharga})
    print("Data List berhasil ditambahkan")
    PrettyTable()

def tampilkandatalist():
    table = PrettyTable()
    table.field_names = ["NO", "Rank", "Harga"]

    #table.add_row(["1", "Warrior", "5000/bintang"])
    #table.add_row(["2", "Elite", "7000/bintang"])
    #table.add_row(["3", "Master", "10000/bintang"])
    #table.add_row(["4", "Grandmaster", "15000/bintang"])
    #table.add_row(["5", "Epic", "20000/bintang"])
    #table.add_row(["6", "Legend", "5000/bintang"])
    #table.add_row(["7", "Mythic", "30000/bintang"])
    #table.add_row(["8", "Mythic Honor", "50000/bintang"])
    #table.add_row(["9", "Mythic Glory", "75000/bintang"])
    #table.add_row(["10", "Mythic Immortal", "100000/bintang"])

    for list in Datalist :
        table.add_row([list["NO"], list["Rank"], list["Harga"]])
        print(table)

def updatedatalist():
    listrank = input("Masukkan List Rank yang ingin di update :")
    for list in Datalist :
        if list["Rank"] == listrank :
            updharga = input("Masukkan Harga Terbaru :")
            list["Harga"] = updharga
            print("Data berhasil di Update")
            return
    print("Data tidak ditemukan")

def hapusdata() :
    listrank = input("Masukkan List Rank yang ingin di hapus :")
    for list in Datalist :
        if list["Rank"] == listrank :
            Datalist.remove(list)
            print("List telah di hapus")
            return
    print("Data tidak ditemukan")

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

def tampilandatajokiers() :
    table = PrettyTable()
    table.field_names = ["Nama Jokiers", "Rank Jokiers", "Rank Tujuan Jokiers", "Harga"]
    for listjokiers in listdatajokiers :
        table.add_row([listjokiers["Nama Jokiers"], listjokiers["Rank Jokiers"], listjokiers["Rank Tujuan"], listjokiers["Harga"]])
    print(table)

def main () :
    while True :
        table = PrettyTable()

        table.field_names = ["Opsi", "Selamat datang di Dreadersjoki.ID", "DREADERSJOKI.ID"]

        table.add_row(["1", "Admin", "DREADERSJOKI.ID"])
        table.add_row(["2", "Jokiers", "DREADERSJOKI.ID"])
        table.add_row(["3", "EXIT", "DREADERSJOKI.ID"])

        print(table)
        opsi = input("Masukkan Opsi yang dipilih :")
        
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

if __name__ == "__main__":
    main()
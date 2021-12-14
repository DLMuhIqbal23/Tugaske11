data = []
print("==== Tambah ====")
def tambah():
        data.append({
            'Nama' : input("Nama: "),
            'Nim' : int(input("NIM: ")),
            'Tugas' : int(input("Nilai Tugas: ")),
            'Uts' : int(input("Nilai UTS: ")),
            'Uas' : int(input("Nilai UAS: "))      
        })

tambah()
tambah()

print("==== Tampilkan ====")
def tampilkan():
    for item in data:
        print("Nama: ",item['Nama'])
        print("NIM: ",item['Nim'])
        print("Nilai Tugas",item['Tugas'])
        print("Nilai UTS: ",item['Uts'])
        print("Nilai UAS: ",item['Uas'])
tampilkan()

print("==== Hapus ====")
def hapus(nama):
    h = nama
    if h == "Ray":
        del data[0]
        print("data telah terhapus")
    elif h == "Dan":
        del data[1]
        print("data telah terhapus")

nama = input("Masukkan Nama yang ingin dihapus: ")
hapus(nama)
tampilkan()

print("==== Ubah ====")
def ubah(nama):
        for item in data:
            c = nama
            if c == item['Nama']:
                item['Nim'] = int(input("Ubah Nim: "))
                item['Tugas'] = int(input("Ubah Nilai Tugas: "))
                item['Uts'] = int(input("Ubah Nilai UTS: "))
                item['Uas'] = int(input("Ubah Nilai UAS: "))

nama = input("Masukkan Nama Yang ingin diubah: ")
ubah(nama)
tampilkan()
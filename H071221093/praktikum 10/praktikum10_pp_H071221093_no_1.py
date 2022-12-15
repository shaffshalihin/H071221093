import re
# from prettytable import PrettyTable
data = []
while True:
    print("""\nPILIHAN LAYANAN
1. Detail Anda
2. Ubah Nama
3. Jumlah Data Pada File
4. Save Data pada File
5. Buat Data Baru
6. Keluar """)
    _inputan = int(input(30*"="+"\nPilihan : "))
    if _inputan == 1: # Menampilkan Data Diri yang ada dalam list data
        if len(data) > 0: 
            print(30*"=")
            for i in range(len(data)):
                for y in range(len(data[0])):
                    print(f'{data[i][y]}')
        else:
            print(30*"="+"\nData saat ini kosong!\n"+30*"=")
    elif _inputan == 2: # Mengubah nama dalam list data
        if len(data) != 0:
            print(30*"=")
            for i in range(len(data)):
                print(f'Urutan {i+1} {data[i][0]}') 
            _newName = list(map(str, input("Masukkan Index dan nama baru (Urutan NamaBaru) : ").split()))
            data[int(_newName[0])-1][0] = "Nama : "+_newName[1]
        elif len(data) == 0:
            print(30*"="+"\nData Tidak Ditemukan!\n"+30*"=")
    elif _inputan == 3: # Menampilkan jumlah data pada file <namaFile>.txt
        _file = input("Masukkan fIle : ")+".txt"
        try:
            with open(_file) as baca:
                dataFILE = re.findall(r"@student.unhas.ac.id", baca.read())
            print(f"Jumlah Data adalah {dataFILE.count('@student.unhas.ac.id')}")
        except FileNotFoundError:
            print(30*"="+f"\nTidak Terdapat File Dengan Nama {_file}")
            print("Jumlah data pada file = 0\n"+30*"=")
    elif _inputan == 4: # Menulis data pada list ke File <namaFile>.txt
        if len(data) == 0: 
            print(30*"="+"\nData Sata Ini Kosong!\n"+30*"=")
        else:
            _FILE = input("Nama File : ")+".txt"
            with open(_FILE, "a") as tulis:
                tulis.write("\n")
                for i in range(len(data)):
                    for y in range(len(data[i])):
                        tulis.write(data[i][y]+"\n")
                    tulis.write(30*"=")
                data = []
    elif _inputan == 5: # Memasukkan data baru kedalam list data
        nama = input(30*"="+"\nNama : "); print(30*"=")
        while True:
            Email = input("Email : ")
            if re.search(r"^[a-z0-9]{1,}@student[.]unhas[.]ac[.]id$", Email):
                break
            else:
                print(30*"="+"\nEmail Yang Anda Masukkan salah\n"+30*"=")
        while True:
            _Pass = input(30*"="+"\nMasukkan Password : "); print(30*"=")
            if len(_Pass) >= 8 and len(_Pass) <= 20:
                if re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$', _Pass):
                    break
                else:
                    print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
            else: 
                print("Password Harus Memiliki 8-20 Karakter")
        data.insert(len(data), ["Nama : " + nama,"E-mail : "+ Email, "Password : "+ _Pass]); print("Berhasil")
    elif _inputan == 6: # Keluar dari program/menyelesaikan while
        print(30*"="+"\nSampai Jumpa Lagi\n"+30*"=")
        break

print(data)
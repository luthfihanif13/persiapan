#Program Ojekonline syariah
import time
import sys


lokasi = {
	'penjemputan': ['SENTOSA', 'GAJAH MADA', 'PRAMUKA', 'PERJUANGAN', 'BENGKURING', 'PALARAN', 'JUANDA', 'CENDANA', 'ALAYA', 'LEMPAKE', 'REMAJA', 'PAHLAWAN', 'MAKROMAN', 'KEBAKTIAN', 'AWANG LONG', 'PEMUDA'],
	'tujuan': ['SENTOSA', 'GAJAH MADA', 'PRAMUKA', 'PERJUANGAN', 'BENGKURING', 'PALARAN', 'JUANDA', 'CENDANA', 'ALAYA', 'LEMPAKE', 'REMAJA', 'PAHLAWAN', 'MAKROMAN', 'KEBAKTIAN', 'AWANG LONG', 'PEMUDA']
}

daftar_driver = {
	'ikhwan': ['adam', 'budi', 'tri', 'rahman', 'shafera']
}

daftar_akhwat = {
	'akhwat': ['puput', 'bila', 'amel', 'rara', 'eka']
}

harga_km = 0

def list_jalanan_penjemputan():
    penjemputan
    for key, value in penjemputan.items():
     print(key, value)


def tambah():
    tambahjalan = input('Tambah nama jalan: ')
    penjemputan['lokasi'].append(tambahjalan)
    

def update():
    updatejalan = input('update nama jalan: ')
    if updatejalan in penjemputan['lokasi']:
      index = penjemputan['lokasi'].index(updatejalan)
      penjemputan['lokasi'][index] = input("masukkan nama jalan :")
      print(" Jalan "+str(updatejalan)+"Berhasil Update ")
    else:# No user prompt was found 
      print(" Gagal Update !")

def hapus():
    hapusjalan = input('hapus nama jalan: ')
    if hapusjalan in penjemputan['lokasi']:
      index = penjemputan['lokasi'].index(hapusjalan)
      penjemputan['lokasi'].pop(index)
      print("Jalan "+str(hapusjalan)+" Berhasil Dihapus ")
    else:# No user prompt was found 
      print("Gagal Hapus !")

def list_jalanan_tujuan():
    tujuan
    for key, value in tujuan.items():
      print(key, value)

def tambah_tujuan():
    tambahtujuan= input('masukan nama tujuan: ')
    tujuan['lokasi'].append(tambahtujuan)

def update_tujuan():
    updatetujuan = input('update nama tujuan: ')
    if updatetujuan in tujuan['lokasi']:
      index = tujuan['lokasi'].index(updatetujuan)
      tujuan['lokasi'][index] = input(" masukkan nama tujuan :")
      print(" tujuan "+str(updatetujuan)+"Berhasil Update ")
    else:# No user prompt was found 
      print(" Gagal Update !")

def hapus_tujuan():
    hapustujuan = input('hapus lokasi tujuan: ')
    if hapustujuan in penjemputan['lokasi']:
      index = penjemputan['lokasi'].index(hapustujuan)
      tujuan['lokasi'].pop(index)
      print("tujuan "+str(hapustujuan)+" Berhasil Dihapus ")
    else:# No user prompt was found 
      print("Gagal Hapus !")

def menuju():
    for i in range (15):
        sys.stdout.write('\rSedang menuju Lokasi penjemputan |')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan /')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan -')
        time.sleep(0.1)
        sys.stdout.write('\rSedang menuju Lokasi penjemputan \\')
        time.sleep(0.1)
    sys.stdout.write('\ndriver telah sampai                        \n')
    for i in range (20):
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan |')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan /')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan -')
        time.sleep(0.1)
        sys.stdout.write('\rdriver mengantar ke lokasi tujuan \\')
        time.sleep(0.1)
    sys.stdout.write('\ndriver telah mengantar sampai di lokasi tujuan  \n')
    print('silahkan melakukan Pembayaran')



def login():
  print('login Ojek Online Syariah')
  while True:
    username = input('username : ')
    passw = input('password : ')
    
    if username == 'Luthfi' and passw == '082': 
       status = 1 
    elif username == 'Adit' and passw == '110' or username == 'puput' and passw == '074' :
    	status = 0

        print('---------------------------------')
        print('-------Ojek Online Syariah-------')
        print('--Membantu Antum dalam Berpergian--')
        print('------Aman,Nyaman,Terpercaya------')
        print('---------------------------------')
        break
    else:
        print('silahkan antum memasukkan password/username dengan benar!')
        continue

def menu():
  while True:
    print('Menu')
    print('1. OjekS')
    print('0. Keluar')
    inmenu = input('masukkan pilihan : ')
    if inmenu == '1' :
      break
    elif inmenu == '0' :
      print('Antum telah logout')
      print('Jazakallah khair telah menggunakan program kami')
      exit()
    else:
      continue
  
  while True:
    print('Kendaraan')
    print('1. Motor\n2. Mobil')
    kendaraan = input('masukan pilihan: ')
    if kendaraan == '1':
        harga_km = 500
        print('\nAntum memilih motor')
        break
    elif kendaraan == '2':
        harga_km = 750
        print('\nAntum memilih mobil')
        break
    else :
      continue


  while True:
    print('Lokasi Penjemputan')
    list_jalanan_penjemputan()
    print('==============')
    print('1. Masukkan Lokasi Penjemputan')
    print('2. Menambahkan lokasi penjemputan')
    print('3. Mengupdate lokasi penjemputan')
    print('4. Menghapus lokasi penjemputan')
    inputjemput = input('masukan pilihan: ')
    if inputjemput == '1':
      break
    elif inputjemput == '2':
      tambah()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputjemput == '3':
      update()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputjemput == '4':
      hapus()
      print("\n")
      input("Tekan Enter untuk kembali...")
    else:
      continue

  while True:
    jemput = input('Masukkan Lokasi Penjemputan: ')
    jemput = jemput.upper()
    if jemput in penjemputan['lokasi']:
      break
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  while True:
    print('Lokasi Tujuan')
    list_jalanan_tujuan()
    print('==============')
    print('1. Masukkan Lokasi Tujuan')
    print('2. Menambahkan lokasi Tujuan')
    print('3. Mengupdate lokasi Tujuan')
    print('4. Menghapus lokasi Tujuan')
    inputtujuan = input('masukan pilihan: ')
    if inputtujuan == '1':
      break
    elif inputtujuan == '2':
      tambah_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputtujuan == '3':
      update_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    elif inputtujuan == '4':
      hapus_tujuan()
      print("\n")
      input("Tekan Enter untuk kembali...")
    else:
      continue

  while True:
    intujuan = input('Masukkan Lokasi Tujuan: ')
    intujuan = intujuan.upper()
    if intujuan in tujuan['lokasi']:
    	jarak = (len(jemput)) * (len(intujuan))
    	break
    else:# No user prompt was found 
      print("Tidak ada lokasi")
      continue

  while True:
    print('Driver')
    print('1. Ikhwan\n2. Akhwat')
    driver = input('masukan pilihan: ')
    if driver == '1':
      urutan= jarak % len(daftar_ikhwan['ikhwan'])
      print('\nNama driver antum : '+str( daftar_ikhwan['ikhwan'][urutan]))
      break
    elif driver == '2':
      urutan= jarak % len(daftar_akhwat['akhwat'])  
      print('\nNama driver antum : '+str( daftar_akhwat['akhwat'][urutan]))
      break
    else:
      continue

  total = jarak * harga_km
  print("Titik Penjemputan : "+str(jemput))
  print("Titik Tujuan : "+str((intujuan)))
  print('Total Pembayaran '+str(total))
  menuju()

  while True:
   try:
   	Bayar=int(input("Jumlah Nominal Uang = Rp. ", ))
   except ValueError:
   	print ("Silahkan Antum Periksa lagi Inputan")
   	continue
   else :
   	if total <= Bayar:
   		Kembalian= (Bayar-total)
   		print("Uang Kembalian = ", "Rp.",Kembalian)
   		break
   	else:
   		print("Uang Anda Kurang")
   		continue
  

 

while True:
 login()
 menu()
 pilihan=input('Apakah antum mau memesan ojek online syariah lagi ? y/t = ')
 if pilihan=='t':
 	print('Terima kasih telah menggunakan program kami')
 	break
 elif pilihan=='y':
 	continue
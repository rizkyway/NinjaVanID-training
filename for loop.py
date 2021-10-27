# nama_buah = ('apel', 'jeruk', 'mangga')
# print(nama_buah[0])

# print(nama_buah)

# for buah in nama_buah:
#     print(buah)
#     print("---")

count = int(input("Berapa Data: "))

nama_pelanggan = []
umur_pelanggan = []

for i in range(count) :
    print("Data ke {}").format (i+1)
    nama = input("Nama : ")
    umur = int(input("Umur : "))

    nama_pelanggan.append(nama)
    umur_pelanggan.append(umur)

for i in range(len(nama_pelanggan)):
 print('Pelanggan {} berusia {}'.format(nama_pelanggan[i], umur_pelanggan[i]))
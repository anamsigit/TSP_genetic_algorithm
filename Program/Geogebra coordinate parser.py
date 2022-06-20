'''Mengambil koordinat kartesius dari geogebra, dengan download as Asymtote.txt
tidak boleh menyertakan label, harus sederhana mungkin

contoh mentahan yang siap diolah
((0.4625,6.94125),dotstyle); 
((0.4425,7.34125),dotstyle); 
((0.3825,8.02125),dotstyle)   (pada koordinat terakhir tidak boleh ada tanda titik koma)
'''


lokasi_file_mentahan = 'C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point.txt'

file1 = open(lokasi_file_mentahan, "r")
ambil1 = file1.read()
file1.close()

file2 = open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'w')
file2.write(ambil1)
file2.close()

file3 = open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'r')
listdata = file3.read()
ekstrakdua = listdata.split('),dotstyle)')
file3.close()

with open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'w') as f:
    for item in ekstrakdua:
        f.write("%s\n" % item)
f.close

file4 = open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'r')
listdata = file4.read()
ekstraktiga = listdata.split('((')
file4.close()

with open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'w') as f:
    for item in ekstraktiga:
        f.write("%s\n" % item)
f.close

file5 = open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_ekstrak.txt', 'r')
listdata = file5.read()
string = listdata.replace('\n',"")
ekstraktiga = string.split(';')
file5.close()

koordinatx = []
koordinaty = []

for i in range(len(ekstraktiga)) :
    koordinat = ekstraktiga[i]
    for j in range(1) :
        spesifik = koordinat.split(',')
        print(spesifik)
        koordinatx.append(spesifik[0])
        koordinaty.append(spesifik[1])


print (f'untuk X: {koordinatx}')
print (f'untuk Y: {koordinaty}')

with open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_X.txt', 'w') as f:
    for item in koordinatx:
        f.write("%s\n" % item)
f.close

with open('C:\\Users\\admin\\Downloads\\Distribusi_energi\\data_point_Y.txt', 'w') as f:
    for item in koordinaty:
        f.write("%s\n" % item)
f.close
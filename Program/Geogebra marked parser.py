'''Mengambil marked/label pada scatter
'''
lokasi_file_mentahan = 'C:\\Users\\admin\\Downloads\\point mark.txt'
lokasi_file_hasil = 'C:\\Users\\admin\\Downloads\\Distribusi_energi\\Result geogebra parser\\point labelling parser.txt'
lokasi_file_hasil_fix = 'C:\\Users\\admin\\Downloads\\Distribusi_energi\\Result geogebra parser\\point labelling parser fix.txt'

file2 = open(lokasi_file_hasil_fix, 'w')
file2.write('')
file2.close()

file1 = open(lokasi_file_mentahan, "r")
ambil1 = file1.read()
file1.close()

file2 = open(lokasi_file_hasil, 'w')
file2.write(ambil1)
file2.close()

file3 = open(lokasi_file_hasil, 'r')
listdata = file3.read()
ekstrakdua = listdata.split('("$')
file3.close()

n = len(ekstrakdua)

for z in range(2,n,1): #anda harus jalankan dulu secara terpisah untuk mengetahui nilai sebenarnya dari 88 dnegan print(len(ekstrakdua))

    file2 = open(lokasi_file_hasil_fix, 'a')
    file2.write('"')
    file2.close()

    with open(lokasi_file_hasil, 'w') as f:
        # for i in range (0, n, 2):
        for item in ekstrakdua[z]:
            f.write(item)
    f.close

    file4 = open(lokasi_file_hasil, 'r')
    listdata = file4.read()
    ekstraktiga = listdata.split('$",')
    file4.close()

    m = len(ekstraktiga)

    with open(lokasi_file_hasil_fix, 'a') as g:
        # for h in range (0, m, 2):
        for item in ekstraktiga[0]:
            g.write(item)
    f.close

    file2 = open(lokasi_file_hasil_fix, 'a')
    file2.write('",')
    file2.close()


# membaca text file, menghapus karakter yang tidak diinginkan lalu menyimpan data tersebut dalam sebuah matriks
def get_data(nama_file):
    text = open(nama_file,'r')     #membuka file dan merekamnya dalam variabel arsip
    lines = text.readlines()

    arr_data = []

    for line in lines :
        # menghapus karakter yang tidak diinginkan untuk disimpan
        line = line.replace('.','')
        line = line.replace(' ', '')
        line = line.replace('\n', '')

        # menyimpan data baris yang dibaca ke dalam sebuah array lalu memasukkannya ke array arr_data
        datas = line.split(",")
        arr_data.append(datas)
    
    return arr_data
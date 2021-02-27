def clean_text(nama_file):
    text = open(nama_file,'r')     #membuka file dan merekamnya dalam variabel arsip
    lines = text.readlines()

    arr_data = []

    for line in lines :
        line = line.replace('.','')
        line = line.replace(' ', '')
        line = line.replace('\n', '')
        datas = line.split(",")
        arr_data.append(datas)
    
    return arr_data
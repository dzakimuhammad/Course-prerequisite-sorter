# NAMA : DZAKI MUHAMMAD
# NIM : 13519049
# KELAS : K-1
# DESKRIPSI : TUGAS KECIL 2 STRATEGI ALGORITMA

# PENYUSUNAN RENCANA KULIAH DENGAN TOPOLOGICAL SORT

from textcleaning_13519049 import get_data
from graphmaking_13519049 import makegraph, listderajat
from dc_and_cq_13519049 import process

#tampilan awal program
print("  _______ ____  _____   ____ _______ ____  _____   ____     _____ ____  _    _ _____   _____ ______  _____ ")
print(" |__   __/ __ \|  __ \ / __ \__   __/ __ \|  __ \ / __ \   / ____/ __ \| |  | |  __ \ / ____|  ____|/ ____|")
print("    | | | |  | | |__) | |  | | | | | |  | | |__) | |  | | | |   | |  | | |  | | |__) | (___ | |__  | (___  ")
print("    | | | |  | |  ___/| |  | | | | | |  | |  ___/| |  | | | |   | |  | | |  | |  _  / \___ \|  __|  \___ \ ")
print("    | | | |__| | |    | |__| | | | | |__| | |    | |__| | | |___| |__| | |__| | | \ \ ____) | |____ ____) |")
print("    |_|  \____/|_|     \____/  |_|  \____/|_|     \____/   \_____\____/ \____/|_|  \_\_____/|______|_____/ ")
                                                                                                           
print()
print("TopoTopo Courses akan menyusun rencana mata kuliah yang dapat Anda ambil!")
print()

#input nama file
nama_file = input("Masukkan nama file yang akan dibaca : ")     
print()

#mengubah text file input ke dalam bentuk matriks
clean_data = get_data(nama_file) 

#dictionary yang merepresentasikan DAG 
graf = makegraph(clean_data) 

#dictionary yang merepresentasikan derajat tiap node pada DAG
derajat = listderajat(clean_data) 

#inisialisasi array rencana kuliah
rencana_kuliah = []

# jalankan topological sort (pendekatan decrease and conquer) selama node graf
# belum dihilangkan semua
while (len(graf)>0) :
    process(graf, derajat, rencana_kuliah)

# mencetak luaran
print("Rencana Kuliah :")
for i in range (len(rencana_kuliah)) :
    print("Semester " + str(i+1) + ":", end = " ")
    
    for j in  range(len(rencana_kuliah[i])) :
        if j == len(rencana_kuliah[i])-1 :
            print(rencana_kuliah[i][j], end = "")
            if i == len(rencana_kuliah)-1 :
                print(".")
            else:
                print()
        
        else :
            print(rencana_kuliah[i][j], end =", ")
    
    
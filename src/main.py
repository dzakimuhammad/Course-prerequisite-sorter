# NAMA : DZAKI MUHAMMAD
# NIM : 13519049
# KELAS : K-1
# DESKRIPSI : TUGAS KECIL 2 STRATEGI ALGORITMA

# PENYUSUNAN RENCANA KULIAH DENGAN TOPOLOGICAL SORT

import textcleaning
import graphmaking
import dc_and_cq

#input nama file
nama_file = input("Masukkan nama file yang akan dibaca : ")     
print()

#mengubah text file input ke dalam bentuk matriks
clean_data = textcleaning.get_data(nama_file) 

#dictionary yang merepresentasikan DAG 
graf = graphmaking.makegraph(clean_data) 

#dictionary yang merepresentasikan derajat tiap node pada DAG
derajat = graphmaking.listderajat(clean_data) 

#inisialisasi array rencana kuliah
rencana_kuliah = []

# jalankan topological sort (pendekatan decrease and conquer) selama node belum diassign ke dalam array rencana kuliah
while (len(graf)>0) :
    dc_and_cq.process(graf, derajat, rencana_kuliah)

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
    
    
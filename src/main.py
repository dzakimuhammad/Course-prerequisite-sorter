# NAMA : DZAKI MUHAMMAD
# NIM : 13519049
# KELAS : K-1
# DESKRIPSI : TUGAS KECIL 2 STRATEGI ALGORITMA

# PENYUSUNAN RENCANA KULIAH DENGAN TOPOLOGICAL SORT

import textcleaning
import graphmaking
import dc_and_cq

nama_file = input("Masukkan nama file yang akan dibaca : ")     #input nama file
print()
clean_data = textcleaning.clean_text(nama_file) #dapetin matriks dari text file

graf = graphmaking.makegraph(clean_data) #bikin dictionary buat DAG 
derajat = graphmaking.listderajat(clean_data) #bikin dictionary buat derajat

rencana_kuliah = []
semester = ["Semester 1", ]

while (len(graf)>0) :
    dc_and_cq.process(graf, derajat, rencana_kuliah)


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
    
    
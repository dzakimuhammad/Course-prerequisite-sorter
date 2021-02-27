# NAMA : DZAKI MUHAMMAD
# NIM : 13519049
# KELAS : K-1
# DESKRIPSI : TUGAS KECIL 2 STRATEGI ALGORITMA

# PENYUSUNAN RENCANA KULIAH DENGAN TOPOLOGICAL SORT

import textcleaning
import graphmaking

nama_file = input("Masukkan nama file yang akan dibaca : ")     #input nama file
clean_data = textcleaning.clean_text(nama_file) #dapetin matriks dari text file

graf = graphmaking.makegraph(clean_data) #bikin dictionary buat DAG 
derajat = graphmaking.listderajat(clean_data) #bikin dictionary buat derajat

rencana_kuliah = []
semester = ["Semester 1", ]

def dnc(graf, derajat, rencana_kuliah) :
    matkul_sem = []
    for matkul in derajat : 
        if derajat[matkul] == 0 :
            matkul_sem.append(matkul)
    rencana_kuliah.append(matkul_sem)
    
    for matkul_taken in matkul_sem:
        for matkul in graf :
            for succ in graf[matkul] :
                if succ == matkul_taken :
                    graf[matkul].remove(matkul_taken)
        
        graf.pop(matkul_taken)
        derajat.pop(matkul_taken)
    graphmaking.updatederajat(graf, derajat)


while (len(graf)>0) :
    dnc(graf, derajat, rencana_kuliah)


print("Rencana Kuliah :")
for i in range (len(rencana_kuliah)) :
    print("Semester " + str(i+1) + ":", end = " ")
    for matkul in rencana_kuliah[i] :
        print(matkul, end = " ")

    
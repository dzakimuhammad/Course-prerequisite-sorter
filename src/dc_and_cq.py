import graphmaking

# proses jalannya topological sort
def process(graf, derajat, rencana_kuliah) :
    # memasukkan mata kuliah yang bisa diambil pada satu semester (mata kuliah yang memiliki derajat = 0) ke dalam rencana kuliah
    matkul_sem = []
    for matkul in derajat : 
        if derajat[matkul] == 0 :
            matkul_sem.append(matkul)
    rencana_kuliah.append(matkul_sem)
    
    # menghilangkan node mata kuliah yang bisa diambil beserta menghilangkan relasi suksesor ke node yang dihilangkan dari graf
    for matkul_taken in matkul_sem:
        for matkul in graf :
            for succ in graf[matkul] :
                if succ == matkul_taken :
                    # menghilangkan node mata kuliah yang bisa diambil pada array suksesor suatu node
                    graf[matkul].remove(matkul_taken)

        # menghilangkan node mata kuliah yang bisa diambil dari graf
        graf.pop(matkul_taken)

        # menghilangkan node mata kuliah yang bisa diambil dari dictionary derajat
        derajat.pop(matkul_taken)

    # memperbaharui derajat dari tiap node setelah graf diubah
    graphmaking.updatederajat(graf, derajat)
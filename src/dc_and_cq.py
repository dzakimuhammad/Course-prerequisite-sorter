import graphmaking

def process(graf, derajat, rencana_kuliah) :
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
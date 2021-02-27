# fungsi membuat representasi DAG dari matriks data menggunakan dictionary
def makegraph(arr_data) :
    graf = {}
    for data in arr_data :
        succ = []
        node = data[0]
        for i in range (1, len(data)) :
            succ.append(data[i])
        graf[node] = succ
    return graf


# fungsi membuat representasi derajat tiap node dari matriks data menggunakan dictionary
def listderajat(arr_data) :
    derajat = {}
    for data in arr_data :
        succ = []
        node = data[0]
        for i in range (1, len(data)) :
            succ.append(data[i])
        derajat[node] = len(succ)
    return derajat

# prosedur memperbaharui derajat tiap node dari graf yang telah diubah
def updatederajat(graf, derajat) :
    for node in graf :
        derajat[node] = len(graf[node])
def makegraph(arr_data) :
    graf = {}
    for data in arr_data :
        succ = []
        node = data[0]
        for i in range (1, len(data)) :
            succ.append(data[i])
        graf[node] = succ
    return graf

def listderajat(arr_data) :
    derajat = {}
    for data in arr_data :
        succ = []
        node = data[0]
        for i in range (1, len(data)) :
            succ.append(data[i])
        derajat[node] = len(succ)
    return derajat

def updatederajat(graf, derajat) :
    for node in graf :
        derajat[node] = len(graf[node])
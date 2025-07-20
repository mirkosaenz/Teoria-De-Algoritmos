# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    if W == 0 or len(elementos) == 0:
        return []
    
    M = []
    for i in range(W+1):
        lista = []
        for j in range(len(elementos)+1):
            lista.append(0)
        M.append(lista)

    for w in range(1, W+1):
        for j in range(len(elementos)):
            valor = elementos[j][0]
            peso = elementos[j][1]
            if peso > w:
                print(M[w][j])
                M[w][j+1] = M[w][j]
            else:
                print(M[w-peso][j]+valor)
                M[w][j+1] = max(M[w][j], M[w-peso][j]+valor)
    
    return reconstruir(M, elementos)

def reconstruir(M, elementos):
    resultado = []
    w = len(M)-1
    j = len(M[0])-1
    
    while w > 0 and j > 0:
        if M[w][j] == M[w][j-1]:
            j -= 1
        else:
            peso = elementos[j-1][1]
            resultado.append(elementos[j-1])
            w = w-peso
            j -= 1
    
    resultado.reverse()
    return resultado

print(mochila([(3,3), (5,5), (2,2), (4,4), (7,7)], 8))
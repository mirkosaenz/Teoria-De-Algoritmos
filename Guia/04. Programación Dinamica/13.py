def bodegon_dinamico(P, W):
    if len(P) == 0 or W == 0:
        return []
    
    if len(P) == 1:
        return [P[0]] if P[0] < W else []
    
    # Lleno matriz de ceros
    M = []
    for i in range(W+1):
        M.append([])
        for j in range(len(P)+1):
            M[i].append(0)

    for w in range(W+1):
        M[w][0] = w
        for i in range(len(P)):
            if P[i] > w:
                M[w][i+1] = M[w][i]
            else: 
                M[w][i+1] = min(M[w-P[i]][i], M[w][i])
    
    return reconstruir(M, P)

def reconstruir(M, P):
    resultado = []

    i = len(M)-1
    j = len(M[0])-1

    while i > 0 and j > 0:
        if M[i][j] == M[i][j-1]:
            j -= 1
        else:
            resultado.append(P[j-1])
            i = i - P[j-1]
            j -= 1
    
    resultado.reverse()
    return resultado

print(bodegon_dinamico([1,3,4,1,2], 6))

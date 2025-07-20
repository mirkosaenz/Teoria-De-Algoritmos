def operaciones(k):
    M = [0]*(k+1)
    if k > 0:
        M[1] = 1
    
    for i in range(2, k+1):
        if i % 2 != 0:
            M[i] = M[i-1] + 1
        else:
            M[i] = min(M[i-1], M[i//2]) + 1
    
    return reconstruir(M)

def reconstruir(M):
    resultado = []

    i = len(M) - 1
    while i >= 1:
        if i % 2 != 0:
            resultado.append("mas1")
            i -= 1
        elif M[i] == M[i-1]+1:
            resultado.append("mas1")
            i -= 1
        else:
            resultado.append("por2")
            i //= 2
    
    resultado.reverse()
    return resultado

print(operaciones(23))
def lunatico(casas):
    if len(casas) <= 3:
        return [casas.index(max(casas))]
    
    M = [0]*(len(casas)+1) # Sin contar el 1ero
    N = [0]*(len(casas)+1) # Contando el 1ero


    for i in range(1, len(casas)):
        M[i+1] = max(M[i-1]+casas[i], M[i])

    for j in range(len(casas)-1):
        N[j+1] = max(N[j-1]+casas[j], N[j])

    if M[-1] > N[-1]:
        return reconstruir(M)
    
    return reconstruir[N]

def reconstruir(M):
    resultado = []

    i = len(M)-1

    while i >= 1:
        if M[i] == M[i-1]:
            i -= 1
        else:
            resultado.append(i-1)
            i -= 2
    
    return sorted(resultado)

print(lunatico([10,3,15,0,25]))
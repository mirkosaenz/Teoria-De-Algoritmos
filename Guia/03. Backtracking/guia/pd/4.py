def juan_el_vago(trabajos):
    M = [0]*(len(trabajos)+1)
    if len(trabajos) > 0:
        M[1] = trabajos[0]

    for i in range(1, len(trabajos)):
        M[i+1] = max(M[i], M[i-1]+trabajos[i])
    
    return reconstruir(M, trabajos)

def reconstruir(M, trabajos):
    resultado = []
    
    i = len(M)-1
    while i > 0:
        if M[i] == M[i-1]:
            i -= 1
        else:
            resultado.append(i-1)
            i -= 2
        
    resultado.reverse()
    return resultado

print(juan_el_vago([20,40,30,50,100]))
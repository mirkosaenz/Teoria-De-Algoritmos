def scheduling(charlas):
    charlas = sorted(charlas, key=lambda x: x[1])
    compatibles = obtener_compatibles(charlas)
    res = [0]*(len(charlas)+1)

    for i in range(len(charlas)):
        _, _, peso_actual = charlas[i]
        res[i+1] = max(res[i], peso_actual+res[compatibles[i+1]])

    return res

def reconstruir(optimos, charlas, compatibles):
    resultado = []

    i = len(optimos)-1
    while i >= 1:
        if optimos[i] == optimos[i-1]:
            i -= 1
        else:
            resultado.append(charlas[i-1])
            i = compatibles[i]
    
    resultado.reverse()
    return resultado

def obtener_compatibles(charlas):
    """
    PRE: Recibe las charlas ordenadas por tiempo de inicio
    """
    compatibles = [0]*(len(charlas)+1)
    
    for i in range(1, len(charlas)+1):
        ini, fin, peso = charlas[i-1]
        indice_compatible = 0
        for j in range(1, i):
            ini_ant, fin_ant, peso_ant = charlas[j-1]
            if fin_ant <= ini:
                indice_compatible = j
            else:
                break
        compatibles[i] = indice_compatible
    
    return compatibles
        
print(obtener_compatibles(
   [(0,3,2),
    (1,5,4),
    (3,6,4),
    (2,7,7),
    (6,8,2),
    (6,9,1),
   ] 
))
def compra_venta(p):
    if len(p) <= 2:
        return 0, 0
    
    # Devuelve, para cada i, el menor precio al que se puede comprar hasta el dia i inclusive
    c = obtener_min_compra(p)

    M = [0]*(len(p)+1)

    for i in range(2, len(p)+1):
        # Elijo entre comprar y vender antes o comprar hoy/antes y vender hoy
        M[i] = max(M[i-1], p[i]-c[i])
    
    i = len(M)-1
    while i > 1 and M[i] == M[i-1]:
        i -= 1
    
    venta = i-1
    compra = p.index(c[i])

    return compra, venta

def obtener_min_compra(p):
    M = [0]*(len(p)+1)
    M[1] = p[0]

    for i in range(2, len(p)+1):
        M[i] = min(M[i-1], p[i-1])
    
    return M
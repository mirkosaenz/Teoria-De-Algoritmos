def escalones(n):
    if n == 0:
        return 1
    M = [0]*(n+1)

    for i in range(n):
        valor = 0
        k = 1

        while (i+1)-k >= 0 and k <= 3:
            valor += M[i+1-k]
            k += 1
        
        if i <= 2:
            valor += 1
        
        M[i+1] = valor
    
    return M[n]
def laberinto(matriz):
    n = len(matriz)
    m = len(matriz[0])

    res = []

    for i in range(n):
        res.append([0]*m)

        for j in range(m):
            suma = matriz[i][j]
            if (i, j) == (0,0):
                res[i][j] == suma
                continue
            if i == 0:
                res[i][j] = res[i][j-1] + suma
            elif j == 0:
                res[i][j] = res[i-1][j] + suma
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1]) + suma
    
    return res[n-1][m-1]


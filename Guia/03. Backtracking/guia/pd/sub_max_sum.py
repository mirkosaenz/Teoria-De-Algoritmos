def max_subarray(arr):
    if len(arr) == 0:
        return []
    sumas, inicio = obtener_sumas_indice(arr)

    M = [0]*(len(arr)+1)

    for i in range(1, len(arr)+1):
        M[i] = max(M[i-1], sumas[i-1])
    
    return reconstruccion(arr, M,  inicio)

def obtener_sumas_indice(arr):
    sumas = [0]*len(arr)
    inicio = [0]*len(arr)

    for i in range(len(arr)):
        suma_max = 0
        indice_izq_min = i
        indice_izq = i
        indice_der = i

        while indice_izq >= 0:
            suma = sum(arr[indice_izq:indice_der+1])

            if suma > suma_max:
                suma_max = suma
                indice_izq_min = indice_izq
            
            indice_izq -= 1
        
        sumas[i] = suma_max
        inicio[i] = indice_izq_min
    
    return sumas, inicio

def reconstruccion(arr, M, inicio):
    i = len(M)-1

    while i > 1 and M[i] == M[i-1]:
        i -= 1
    
    der = i
    izq = inicio[i-1]

    return arr[izq:der] if sum(arr[izq:der]) > 0 else []
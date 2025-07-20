def max_subarray(arr):
    if len(arr) == 0:
        return arr, 0
    if len(arr) == 1:
        return ((arr, arr[0]) if arr[0] >= 0 else ([], 0))
    
    mitad = len(arr) // 2
    izq, suma_parte_izq = max_subarray(arr[:mitad])
    der, suma_parte_der = max_subarray(arr[:mitad])

    indice_izq = mitad-1
    suma_izq = 0
    suma_mitad = 0
    for i in range(mitad-1, -1, -1):
        suma_izq += arr[i]
        if suma_mitad + suma_izq > suma_mitad:
            indice_izq = i
            suma_mitad += suma_izq
            suma_izq = 0
    
    indice_der = mitad
    suma_der = 0
    for i in range(mitad, len(arr)):
        suma_der += arr[i]
        if suma_mitad + suma_der > suma_mitad:
            indice_der = i
            suma_mitad += suma_der
            suma_der = 0
    
    max_suma = max(suma_parte_izq, suma_parte_der, suma_mitad)
    if max_suma == suma_parte_izq:
        return izq, suma_parte_izq
    if max_suma == suma_parte_der:
        return der, suma_parte_der
    
    return arr[indice_izq:indice_der+1], suma_mitad
    
print(max_subarray([5, 3, 2, 4, -1]))
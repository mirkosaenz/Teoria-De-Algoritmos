def mas_de_la_mitad(arr):
    candidato = _mas_de_la_mitad(arr)
    return arr.count(candidato) > len(arr) / 2

def _mas_de_la_mitad(arr):
    if len(arr) <= 3:
        for elem in arr:
            if arr.count(elem) > len(arr) / 2:
                return elem
        return -1
    
    i = 0
    posibles = []
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            posibles.append(arr[i])
        i += 2
    
    # Si se repite mas de la mitad en el arreglo generado, se cumple para este
    candidato = _mas_de_la_mitad(posibles)
    if arr.count(candidato) > len(arr) / 2:
        return True
    
    # Si se repite mas de la mitad el ultimo y soy impar, se cumple
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr)/2:
        return True

    return False

print(mas_de_la_mitad([1,2,1,2,2,2,1,2,1,1,3]))
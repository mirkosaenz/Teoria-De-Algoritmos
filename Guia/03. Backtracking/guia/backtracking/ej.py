def combinaciones_dos(numeros):
    for i in range(len(numeros)):
        _combinaciones_dos(numeros, i, [], [])

def _combinaciones_dos(numeros, num_actual, comb_actual, combinaciones_total):
    if num_actual == len(numeros):
        return
    
    comb_actual.append(numeros[num_actual])
    if len(comb_actual) == 3:
        print(comb_actual)
    
    _combinaciones_dos(numeros, num_actual+1, comb_actual, combinaciones_total)
    if len(comb_actual) >= 1:
        comb_actual.pop()
    _combinaciones_dos(numeros, num_actual+1, comb_actual, combinaciones_total)

print(combinaciones_dos([1,2,3,4,5]))
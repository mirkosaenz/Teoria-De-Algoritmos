def tiradas_suman(n, s):
    return _tiradas_suman(n, s, [], 0, [])

def _tiradas_suman(n, s, sol_parcial, suma_parcial, soluciones):
    if suma_parcial > s:
        return soluciones
    
    if len(sol_parcial) == n:
        if suma_parcial == s:
            soluciones.append(sol_parcial.copy())
        return soluciones
    
    soluciones_max = soluciones

    for i in range(1, 7):
        sol_parcial.append(i)
        soluciones_max = _tiradas_suman(n, s, sol_parcial, suma_parcial+i, soluciones_max)
        sol_parcial.pop()
    
    return soluciones_max

print(tiradas_suman(2, 7))
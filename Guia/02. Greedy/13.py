def cobertura(casas, R, K):
    antenas = []
    casas = sorted(casas)

    for casa in casas:
        if len(antenas) == 0 or antenas[len(antenas)-1] + R < casa:
            nueva_antena = casa+R
            if nueva_antena > K:
                nueva_antena = K
            
            antenas.append(nueva_antena)

    return antenas

print(cobertura([0, 100, 200], 100, 200))
def bolsas(capacidad, productos):
    bolsas = []
    peso_bolsas = []
    productos = sorted(productos, reverse=True)
    
    for producto in productos:
        
        # Si entra en alguna de las bolsas existentes, lo agrego
        agregado = False
        for i in range(len(bolsas)):
            restante = capacidad - peso_bolsas[i]
            if producto <= restante:
                bolsas[i].append(producto)
                peso_bolsas[i] += producto
                agregado = True
                break
        
        # Si no entro en ninguna bolsa lo agrego en una nueva
        if not agregado:
            bolsas.append([])
            bolsas[len(bolsas)-1].append(producto)
            peso_bolsas.append(producto)

    return bolsas

print(bolsas(5, [1,2,3,4,5,4,2]))
def contar_digitos(numero):
    if numero < 10:
        return 1
    
    return 1 + contar_digitos(numero // 10)

def multiplicar(a, b):
    if b < 10 or a < 10:
        return a*b

    es_impar = False
    n = contar_digitos(a)
    if n % 2 != 0:
        a *= 10
        b *= 10
        n += 1
        es_impar = True
    
    mitad = n // 2

    x0, x1 = separar(a, mitad)
    y0, y1 = separar(b, mitad)

    # Me armo los prods que necesito
    x1y1 = multiplicar(x1, y1)
    x0y0 = multiplicar(x0, y0)
    prod_mesopotamico = multiplicar(x1+x0, y1+y0)
    x1y0_x0y1 = prod_mesopotamico - x0y0 - x1y1

    resultado = (x1y1)*(10**n) + (10**(n//2))*x1y0_x0y1 + x0y0
    if es_impar:
        resultado = resultado // 100
    
    return resultado
    

def separar(n, mitad):
    n1 = n // (10 ** mitad)
    n0 = n - (n1*(10**mitad))

    return n0,n1


print(multiplicar(125, 125))
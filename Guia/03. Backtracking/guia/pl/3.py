import pulp as pl
from pulp import LpAffineExpression as Sumatoria
from grafo import Grafo

def vertex_cover_min(grafo):
    vertices = list(grafo.obtener_vertices())
    prob = pl.LpProblem("vertex_cover", pl.LpMinimize)

    # Yi = 1 si el vertice i esta, 0 en otro caso
    variables_y = []

    for i in range(len(vertices)):
        vertice = vertices[i]
        variables_y.append(pl.LpVariable(vertice, cat="Binary"))

    for i in range(len(vertices)):
        vertice = vertices[i]
        variable = variables_y[i]
        
        # ai=0 si el vertice no tiene aristas, 1 en otro caso
        ai = 0 if len(grafo.adyacentes(vertice)) == 0 else 1
        cant_adyacentes = len(grafo.adyacentes(vertice))
        
        variables_ady = []
        for k in range(len(vertices)):
            if k == i or vertices[k] not in grafo.adyacentes(vertice):
                continue

            variables_ady.append(variables_y[k])
        
        comb_lineal_restricc = variable + Sumatoria([ (adyacente, 1) for adyacente in variables_ady ])
        # yi+sum(para todo k ady, yk) >= ai
        prob += comb_lineal_restricc >= 1*variable + cant_adyacentes*(1-variable)

    prob += Sumatoria([(variable, 1) for variable in variables_y])
    prob.solve()
    
    agregados = []
    for y in variables_y:
        valor = pl.value(y)
        if valor == 1:
            agregados.append(y.getName())
    
    return agregados

def main():
    grafo = Grafo(es_dirigido=False)
    vertices = ["a", "b", "c", "d"]
    
    for vertice in vertices:
        grafo.agregar_vertice(vertice)
    
    grafo.agregar_arista("a", "b")
    grafo.agregar_arista("a", "c")
    grafo.agregar_arista("d", "c")

    return vertex_cover_min(grafo)

    
print(main())
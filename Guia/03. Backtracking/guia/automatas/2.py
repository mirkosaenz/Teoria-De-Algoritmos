from automata import Automata

def automata_pares_1y0():
    a = Automata()
    
    # Agregar estados
    a.estado("q0", es_inicial=True, es_final=True)
    a.estado("q1")
    a.estado("q2")
    a.estado("q3")

    # Agrego transiciones
    a.transicion_estado("q0", "q1", "1")
    a.transicion_estado("q1", "q0", "1")
    a.transicion_estado("q0", "q2", "0")
    a.transicion_estado("q2", "q0", "0")
    a.transicion_estado("q1", "q3", "0")
    a.transicion_estado("q3", "q1", "0")
    a.transicion_estado("q2", "q3", "1")
    a.transicion_estado("q3", "q2", "1")

    return a
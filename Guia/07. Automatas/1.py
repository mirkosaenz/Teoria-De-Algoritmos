from automata import Automata

def automata_potencias_2():
    a = Automata()
    
    # Añadir estados
    a.estado("q0", es_inicial=True)
    a.estado("q1", es_final=True)
    a.estado("q2")

    # Añadir transiciones
    a.transicion_estado("q0", "q0", "0")
    a.transicion_estado("q0", "q1", "1")
    a.transicion_estado("q1", "q1", "0")
    a.transicion_estado("q1", "q2", "1")

    return a
from automata import Automata

def expresion():
    a = Automata()

    # Agrego estados
    a.estado("q0", es_inicial=True, es_final=True)
    a.estado("q1")
    a.estado("q2")
    a.estado("q3")
    a.estado("q4")
    a.estado("q5")
    a.estado("q6", es_final=True)
    a.estado("q7")

    # Agrego transiciones

    # Hago operacion estrella con cadenas "aab"
    a.transicion_estado("q0", "q1", "")
    a.transicion_estado("q1", "q2", "a")
    a.transicion_estado("q2", "q3", "a")
    a.transicion_estado("q3", "q4", "b")
    a.transicion_estado("q4", "q0", "")

    # Hago concatenacion con cadenas "a, aba"
    a.transicion_estado("q0", "q5", "")
    a.transicion_estado("q5", "q6", "a")
    a.transicion_estado("q6", "q6", "a")
    a.transicion_estado("q6", "q7", "b")
    a.transicion_estado("q7", "q6", "a")

    return a
from automata import Automata

def expresion():
    a = Automata()
    # resolucion del ejercicio

    # Agrego estados
    a.estado("q0", es_inicial=True)
    a.estado("q1")
    a.estado("q2")
    a.estado("q3")
    a.estado("q4", es_final=True)
    a.estado("q5", es_final=True)
    a.estado("q6")
    a.estado("q7")

    # Agrego transiciones

    # Automata 1: ((ab)+ba*)
    a.transicion_estado("q1", "q2", "a")
    a.transicion_estado("q2", "q3", "b")
    a.transicion_estado("q3", "q1", "")
    a.transicion_estado("q3", "q4", "b")
    a.transicion_estado("q4", "q4", "a")

    # Automata 2: (b*(ab)*)
    a.transicion_estado("q5", "q5", "b")
    a.transicion_estado("q5", "q6", "a")
    a.transicion_estado("q6", "q7", "b")
    a.transicion_estado("q7", "q5", "")

    # Operaciones entre los lenguajes

    # El primero es opcional
    a.transicion_estado("q0", "q1", "")
    a.transicion_estado("q0", "q5", "")

    # Concateno el lenguaje 1 al lenguaje 2
    a.transicion_estado("q4", "q5", "")


    return a
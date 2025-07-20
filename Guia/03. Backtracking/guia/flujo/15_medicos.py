from grafo import Grafo
from ff import ford_fulkerson

DURACION_TURNO = 1 #En horas

def obtener_red(especialidad, medicos, pacientes):
    red = Grafo(es_dirigido=True)
    horarios_pacientes = []
    horarios_medicos = []

    red.agregar_vertice("S") #Fuente
    red.agregar_vertice("T") #Sumidero

    for paciente in pacientes:
        nombre, especialidad_requerida, horarios = paciente
        if especialidad_requerida == especialidad:
            red.agregar_vertice(nombre)
            red.agregar_arista("S", nombre, peso=1)

            for horario in horarios:
                vertice_horario = (nombre, horario)
                red.agregar_vertice(vertice_horario)
                red.agregar_arista(nombre, vertice_horario, peso=1)
                horarios_pacientes.append(vertice_horario)
    
    for medico in medicos:
        nombre, especialidad_med, horarios = medico
        if especialidad_med == especialidad:
            red.agregar_vertice(nombre)

            for horario in horarios:
                duracion_franja = int(horario[1]) - int(horario[0])
                vertice_horario = (nombre, horario)
                red.agregar_vertice(vertice_horario)
                red.agregar_arista(vertice_horario, "T", peso=duracion_franja/DURACION_TURNO)
                horarios_medicos.append(vertice_horario)
    
    for vertice_horario_pac in horarios_pacientes:
        nombre_pac, horario_pac = vertice_horario_pac
        ini_pac, fin_pac = horario_pac

        for vertice_horario_med in horarios_medicos:
            nombre_med, horario_med = vertice_horario_med
            ini_med, fin_med = horario_med
            
            # La coincidencia de horarios esta incluida en ambos casos
            cond1 = (ini_pac <= fin_med and fin_pac >= ini_med) #Arranco despues que el medico pero antes q termine
            cond2 = (ini_med <= fin_pac and fin_med >= ini_pac) # Termino antes que el medico pero despues de que arranque
            if cond1 or cond2:
                red.agregar_arista(vertice_horario_pac, vertice_horario_med, peso=1)
    
    return red

def obtener_redes(medicos, pacientes):
    redes = {}
    especialidades = set(med[1] for med in medicos)

    for especialidad in especialidades:
        red = obtener_red(especialidad, medicos, pacientes)
        redes[especialidad] = red
    
    return redes

def asignar_turnos(medicos, pacientes):
    """
    Recibe:
    -   Medicos = (nombre, especialidad, [(ini, fin), ...])
    -   Pacientes = (nombre, especialidad, [(ini, fin), ...])
    -   
    }
    """
    redes = obtener_redes(medicos, pacientes)
    flujos = {}

    for especialidad in redes:
        red = redes[especialidad]
        flujo = ford_fulkerson(red)

        caminos = []

        actual = "S"
        cam_actual = []
        while cam_actual != None:
            cam_actual.append(actual)
            if actual == "T":
                caminos.append(cam_actual)
                cam_actual = []
                actual = "S"
                continue
            
            sig = None
            for ady in red.adyacentes(actual):
                arista = (actual, ady)
                if flujo[arista] == 1:
                    sig = ady
                    flujo[arista] = 0
                    break
            
            if sig == None:
                cam_actual = None
            
            actual = sig


        flujos[especialidad] = caminos
    
    return flujos

def main():
    medicos = []
    pacientes = []
    archivo = open("datos/datos_15.txt")
    for linea in archivo:
        linea = linea.strip()
        tipo, nombre, especialidad, horarios = linea.split(",")
        horarios = horarios.split("/")
        horarios = [(hora.split("-")[0], hora.split("-")[1]) for hora in horarios]

        if tipo == "Medico":
            medicos.append((nombre, especialidad, horarios))
        else:
            pacientes.append((nombre, especialidad, horarios))
    
    
    flujos = asignar_turnos(medicos, pacientes)
    print(flujos)

main()
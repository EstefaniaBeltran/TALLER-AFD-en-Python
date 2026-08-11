import sys

# Verificar que se hayan enviado los dos archivos
if len(sys.argv) != 3:
    print("Uso: python3 AFD.py archivo_conf archivo_cadenas")
    sys.exit()

archivo_conf = sys.argv[1]
archivo_cadenas = sys.argv[2]

# Variables del automata
estados = []
alfabeto = []
inicial = ""
finales = []
transiciones = {}

# Leer el archivo de configuracion
with open(archivo_conf, "r") as archivo:

    for linea in archivo:

        # Quitar espacios y salto de linea
        linea = linea.strip()

        # Ignorar comentarios y lineas vacias
        if linea.startswith("#") or linea == "":
            continue

        # Leer los datos principales
        if linea.startswith("estados="):
            estados = linea.split("=")[1].split(",")

        elif linea.startswith("alfabeto="):
            alfabeto = linea.split("=")[1].split(",")

        elif linea.startswith("inicial="):
            inicial = linea.split("=")[1]

        elif linea.startswith("inicio="):
            inicial = linea.split("=")[1]

        elif linea.startswith("finales="):
            valor = linea.split("=")[1]
            if valor != "":
                finales = valor.split(",")

        elif linea.startswith("aceptacion="):
            finales = [linea.split("=")[1]]

        elif linea.startswith("transiciones="):
            continue

        else:
            # Leer una transicion
            partes = linea.split(",")

            estado_actual = partes[0]
            simbolo = partes[1]
            estado_siguiente = partes[2]

            transiciones[(estado_actual, simbolo)] = estado_siguiente


# Mostrar la informacion que leyo el programa
print("Estados:", estados)
print("Alfabeto:", alfabeto)
print("Estado inicial:", inicial)
print("Estados finales:", finales)
print()


# Leer las cadenas
with open(archivo_cadenas, "r") as archivo:

    for cadena in archivo:

        # Quitar espacios y salto de linea
        cadena = cadena.strip()

        estado_actual = inicial
        aceptada = True

        # Recorrer cada simbolo de la cadena
        for simbolo in cadena:

            # Verificar que el simbolo pertenezca al alfabeto
            if simbolo not in alfabeto:
                aceptada = False
                break

            # Buscar la transicion
            if (estado_actual, simbolo) in transiciones:
                estado_actual = transiciones[(estado_actual, simbolo)]
            else:
                aceptada = False
                break

        # Comprobar si termino en un estado final
        if aceptada and estado_actual in finales:
            print(repr(cadena), "-> ACEPTADA")
        else:
            print(repr(cadena), "-> RECHAZADA")

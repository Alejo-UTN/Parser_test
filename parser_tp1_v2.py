from Lexer_tp import *
VN = [ "Program","ListSentencia","ListSentenciaP","SentSi","SentenciaSiP","SentRepetir","SentAsignar","SentLeer",
"SentMostar","SentFun","Proc","ListPar","ListParP","Expresion","ExpresionP",
"Expresion2","Expresion2P","Termino","TerminoP","Factor"]

VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTRAR", "FUN", "FINFUC", "=", "," , ";", ">,<,<=,>=", "NUMERO", "ID"]


tabla ={
    'Program':{
        "SI": ["ListSentencia"],
        "REPERTIR":["ListSentencia"],
        "LEER":["ListSentencia"],
        "FUN":["ListSentencia"],
        "MOSTRAR":["ListSentencia"],
        "ID":["ListSentencia"]
    }, 
    "ListSentencia":{
        "SI": ["Sentencia","ListSentencia"],
        "REPERTIR":["Sentencia","ListSentencia"],
        "LEER":["Sentencia","ListSentencia"],
        "FUN":["Sentencia","ListSentencia"],
        "MOSTRAR":["Sentencia","ListSentencia"],
        "ID":["Sentencia","ListSentencia"]
    },
    "ListSentenciaP":{
        ";":[";","Sentencia","ListSentenciaP"],
        "#":[],
        "SINO":[],
        "FINSI":[],
        "HASTA":[],
        "FINFUC":[]
    },
    "SentSI":{
        "SI":["SI","Expresion","ENTONCES","ListSentencia","SentenciaSiP"],
    },
    "SentenciaSiP":{
        "SINO":["SINO","ListSentencia","FINSI"],
        "FINSI":["FINSI"]
    },
    "SentRepetir":{
        "REPETIR":["REPETIR","ListSentencia","HASTA","Expresion"]
    },
    "SentAsignar":{
        "ID":["ID","=","Expresion"]
    },
    "sentLeer":{
        "LEER":["LEER","ID"]
    },
    "SentMostrar":{
        "MOSTRAR":["MOSTRAR","Expresion"]
    },
    "SentFun":{
        "FUN":["FUN","Proc","FINFUC"]
    },
    "Proc":{
        "ID":["ID","ListaPar","ListSentencia"]
    },
    "ListaPar":{
        "ID":["ID","ListaParP"]
    },
    "ListaParP":{
        ";":[";","ID","ListaParP"]
    },
    "Expresion":{
        "NUMERO":["Expresion2","ExpresionP"],
        "ID":["Expresion2","ExpresionP"]
    },
    "ExpresionP":{
        ">,<,>=,<=":[">,<,>=,<=","Expresion2"],
        "=":[],
        ";":[],
        "#":[],
        "FINFUC":[],
        "FINSI":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Expresion2":{
        "NUMERO":["Termino","Expresion2P"],
        "ID":["Termino","Expresion2P"]
    },
    "Expresion2P":{
        "+":["+","Termino","Expresion2P"],
        ">,<,>=,<=":[],
        "=":[],
        "#":[],
        "FINSI":[],
        ";":[],
        "FINFUC":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Termino":{
        "NUMERO":["Factor","TerminoP"],
        "ID":["FACTOR","TerminoP"]
    },
    "TerminoP":{
        "*":["*","Factor","TerminoP"],
        "+":[],
        ">,<,>=,<=":[],
        "=":[],
        "#":[],
        ";":[],
        "FINFUC":[],
        "FINFUC":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Factor":{
        "NUMERO":["NUMERO"],
        "ID":["ID"]
    }
}
def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

# Función que genera las derivaciones, recibe el elemento a derivar, en que cadena y por que se deriva


def genDerivacion(topePila, produccionAnterior, derivacion):
    # Obtenemos en que posición se encuentra el elemento a derivar
    indice = produccionAnterior.index(topePila)
    # Eliminamos el elemento a derivar
    produccionAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionInvertida = []
    for i in derivacion:
        produccionInvertida.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionInvertida:
        produccionAnterior.insert(indice, i)

    return produccionAnterior


# Función principal
def parser(cadena):
    # Iniciamos la pila con el simbolo EOF (#) y el simbolo distinguido
    pila = ['#', 'Program']
    simboloApuntado = 0
    # Lista donde se trabaja con las derivaciones en cada ciclo
    derivacion = ['Program']
    # Lista donde se guardan todas las derivaciones
    derivaciones = []

    # Flag para salir del ciclo principal
    continuar = True

    # Ciclo principal
    while continuar:
        # Actualizamos el valor del tope
        tope = pila[-1]

        # Condición de éxito
        if (tope == '#') and (cadena[simboloApuntado] == '#'):
            print("La cadena es aceptada por el lenguaje")
            print("Derivaciones:")
            for i in derivaciones:
                print(i)
            break

        if tope in VT:
            if tope == cadena[simboloApuntado]:
                # Consumimos el último elemento de la pila
                pila.pop()
                # Avanzamos el puntero en un elemento
                simboloApuntado += 1

            # Si no se cumple la condición salimos del ciclo
            else:
                continuar = False
                print("La cadena no pertenece al lenguaje")
        else:
            # Intentamos obtener el elemento de la tabla en la posición indicada
            try:
                produccionTabla = tabla[tope][cadena[simboloApuntado]]
                # Damos vuelta la producción
                produccionInvertida = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionInvertida.insert(0, i)
                # Consumimos el último elemento de la pila
                pila.pop()
                # Agregamos la producción dada vuelta a la pila
                pila.extend(produccionInvertida)
                # Guardamos la derivación
                derivacion = genDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())

            # Si hay error salimos del ciclo
            except:
                continuar = False
                print("La cadena no pertenece al lenguaje")

#AIUDAAAAAAAAAAAAA




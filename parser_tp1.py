# Función que convierte la salida del lexer a una lista que el parser puede entender
def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

def genDerivaciones(topePila, prodAnterior, derivacion)
    #wea para saber la posicion del elemento a derivar
    indice = prodAnterior.index(topePila)
    #limpio el elemento a derivar
    prodAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionReversed = []
    for i in derivacion:
        produccionReversed.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionReversed:
        prodAnterior.insert(indice, i)
    
    return prodAnterior

# "program -> estructura program" tiene como simbolos directrices a: "ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI"...
# El EOF es el simbolo #

#NOTA TEMPORAL:Los NT van en minuscula y los T en mayuscula.|  Program es un NT que deriva excluyentemente en ENTONCES, SINO, etc,etc. Luego continua con un estructura o program.

# tabla[Columna][Fila]
tabla = {
    "program":{
        "ENTONCES" :     [ "estructura" , "program"],
        "REPERTIR" :     [ "estructura" , "program"],
        "HASTA" :        [ "estructura" , "program"],
        "SI" :           [ "estructura" , "program"],
        "LEER" :         [ "estructura" , "program"],
        "MOSTRAR":       [ "estructura" , "program"],
        "FUN" :          [ "estructura" , "program"],
        "ID" :           [ "estructura" , "program"],
        "," :            [],
        "#" :            []
    },
    "estructura":{
        "SI":           ["SI","expresion", "ENTONCES", "FUN", "program",",","SINO","FUN","program","," ],
        "ENTONCES" :    [ "FUN","program",","],
        "HASTA" :       ["HASTA","expresion","program",","],
        "REPETIR" :     ["REPETIR", "FUN", "program", "HASTA", "expresion", "program", ","],
        "MOSTRAR" :     ["MOSTRAR", "expresion"],
        "LEER" :        ["LEER", "expresion"],
        "ID" :          ["ID", "expresion"]
    },
    "valor":{
        "ID" :  ["ID"],
        "NUMERO":  ["NUMERO"]
    },
    "expresion":{
        "ID" : ["termino","expresion2"],
        "NUMERO": ["termino", "expresion2"]
    },
    #Se hace asi por la jerarquia de la suma y la mltiplicacion, con los terminos siendo multiplicaciones y las expresion 2 las sumas
    "expresion2":{
        "+":        ["+", "termino", "expresion" ],
        "SI":       [],
        "ENTONCES": [],
        "HASTA":    [],
        "REPETIR":  [],
        "MOSTRAR":  [],
        "LEER":     [],
        "ID":       []
    },
    "termino":{
        "ID":     ["factor", "termino2"],
        "NUMERO": ["factor", "termino2"]
    },
    "termino2":{
        "*": ["*", "factor", "termino2"],
        "SI":       [],
        "ENTONCES": [],
        "HASTA":    [],
        "REPETIR":  [],
        "MOSTRAR":  [],
        "LEER":     [],
        "ID":       []
    },
    "factor":{
        "ID":       ["valor"],
        "NUMERO":   ["valor"]
     }
}
        

# listas de V.Terminales
VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTAR", "FUN", "FINFUC", "=", "," , ";", ">,<,<=,>=", "NUMERO", "ID"]

#codigo parser
def parse(cadena)
    #Vamos a tenre una pila con el EOF y el simbolo distinguido
    pila = ["#", "program"]
    #Variable temporal para la derivacion actual, le damos el SD
    der = ["program"]
    #Variable para almacenar las derivaciones
    derivaciones = []
    #"Puntero"
    pointer = 0
    #Variable para romper el ciclo
    i = 1
    while i = 1:
        #Le meto el tope de la pila a top ||Nota a mi mismo: poner un indice negativo empieza a contar desde el tope -1 es el tope||
        top = pila[-1]
        #Formula para consumir lo de la pila
        if top in VT:
            if top == cadena[pointer]:
                #Consumimos ||Nota personal: Pop le hace POP! a lo que le digas y lo borra
                pila.pop()
                pointer = pointer + 1
            else:
                #Abandonamos porque no pertenece
                print("La cadena no pertenece al lenuaje")
                seg = 0
        #Ahora determinamos que significa que la cadena sea aceptada y creamos la condicion
        if (top == '#'):
            if (cadena[pointer] == "#"):
                print("La cadena es aceptadoa por el lenguaje")
                for j in derivaciones: print(j)
        


            
            
    







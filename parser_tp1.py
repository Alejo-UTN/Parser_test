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


# "Program -> Estructura Program" tiene como simbolos directrices a: "ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI"...
# El EOF es el simbolo #

# tabla[Columna][Fila]
tabla = {
    "program": {
        "ENTONCES" :     [ "estructura" , "program"],
        "SINO" :         [ "estructura" , "program"],
        "FINSI" :        [ "estructura" , "program"],
        "REPERTIR" :     [ "estructura" , "program"],
        "HASTA" :        [ "estructura" , "program"],
        "SI" :           [ "estructura" , "program"],
        "LEER" :         [ "estructura" , "program"],
        "FUN" :          [ "estructura" , "program"],
        "FINFUC" :       [ "estructura" , "program"],
        "ID" :           [ "estructura" , "program"],
        "#" :            []
    };
    "estructura":{
        "ENTONCES" : [ "FUN","FINFUN","LEER","MOSTAR","ID"],
        "SINO" : [ "FUN","FINFUN","LEER","MOSTAR","ID"],
    };
    "valor":{
        "ID" :  ["ID"],
        "NUMERO":  ["NUMERO"]
    };
    "expresion":{
        "(" : []

#Gola como te va

VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTAR", "FUN", "FINFUC", "=", "," , ";", ">,<,<=,>=", "NUMERO", "ID"]

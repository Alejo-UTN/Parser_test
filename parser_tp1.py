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


# "program -> estructura program" tiene como simbolos directrices a: "ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI"...
# El EOF es el simbolo #

#NOTA TEMPORAL:Los NT van en minuscula y los T en mayuscula.|  Program es un NT que deriva excluyentemente en ENTONCES, SINO, etc,etc. Luego continua con un estructura o program.

# tabla[Columna][Fila]
tabla = {
    "program": {
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
    };
    "estructura":{
        "SI":        ["SI","expresion", "ENTONCES", "FUN", "program",",","SINO","FUN","program","," ],
        "ENTONCES" : [ "FUN","program",","],
        "HASTA" :    ["HASTA","expresion","program",","],
        "REPETIR" :  ["REPETIR", "FUN", "program", "HASTA", "expresion", "program", ","],
        "MOSTRAR" :  ["MOSTRAR", "expresion",]
        
       
    "valor":{
        "ID" :  ["ID"],
        "NUMERO":  ["NUMERO"]
    };
    "expresion":{
        "(" : []



VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTAR", "FUN", "FINFUC", "=", "," , ";", ">,<,<=,>=", "NUMERO", "ID"]

# Función que convierte la salida del lexer a una lista que el parser puede entender
def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

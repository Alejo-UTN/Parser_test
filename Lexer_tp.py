# DEFINI A CADA AFD CON NOMBRE DEPENDIEDNDO DE LOS TOKENS 
# LISTA DE TOKENS 
# TOKEN1 = ENTONCES 
#TOKEN2 = SINO 
#TOKEN3 = FINSI 
#TOKEN4 = REPETIR 
#corregir las constantes 
estadofinal = "estado_final"
estadonofinal = "estado2 no aceptado"
estadotrampa = "esta en estado2 trampa"
codigo = ""
def afdtoken1(lexema):
    estado1 = 0
    estadofinal1 = [8]
    for caracter in lexema: 
        if estado1 == 0 and caracter == 'e':
            estado1 = 1
        elif estado1 == 1 and caracter == 'n' :
             estado1 = 2
        elif estado1 == 2 and caracter == 't' :
             estado1 = 3
        elif estado1 == 3 and caracter == 'o' :
            estado1 = 4
        elif estado1 == 4 and caracter == 'n' :   
            estado1 = 5
        elif estado1 == 5 and caracter  == 'c' :
            estado1 = 6
        elif estado1 == 6 and caracter == 'e' :
            estado1 = 7
        elif estado1 == 7 and caracter == 's' :
            estado1 = 8
        else:
            estado1 = -1
            break 

    if estado1 == -1 :
      return estadotrampa
    if estado1 in estadofinal1 :
      return estadofinal
    else : 
      return estadonofinal
#ADF PARA EL TOKEN1 CHEQUEADO QUE FUNCIONA !!!!!!!

    #python -i sintaxis\ laboratorio.py  

#if __name__=='__main__':
 #   afd('lexema')

 #token2 = sino

def afdtoken2(lexema):
    estado2 = 0 
    estadofinal2 = [4]
    for caracter in lexema:
        if estado2 == 0 and caracter == 's' :
           estado2 = 1
        elif estado2 == 1 and caracter == 'i' :
           estado2 = 2
        elif estado2 == 2 and caracter == 'n' :
           estado2 = 3
        elif estado2 == 3  and caracter == 'o' : 
           estado2 = 4
        else: 
            estado2 = -1
            break
    
    if estado2 == -1 :
        return estadotrampa
    if estado2 in estadofinal2 :
        return estadofinal
    else:
        return estadonofinal
    # CHEQUEAdo SI FUNCIONA ESTE AUTOMATA 

    # TOKEN3 =FINSI 
def afdtoken3(lexema):
    estado3 = 0
    estadofinal3 = [5]
    for caracter in lexema :
        if estado3 == 0 and caracter == 'f' : 
           estado3 = 1
        elif estado3 == 1  and caracter == 'i': 
           estado3 = 2
        elif estado3 == 2 and caracter == 'n' : 
            estado3 = 3 
        elif estado3 == 3 and caracter == 's' : 
             estado3 = 4 
        elif estado3 == 4 and caracter == 'i' : 
            estado3 = 5 
        else:
            estado3 = -1
            break 

    if estado3 == -1 :
       return estadotrampa
    if estado3 in estadofinal3 :
       return estadofinal 
    else: 
       return estadonofinal 

# TOKEN 3 CHEQUEAdo AUN 
 # TOEEN 4 repetir 

def afdtoken4(lexema):
    estado4 = 0 
    estadofinal4 = [7]
    for caracter in lexema :
        if estado4 == 0 and caracter == 'r' :
             estado4 = 1 
        elif estado4 == 1 and caracter == 'e' :
             estado4 = 2 
        elif estado4 == 2 and caracter == 'p' : 
             estado4 = 3 
        elif estado4 == 3 and caracter == 'e' : 
             estado4 = 4 
        elif estado4 == 4 and caracter == 't' : 
             estado4 = 5
        elif estado4 == 5 and caracter == 'i' : 
             estado4 = 6 
        elif estado4 == 6 and caracter == 'r' : 
             estado4 = 7
        else:
            estado4 = -1
            break 
    if estado4 == -1 : 
        return estadotrampa
    if estado4  in estadofinal4 : 
        return  estadofinal
    else:
        return estadonofinal
             
# token 4 chequeado 
# token 5 para palabra reservada hasta 

def afdtoken5(lexema):
    estado5 = 0 
    estadofinal5 = [5]
    for caracter in lexema : 
        if estado5 == 0 and caracter == 'h' : 
            estado5 = 1
        elif estado5 == 1 and caracter == 'a' : 
            estado5 = 2
        elif estado5 == 2 and caracter == 's' : 
            estado5 = 3 
        elif estado5 == 3 and caracter == 't' : 
            estado5 = 4
        elif estado5 == 4 and caracter == 'a' : 
            estado5 = 5 
        else: 
         estado5 = -1 
         break 
    if estado5 == -1 :
     return estadotrampa
    if estado5 in estadofinal5 :
     return estadofinal
    else: 
        return estadonofinal
#chequeado
 # token 6 para palabra reservada SI 

def afdtoken6(lexema):
    estado6 = 0
    estadofinal6 = [2]
    for caracter in lexema :
        if estado6 == 0 and caracter == 's' : 
            estado6 = 1 
        elif estado6 == 1 and caracter == 'i' : 
            estado6 = 2
        else :
            estado6 = -1 
            break 
    if estado6 == -1 : 
        return estadotrampa
    if estado6 in estadofinal6 :
        return estadofinal
    else :
        return estadonofinal
    # chequeado adf para palabra reservada si 
    # token 7 para la palabra reservada +

def afdtoken7(lexema):
    estado7 = 0 
    estadofinal7 = [1]
    for caracter in lexema :
        if estado7 == 0 and caracter == '+' :
            estado7 = 1
        else : 
            estado7 = -1
            break
    if estado7 == -1 : 
        return estadotrampa
    if estado7 in estadofinal7 :
        return estadofinal
    else : 
        return estadonofinal 
           
# chequeado token 7

# token 8 para l apalabra reservada *
def afdtoken8(lexema):
    estado8 = 0
    estadofinal8 = [1]
    for caracter in lexema: 
        if estado8 == 0 and caracter =='*':
            estado8 = 1 
        else :
            estado8 = -1
            break
    if estado8 == -1 :
        return estadotrampa     
    if estado8 in estadofinal8 :
        return estadofinal
    else : 
        return estadonofinal

# aun chequeado
# token 9 para la palabra reservada leer
def afdtoken9(lexema):
    estado9 = 0 
    estadofinal9 = [4]
    for caracter in lexema :
        if estado9 == 0 and caracter == 'l':
            estado9 = 1
        elif estado9 == 1 and caracter == 'e':
            estado9 = 2 
        elif estado9 == 2 and caracter == 'e':
            estado9 = 3
        elif estado9 == 3 and caracter == 'r':
            estado9 = 4 
        else: 
            estado9 = -1 
            break
    if estado9 == -1:
       return estadotrampa
    if estado9 in estadofinal9: 
        return estadofinal
    else:
        return estadonofinal 
  # token 9 chequeado    
# token10 para la palabra reservada  mostrar
def afdtoken10(lexema):
    estado10 = 0 
    estadofinal10 = [7]
    for caracter in lexema : 
        if estado10 == 0 and caracter =='m':
           esatdo10 = 1 
        elif estado10 == 1 and caracter == 'o':
           estado10 = 2   
        elif estado10 == 2 and caracter == 's':
           estado10 = 3 
        elif estado10 == 3 and caracter == 't':
            estado10 = 4 
        elif estado10 == 4 and caracter == 'r':
            estado10 = 5
        elif estado10 == 5 and caracter == 'a':
            estado10 = 6
        elif estado10 == 6 and caracter == 'r':
            estado10 = 7 
        else:
            estado10 = -1 
            break
    if estado10 == -1:
        return estadotrampa 
    if estado10 in estadofinal10 : 
        return estadofinal
    else:
        return estadonofinal

##    token 10 chequeado 
##    ahora token 11 para la palabra func

def afdtoken11(lexema):
    estado11 = 0 
    estadofinal11 = [4]
    for caracter in lexema :
        if estado11 == 0 and caracter == 'f':
            estado11 = 1
        elif estado11 == 1 and caracter == 'u':
            estado11 = 2
        elif estado11 == 2 and caracter == 'n':
            estado11 = 3 
        elif estado11 == 3 and caracter == 'c':
            estado11 = 4 
        else: 
            estado11 = -1 
            break
    if estado11 == -1 :
            return estadotrampa 
    if estado11 in estadofinal11:
            return estadofinal 
    else:
            return estadonofinal 
        
# chequeado token 11 
# ahora adf para token 12 de la palabra reservada finfunc
def afdtoken12(lexema):
    estado12 = 0 
    estadofinal12 = [7]
    for caracter in lexema :
        if estado12 == 0 and caracter =='f':
             estado12 = 1 
        elif estado12 == 1 and caracter == 'i':
             estado12 = 2 
        elif estado12 == 2 and caracter == 'n':
             estado12 = 3
        elif estado12 == 3 and caracter == 'f':
            estado12 = 4
        elif estado12 == 4 and caracter == 'u':
            estado12 = 5 
        elif estado12 == 5 and caracter == 'n':
            estado12 = 6 
        elif estado12 == 6 and caracter == 'c':
            estado12 = 7 
        else:
            estado12 = -1 
            break
    if estado12 == -1:
            return estadotrampa 
    if estado12 in estadofinal12 :
            return estadofinal
    else:
            return estadonofinal 
    # token 12 chequeado
    # ahora token 13 ´para la palñabra reserada equal  (=)
def afdtoken13(lexema):
        estado13 = 0 
        estadofinal13 = [1]
        for caracter in lexema : 
            if estado13 == 0 and caracter == '=' :
                estado13 = 1
            else:
                estado13 = -1
                break
        if estado13 == -1 :
            return estadotrampa 
        if estado13 in estadofinal13 :
            return estadofinal 
        else:
            return estadonofinal
    # token 13 chequeado 
    #ahora token 14 para la palabra reservada (,)
def afdtoken14(lexema):
    estado14 = 0 
    estadofinal14 = [1]
    for caracter in lexema :
        if estado14 == 0 and caracter ==',':
            estado14 = 1  
        else: 
            estado14 = -1
            break
    if estado14 == -1:
        return estadotrampa
    if estado14 in estadofinal14 :
        return estadofinal 
    else:
        return estadonofinal
#token 14 chequeado 
# token 15 para la palanra reservada (;)
def afdtoken15(lexema):
    estado15 = 0 
    estadofinal15 =[1]
    for caracter in lexema :
        if estado15 == 0 and caracter ==';':
            estado15 = 1 
        else:
            estado15 = -1 
            break
    if estado15 == -1: 
        return estadotrampa 
    if estado15 in estadofinal15 : 
        return estadofinal 
    else:
        return estadonofinal 
##   chequeado token 15     
# ahora token 16 para operacion relacion (><>=,<=)!!!!!
def afdtoken16(lexema):
    estado16 = 0
    estadofinal16 = [1, 2, 3, 4]  # Estados finales válidos

    for caracter in lexema:
        if estado16 == 0 and caracter == '>':   # estado 1 para el caracter >
                estado16 = 1
        elif estado16 == 0 and caracter == '<' : # estado 2 para el caracter <
                estado16 = 2 
        elif estado16 == 1 and caracter == '=' : # estado 3 para el caracter <=
             estado16 = 3
        elif estado16 == 2 and caracter == '=' : # estado 4 para el caracetr >=
            estado16 = 4
        else:
            estado16 = -1  # cualquier otro caracter hace que el adf se mande a un estado trampa py
            break    
    if estado16 == -1:
       return estadotrampa

    if estado16 in estadofinal16:
        return estadofinal
    else:
        return estadonofinal
    ##   chequeado fue una paja hacerlo 
# adf para token 17 num 
def afdtoken18(lexema):
    estado18 = 0
    estadofinal18 = [1]
    for caracter in lexema:
        if estado18 == 0 and caracter.isdigit():
            estado18 = 1
        elif estado18 == 1:
            if not caracter.isdigit():
                estado18 = -1
        else:
            estado18 = -1
            break
    if estado18 == -1:
        return estadotrampa
    if estado18 in estadofinal18:
        return estadofinal
    else:
        return estadonofinal

def afdtoken19(lexema):    # este usa la misma estrutuctura que el adf anterior primero se verifica que el primer caracter sea letra p _ y despues verifica que si los demas caracteres estan en las palabras permitidas para que sea un ide
    estado19 = 0
    estadofinal19 = [1]
    caracteresValidos = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for caracter in lexema:
        if estado19 == 0:
            if caracter.isalpha() or caracter == "_":
                estado19 = 1
            else:
                estado19 = -1  # Estado de error
                break
        elif estado19 == 1:
            if caracter not in caracteresValidos:
                estado19 = -1  # Estado de error
                break
    if estado19 == -1 :
        return estadotrampa
    if estado19 in estadofinal19:
        return estadofinal
    else:
        return estadonofinal
  
##   >>> adftoken19, con esto todos los automatas ya estan chequeados y corregidos 
'estado_final'



posibles_tokens = [("ENTONCES", afdtoken1),("SINO",afdtoken2),("FINSI",afdtoken3),("REPETIR",afdtoken4),("HASTA",afdtoken5),("SI",afdtoken6),("+",afdtoken7),("*",afdtoken8),("LEER",afdtoken9),("MOSTRAR",afdtoken10),("FUNC",afdtoken11),("FINFUNC",afdtoken12),("=",afdtoken13),(",",afdtoken14),(";",afdtoken15),(">,<,<=,>=",afdtoken16),("NUMERO",afdtoken18),("ID",afdtoken19)]




def lexer(codigo):
    tokens = []
    posicion = 0
    while posicion < len(codigo) :
        while codigo[posicion].isspace():
            posicion = posicion +1

        comienzo_lexema = posicion 
        tokens_posibles = []
        tokens_posibles_mas_un_caracter = []
        lexema = ""
        todos_en_estado_trampa = False

        while not todos_en_estado_trampa and posicion<len(codigo)+1:
            
            todos_en_estado_trampa = True
            lexema = codigo[comienzo_lexema:posicion +1]
            tokens_posibles = tokens_posibles_mas_un_caracter
            tokens_posibles_mas_un_caracter = []

            for (un_tipo_de_token, afd) in posibles_tokens:
                simulacion_afd = afd(lexema)
                if simulacion_afd == estadofinal:
                    tokens_posibles_mas_un_caracter.append(un_tipo_de_token)
                    todos_en_estado_trampa = False
                elif simulacion_afd == estadonofinal:
                    todos_en_estado_trampa = False

            posicion = posicion +1

        if len(tokens_posibles) == 0:
            print("ERROR:TOKEN DESCONOCIDO")
        
        posicion=posicion-1 

        un_tipo_de_token = tokens_posibles[0]
        token = (un_tipo_de_token, codigo[comienzo_lexema:posicion])
        tokens.append(token)
    return tokens


def analizar_lexico_desde_consola():
    codigo_fuente = input("Ingrese el código fuente: ")
    tokens = lexer(codigo_fuente)
    for token in tokens:
        print(token)

analizar_lexico_desde_consola()
input("Gracias por ver")

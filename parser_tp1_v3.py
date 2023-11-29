from Lexer_tp import *
VN = [ "Program","ListSentencia","ListSentenciaP","Sentencia","SentSi","SentenciaSiP","SentRepetir","SentAsignar","SentLeer",
"SentMostrar","SentFunc","Proc","ListPar","ListParP","Expresion","ExpresionP",
"Expresion2","Expresion2P","Termino","TerminoP","Factor"]

VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTRAR", "FUNC", "FINFUNC", "=" , ";","(",")", "OPrel", "NUMERO", "ID"]
#como nota, al todavia no saber si hay que agregarle al lexer los parentesis, los dejo como nota

tabla ={
    "Program":{
        "SI": ["ListSentencia"],
        "REPETIR":["ListSentencia"],
        "LEER":["ListSentencia"],
        "FUNC":["ListSentencia"],
        "MOSTRAR":["ListSentencia"],
        "ID":["ListSentencia"]
    }, 
    "ListSentencia":{
        "SI": ["Sentencia","ListSentenciaP"],
        "REPETIR":["Sentencia","ListSentenciaP"],
        "LEER":["Sentencia","ListSentenciaP"],
        "FUNC":["Sentencia","ListSentenciaP"],
        "MOSTRAR":["Sentencia","ListSentenciaP"],
        "ID":["Sentencia","ListSentenciaP"]
    },
    "ListSentenciaP":{
        ";":[";","Sentencia","ListSentenciaP"],
        "#":[],
        "SINO":[],
        "FINSI":[],
        "HASTA":[],
        "FINFUNC":[]
    },
    "Sentencia":{
        "SI":["SentSi"],
        "REPETIR":["SentRepetir"],
        "LEER":["SentLeer"],
        "FUNC":["SentFunc"],
        "ID":["SentAsignar"],
        "MOSTRAR":["SentMostrar"]   
    },

    "SentSi":{
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
    "SentLeer":{
        "LEER":["LEER","ID"]

    },
    "SentMostrar":{
        "MOSTRAR":["MOSTRAR","Expresion"]
    },
    "SentFunc":{
        "FUNC":["FUNC","Proc","FINFUNC"]
    },
    "Proc":{
        "ID":["ID","(","ListaPar",")", "ListSentencia"]
    },
    "ListaPar":{
        "ID":["ID","ListaParP"]
    },
    "ListaParP":{
        ";":[";","ID","ListaParP"],
        ")":[]
    },
    "Expresion":{
        "(": ['Expresion2','ExpresionP'],
        "NUMERO":["Expresion2","ExpresionP"],
        "ID":["Expresion2","ExpresionP"]
    },
    "ExpresionP":{
        "OPrel":["OPrel","Expresion2"],
        ")":[],
        ";":[],
        "#":[],
        "FINFUNC":[],
        "FINSI":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Expresion2":{
        "(": ['Termino', 'Expresion2P'],
        "NUMERO":["Termino","Expresion2P"],
        "ID":["Termino","Expresion2P"]
    },
    "Expresion2P":{
        "+":["+","Termino","Expresion2P"],
        "OPrel":[],
        ")":[],
        "#":[],
        "FINSI":[],
        ";":[],
        "FINFUC":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Termino":{
        "(": ['Factor', 'TerminoP'],
        "NUMERO":["Factor","TerminoP"],
        "ID":["Factor","TerminoP"]
    },
    "TerminoP":{
        "*":["*","Factor","TerminoP"],
        "+":[],
        "OPrel":[],
        ")":[],
        "#":[],
        ";":[],
        "FINFUNC":[],
        "FINSI":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Factor":{
        "(":["(","Expresion",")"],
        "NUMERO":["NUMERO"],
        "ID":["ID"]
    }
}
def parser(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
    def pni(no_terminal):
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual in tabla[no_terminal].keys():
            cuerpo_produccion=tabla[no_terminal][caracter_actual]
            print(caracter_actual,'   ',cuerpo_produccion)
            procesar(cuerpo_produccion)
        else:
            datos_locales['error'] = True
                
    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            #lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != '#' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()

#print(lexer("mostrar"))
#print(parser(lexer("si 5>5 entonces mostrar (x+5 ) finsi")))

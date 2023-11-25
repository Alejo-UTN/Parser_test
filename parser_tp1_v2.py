from Lexer_tp import *
VN = [ "Program","ListSentencia","ListSentenciaP","SentSi","SentenciaSiP","SentRepetir","SentAsignar","SentLeer",
"SentMostar","SentFun","Proc","ListPar","ListParP","Expresion","ExpresionP",
"Expresion2","Expresion2P","Termino","TerminoP","Factor"]

VT = ["ENTONCES", "SINO", "FINSI", "REPETIR", "HASTA", "SI", "+", "*", "LEER", "MOSTRAR", "FUN", "FINFUC", "=" , ";", ">,<,<=,>="#este seria op rel , y faltan "()" para los parentesis
      , "NUMERO", "ID"]
#como nota, al todavia no saber si hay que agregarle al lexer los parentesis, los dejo como nota

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
        "ID":["ID",#"(",
              "ListaPar",#")"
              "ListSentencia"]
    },
    "ListaPar":{
        "ID":["ID","ListaParP"]
    },
    "ListaParP":{
        ";":[";","ID","ListaParP"],
        #")":[]
    },
    "Expresion":{
        # "(": ['Expresion2','ExpresionP'],
        "NUMERO":["Expresion2","ExpresionP"],
        "ID":["Expresion2","ExpresionP"]
    },
    "ExpresionP":{
        ">,<,>=,<=":[">,<,>=,<=","Expresion2"],
        # ")":[],
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
        #"(": ['Termino', 'Expresion2P'],
        "NUMERO":["Termino","Expresion2P"],
        "ID":["Termino","Expresion2P"]
    },
    "Expresion2P":{
        "+":["+","Termino","Expresion2P"],
        ">,<,>=,<=":[],
        #aca va ")":[],
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
        # "(": ['Factor', 'TerminoP'],
        "NUMERO":["Factor","TerminoP"],
        "ID":["FACTOR","TerminoP"]
    },
    "TerminoP":{
        "*":["*","Factor","TerminoP"],
        "+":[],
        ">,<,>=,<=":[],
        "=":[],
        #aca va ")":[],
        "#":[],
        ";":[],
        "FINFUC":[],
        "FINFUC":[],
        "SINO":[],
        "HASTA":[],
        "ENTONCES":[]
    },
    "Factor":{
        # ")":["(","Expresion",")"],
        "NUMERO":["NUMERO"],
        "ID":["ID"]
    }
}

#AIUDAAAAAAAAAAAAA




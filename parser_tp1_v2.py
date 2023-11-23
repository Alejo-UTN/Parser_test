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
        ",":[",","Sentencia","ListSentenciaP"],
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
        ",":[],
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
        ",":[],
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
        ",":[],
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
#AIUDAAAAAAAAAAAAA




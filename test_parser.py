from Lexer_tp.py import lexer
from parser_tp1.py import parser

cadenaPrueba = [
  " SI var < var  ENTONCES FUN , SINO FUN ",
  " MOSTRAR var",
  " LEER var",
  " MOSTRAR x + 9",
  " ID = ID ",
  " REPETIR FUN 2+2 HASTA 4 "
  "
  
]
i = 1
for ejemplo in cadenaPrueba:
  print ("=============Cadena N°", i, "=============")
  parser(traduccionParser(lexer(ejemplo)))
  i += 1

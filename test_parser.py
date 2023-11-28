from Lexer_tp import lexer
from Parser_tp1_v2 import traduccionParser, parser

cadenasEjemplo = [
    "L",
    "MOSTRAR (5)"
]

i = 1
for ejemplo in cadenaPrueba:
  print ("=============Cadena N°", i, "=============")
  parser(traduccionParser(lexer(ejemplo)))
  i += 1

from Lexer_tp import lexer
from Parser_tp1_v2 import traduccionParser, parser

# Pruebas:
parser(traduccionParser(lexer("leer var")))
parser(traduccionParser(lexer("aux equal 5")))
parser(traduccionParser(lexer("func aux (aux2) leer aux3 finfunc")))
parser(traduccionParser(lexer("aux equal 9")))
parser(traduccionParser(lexer("mostrar 5")))
parser(traduccionParser(lexer("repetir mostrar 3 hasta aux3")))
parser(traduccionParser(lexer("si 5>5 entonces mostrar x+6 finsi")))
parser(traduccionParser(lexer("mostrar x+3")))
parser(traduccionParser(lexer("func rest(n1; n2) x equal n1 - n2; mostrar x finfunc")))
parser(traduccionParser(lexer("mostrar x + 5")))

i = 1
for ejemplo in cadenaPrueba:
  print ("=============Cadena N°", i, "=============")
  parser(traduccionParser(lexer(ejemplo)))
  i += 1

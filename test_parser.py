from Lexer_tp.py import lexer
from parser_tp1.py import parser

cadenaPrueba = [
  "






]
i = 1
for ejemplo in cadenaPrueba:
  print ("=============Cadena N°", i, "=============")
  parser(traduccionParser(lexer(ejemplo)))
  i += 1

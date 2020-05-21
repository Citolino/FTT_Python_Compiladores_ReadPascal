#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Analizador import Analizador

def load_buffer():
      arq = open('p1.pas', 'r')
      text = arq.readline()

      buffer = []
      cont = 1

      while text != "":
          buffer.append(text)
          text = arq.readline()
          cont += 1

          if cont == 10 or text == '':
              buf = ''.join(buffer)
              cont = 1
              yield buf

              buffer = []

      arq.close()





Analisador = Analizador()


token = []
lexeme = []
row = []
column = []


for i in load_buffer():
    t, lex, lin, col = Analisador.tokenize(i)
    token += t
    lexeme += lex
    row += lin
    column += col


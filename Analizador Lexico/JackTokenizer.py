#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''

class JackTocknizer:

    def __init__(self):
        #  arquivo(.jack) com o script a ser compitalado
        self.file_script_input = "script.jack"

    def isLetter (self, string):
        letter = "[a-z][A-Z]" # obs: definir regex ainda
        if string in letter:
            return True
        return False

     # Identifica se a entrada é um digito
    def isDigit (self, string):
        digit = '0123456789'
        if string in digit:
            return True
        return False

     # Identifica se a entrada é um operador
    def isOperator(self, byte_in):
        operators = '. + - * / ++ -- == != > >= < <= && || ='.split()
        if byte_in in operators:
            return True
        return False

    # Identifica se a entrada é um simbolo
    def isSymbol(self, string):
        symbols = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~'''
        if(string in symbols):
            return True
        return False


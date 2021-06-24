#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''
#Suporte para expressões regulares
import re

class JackTockenizer:

    def __init__(self, input_code):
        #  arquivo(.jack) com o script a ser compitalado
        self.file_script_input = "main.jack"
        # Transforma o código em uma lista de tokens
        self.current_token_index = 0
        self.tokens = []
        clean_code = JackTockenizer.clean_code(input_code)
        for line in clean_code:
            self.tokens.extend(JackTockenizer.handle_line(line))
        
        self.total_tokens = len(self.tokens)

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
    
    @staticmethod
    def clean_code(input_code):
        # Remove comentários e linha adicionais do código de entrada
        lines = []
        comment_on = False
        for line in input_code:
            line = line.strip()
            if line.startswith('/*') and (not line.endswith('*/')):
                comment_on = True
            
            if not comment_on:
                lines.append(line)

            if line.startswith('*/') or line.endswith('*/'):
                comment_on = False

        lines = [line.split('//')[0].strip() for line in lines 
                 if JackTockenizer.is_valid(line)]
        return lines

    @staticmethod
    def is_valid(line):
        # Verifica se é uma linha de código Jack válida. 
        return line and (not line.startswith('//')) and (
            not line.startswith('/*'))

    @staticmethod
    def handle_line(line):
        # Converte uma linha de código Jack em uma lista de tokens. 
        line = line.strip()
        ret = []
        if '"' in line:
            match = re.search(r"(\".*?\")", line)
            ret.extend(JackTockenizer.handle_line(match.string[:match.start()]))
            ret.append(match.string[match.start():match.end() - 1])
            ret.extend(JackTockenizer.handle_line(match.string[match.end():]))
        else:
            for candidate in line.split():
                ret.extend(JackTockenizer.handle_token_candidate(candidate))
        return ret

    @staticmethod
    def handle_token_candidate(candidate):
        # Manipula uma string que pode ser um possível token.
        # Pode ser múltiplos tokens
        # Retorna uma lista de tokens

        if not candidate:
            return []
        ret = []
        match = re.search(
            r"([\&\|\(\)<=\+\-\*>\\/.;,\[\]}{~])", candidate.strip()
        )
        if match is not None:
            ret.extend(JackTockenizer.handle_token_candidate(
                match.string[:match.start()]
            ))
            ret.append(match.string[match.start()])
            ret.extend(JackTockenizer.handle_token_candidate(
                match.string[match.end():]
            ))
        else:
            ret.append(candidate)

        return ret

# Chamando o arquivo main.jack e imprimindo os tokens enumerados.  
if __name__ == "__main__":
    with open('main.jack', 'r') as f:
        TEST_LINES = f.readlines()
    TOKENIZER = JackTockenizer(TEST_LINES)
    for i, tk in enumerate(TOKENIZER.tokens):
        print(i, tk)
    print('-----------------')


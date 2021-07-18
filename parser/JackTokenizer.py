#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''
#Suporte para expressões regulares
import re

class JackTokenizer:

    def __init__(self, raw_code):
        #  arquivo(.jack) com o script a ser compilado
        self.file_script_input = "Square.jack"
        # Transforma o código em uma lista de tokens
        self.current_token_index = 0
        self.tokens = []
        clean_code = JackTokenizer.clean_code(raw_code)
        for line in clean_code:
            self.tokens.extend(JackTokenizer.handle_line(line))
        
        self.total_tokens = len(self.tokens)

    def isString (token):
        if token.startswith('"'):
            return True
        return False

    # Identifica se a entrada é um digito
    def isDigit (token):
        if token.isdigit():
            return True
        return False

    # Identifica se a entrada é um operador
    def isOperator(byte_in):
        operators = '. + - * / ++ -- == != > >= < <= && || ='.split()
        if byte_in in operators:
            return True
        return False

    # Identifica se a entrada é um simbolo
    def isSymbol(token):
        symbols = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~'''
        if(token in symbols):
            return True
        return False

    # Identifica se a entrada é uma Palavra chave
    def isKeyword (token):
        digit = ('class', 'constructor', 'function', 'method', 
                'field', 'static', 'var', 'int', 'char', 'if',
                'boolean', 'void', 'true', 'false', 'null',
                'this', 'let', 'do', 'return', 'else', 'while')
        if token in digit:
            return True
        return False

    # Identifica se a entrada é uma Palavra chave
    def isIdentifier (token):
        if (not token[0].isdigit()):
            return True
        return False

    def keyWord(token):
        """Returns the keyword which is the current token."""
        if (JackTokenizer.isKeyword(token)):
            return token
        
    def symbol(token):
        """Returns the character which is the current token."""
        if (JackTokenizer.isSymbol(token)):
            return token

        
    def identifier(token):
        """Returns the identifier which is the current token."""
        if (JackTokenizer.isIdentifier(token)):
            return token

        
    def intVal(token):
        """Returns the integer value of the current token."""
        if (JackTokenizer.isDigit(token)):
            return token


    def stringVal(token):
        """Returns the string value of the current token, without the double quotes."""
        if (JackTokenizer.isString(token)):
            #skip quotes in constant
            return token[1:-1]

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
                 if JackTokenizer.is_valid(line)]
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
            ret.extend(JackTokenizer.handle_line(match.string[:match.start()]))
            ret.append(match.string[match.start():match.end() - 1])
            ret.extend(JackTokenizer.handle_line(match.string[match.end():]))
        else:
            for candidate in line.split():
                ret.extend(JackTokenizer.handle_token_candidate(candidate))
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
            ret.extend(JackTokenizer.handle_token_candidate(
                match.string[:match.start()]
            ))
            ret.append(match.string[match.start()])
            ret.extend(JackTokenizer.handle_token_candidate(
                match.string[match.end():]
            ))
        else:
            ret.append(candidate)

        return ret

    def token_type(token):
        # Retorna o tipo do token
        # Tipos: KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST

        symbol_type = None
        if (JackTokenizer.isKeyword(token)):
            #symbol_type = 'KEYWORD'
            symbol_type =  "<keyword> %s </keyword>" % token
        elif (JackTokenizer.isSymbol(token)):
            #symbol_type = 'SYMBOL'
            if token == "<":
                symbol_type = "<symbol> &lt; </symbol>"
            elif token == ">":
                symbol_type = "<symbol> &gt; </symbol>"
            elif token == "&":
                symbol_type = "<symbol> &amp; </symbol>"
            else:
                symbol_type = "<symbol> %s </symbol>" % token

        elif (JackTokenizer.isDigit(token)):
            #symbol_type = 'INT_CONST'
            symbol_type = "<integerConstant> %s </integerConstant>" % token
        elif (JackTokenizer.isString(token)):
            #symbol_type = 'STRING_CONST'
            symbol_type = "<stringConstant> %s </stringConstant>" % token[1:-1]
        elif (JackTokenizer.isIdentifier(token)):
            #symbol_type = 'IDENTIFIER'
            symbol_type  = "<identifier> %s </identifier>" % token
        elif (JackTokenizer.isOperator(token)):
            symbol_type = 'OPERATOR'
        else:
            raise SyntaxError('Token Inválido: {}'.format(token))
        return symbol_type 

    
    def advance(self):
        """Advance the token pointer by one. Throws error if no more tokens."""

        if self.has_more_tokens():
            self.current_token_index += 1
        else:
            raise IndexError('No more tokens.')
    
    def has_more_tokens(self):
        """Check if there are more tokens available."""
        return self.current_token_index < (self.total_tokens - 1)

    @property
    def curr_token(self):
        """Return the current token. 
        
        Returns:
            str: Current token
        """

        return self.tokens[self.current_token_index]
    
    @property
    def next_token(self):
        """Returns next token if there is one.
        """

        if self.has_more_tokens():
            return self.tokens[self.current_token_index + 1]
    
    @property
    def prev_token(self):
        """Returns the previous token, if there is one. 
        """

        if self.current_token_index > 0:
            return self.tokens[self.current_token_index - 1]


# Chamando o arquivo main.jack e imprimindo os tokens enumerados.  
if __name__ == "__main__":
    with open('main.jack', 'r') as f:
        TEST_LINES = f.readlines()
    TOKENIZER = JackTokenizer(TEST_LINES)
    for i, token in enumerate(TOKENIZER.tokens):
        print(i, token)
        print(JackTokenizer.token_type(token))
    print('-----------------')
from JackTokenizer import JackTokenizer

class JackAnalyser:
    
    def __init__(self, input_stream, output_file):
        self.tokenizer = input_stream
        self.outfile = output_file

    def CompileClass(self):

        self.xmlout = open(self.outfile, "w")
        
        #Compila uma classe completa.
        self._output("<class>")

        #Esperado class
        if self.tokenizer.curr_token != "class":
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                            
        self.tokenizer.advance()
        #Esperado o nome da classe

        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        #Esperado {
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "{":
            return False
            
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        
        #verifica se há alguma declaração de campo var
        
        while JackTokenizer.keyWord(self.tokenizer.curr_token) in ("static", "field"):
            self.CompileClassVarDec()
       
        while JackTokenizer.keyWord(self.tokenizer.curr_token) in ("constructor", "function", "method"):     
            self.CompileSubroutine()

        #Esperado }
        #if JackTokenizer.symbol(self.tokenizer.curr_token) != "}":
            #return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self._output("</class>")
        self.xmlout.close()
        
    def CompileClassVarDec(self):
        # Compila uma declaração estática ou uma declaração de campo.
        self._output("<classVarDec>")
        if JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("static", "field"):
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

        self.tokenizer.advance()
        #Esperado var type
        if not JackTokenizer.identifier(self.tokenizer.curr_token) and not JackTokenizer.keyWord(self.tokenizer.curr_token) in ("int", "char", "boolean"):
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                    
        self.tokenizer.advance()
        #Esperado var name
        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                    
        self.tokenizer.advance()

        #verificar, varname
        while JackTokenizer.symbol(self.tokenizer.curr_token) == ",":
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            #Esperado identifier
            if not JackTokenizer.identifier(self.tokenizer.curr_token):
                return False
            
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            self.tokenizer.advance()
                
        if not JackTokenizer.symbol(self.tokenizer.curr_token) == ";":
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                    
        self.tokenizer.advance()
        self._output("</classVarDec>")              
        
    def CompileSubroutine(self):
        """Compiles a complete method, function, or constructor."""
        self._output("<subroutineDec>")
        #Esperando class ctor, function or method
        if JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("constructor", "function", "method"):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        
        #Esperando func return type
        if not JackTokenizer.identifier(self.tokenizer.curr_token) and JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("void", "int", "char", "boolean"):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        #Esperando function name
        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        #Esperando ( symbol
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "(":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        #check for parameter list
        self._output("<parameterList>")
        self.CompileParameterList()
        self._output("</parameterList>")
        
        #Esperando ) symbol
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
            return False
            
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        self._output("<subroutineBody>")
        self.tokenizer.advance()
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "{":
            return False
            
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        #checking for var declarations
        self.tokenizer.advance()
        while JackTokenizer.keyWord(self.tokenizer.curr_token) == "var":
            self.CompileVarDec()

        #check for statements
        while JackTokenizer.keyWord(self.tokenizer.curr_token) in ("let", "if", "while", "do", "return"):
            self.CompileStatements() 
        
        #Esperando } to end subroutine
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "}":
            return False
            
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        self.tokenizer.advance()
        self._output("</subroutineBody>")
        self._output("</subroutineDec>")
        
    def CompileParameterList(self):
        
        #Compila uma lista de parâmetros (possivelmente vazia), sem incluir '()'.

        if JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("void", "int", "char", "boolean") and not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        #Esperando var name
        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        while JackTokenizer.symbol(self.tokenizer.curr_token) == ",":
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

            self.tokenizer.advance()
            #Esperado var type
            if JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("int", "char", "boolean") and not JackTokenizer.identifier(self.tokenizer.curr_token):
                return False

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            #Esperado var name
            if not JackTokenizer.identifier(self.tokenizer.curr_token):
                return False

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                            
            self.tokenizer.advance()
        
    def CompileVarDec(self):
        #Compila uma declaração var.
        self._output("<varDec>")
        #Esperando var keyword
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "var":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #Esperado var type
        if JackTokenizer.keyWord(self.tokenizer.curr_token) not in ("int", "char", "boolean") and not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #Esperado var name
        if self.tokenizer.tokenType() != JackTokenizer.Identifier:
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        while JackTokenizer.symbol(self.tokenizer.curr_token) == ",":
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            #Esperado var name
            if not JackTokenizer.identifier(self.tokenizer.curr_token):
                return False
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            
        #Esperado ;
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ";":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self._output("</varDec>")
        
    def CompileStatements(self):
        
        #Compila uma sequência de instruções, não incluindo '{}'.

        self._output("<statements>")
        while JackTokenizer.keyWord(self.tokenizer.curr_token) in ("let", "if", "while", "do", "return"):
            if JackTokenizer.keyWord(self.tokenizer.curr_token) == "let":
                self.CompileLet()
            elif JackTokenizer.keyWord(self.tokenizer.curr_token) == "if":
                self.CompileIf()
            elif JackTokenizer.keyWord(self.tokenizer.curr_token) == "while":
                self.CompileWhile()
            elif JackTokenizer.keyWord(self.tokenizer.curr_token) == "do":
                self.CompileDo()
            elif JackTokenizer.keyWord(self.tokenizer.curr_token) == "return":
                self.CompileReturn()
                #TODO is this right?
                break

        self._output("</statements>")

    def CompileDo(self):
        #Compila uma instrução do.
        
        self._output("<doStatement>")
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "do":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #Esperando subroutine call
        self.CompileSubroutineCall()

        #Esperando ;
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ";":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self._output("</doStatement>")
                
    def CompileLet(self):
        # Compila uma instrução let
        self._output("<letStatement>")
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "let":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #Esperado identifier
        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        
        if JackTokenizer.symbol(self.tokenizer.curr_token) == "[":
            #array access
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            self.tokenizer.advance()
            #Esperado expressão 
            self.CompileExpression()
            
            #Esperado closing ]
            if JackTokenizer.symbol(self.tokenizer.curr_token) != "]":
                return False
            
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()        
        
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "=":
            #Esperado = 
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #Esperando expressão
        self.CompileExpression()

        if JackTokenizer.symbol(self.tokenizer.curr_token) != ";":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self._output("</letStatement>")
            
    def CompileWhile(self):
        #Compila uma instrução while.
        self._output("<whileStatement>")
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "while":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #esperando (
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "(":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self.CompileExpression()
        
        #esperando )
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        #esperando {
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "{":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self.CompileStatements()
        
        #Esperado }
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "}":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                
        self.tokenizer.advance()
        self._output("</whileStatement>")

    def CompileReturn(self):
        #Compila uma instrução de retorno.
        self._output("<returnStatement>")
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "return":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()

        if JackTokenizer.symbol(self.tokenizer.curr_token) != ";":
            #Esperando expressão. 
            self.CompileExpression()
        
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ";":
            #Esperando ;
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        self._output("</returnStatement>")
        
    def CompileIf(self):
        #Compila uma instrução if, possível com uma cláusula else à direita.
        self._output("<ifStatement>")
        
        if JackTokenizer.keyWord(self.tokenizer.curr_token) != "if":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        
        #Esperado (
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "(":
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()
        self.CompileExpression()
        
        #Esperado )
        if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                        
        self.tokenizer.advance()
        #Esperado {
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "{":
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

        self.tokenizer.advance()
        
        self.CompileStatements()
        
        #Esperado }
        if JackTokenizer.symbol(self.tokenizer.curr_token) != "}":
            return False

        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        self.tokenizer.advance()
        
        if JackTokenizer.keyWord(self.tokenizer.curr_token) == "else":
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            self.CompileStatements()
            
            if JackTokenizer.symbol(self.tokenizer.curr_token) != "}":
                return False

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            
        self._output("</ifStatement>")
        
    def CompileExpression(self):
        #Compila uma expressão.
        self._output("<expression>")
        self.CompileTerm()
        
        #(op term)*
        while JackTokenizer.symbol(self.tokenizer.curr_token) in ("+", "-", "*", "/", "&", "|", "<", ">", "="):
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            self.tokenizer.advance()
            self.CompileTerm()

        self._output("</expression>")
        
    def CompileTerm(self):
        #Compila um termo
        self._output("<term>")
        thisisterm = False
        
        if self.tokenizer.intVal(): #integer constante
            thisisterm = True
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        elif self.tokenizer.stringVal(): #string constante
            thisisterm = True
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
        elif JackTokenizer.keyWord(self.tokenizer.curr_token): #keyword constante
            keyterm = JackTokenizer.keyWord(self.tokenizer.curr_token)

            #Pode ser true, false, null, this
            if keyterm not in ("true", "false", "null", "this"):
                return False
                
            thisisterm = True
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                        
        elif JackTokenizer.symbol(self.tokenizer.curr_token) == "(":
            #verificar (expressão)
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

            self.tokenizer.advance()
            self.CompileExpression()

            if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
                return False

            thisisterm = True                
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

        elif JackTokenizer.symbol(self.tokenizer.curr_token) in ("-", "~"):
            #Esperado termo
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            self.tokenizer.advance()

            self.CompileTerm()
            
        elif JackTokenizer.identifier(self.tokenizer.curr_token): #nome variável
            # Verificando sinais de acesso à matriz ou sinais de chamada de sub-rotina
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            self.tokenizer.advance()

            if JackTokenizer.symbol(self.tokenizer.curr_token) == "[":
                #acesso ao array
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                self.tokenizer.advance()
                self.CompileExpression()
                
                if JackTokenizer.symbol(self.tokenizer.curr_token) != "]":
                    return False

                thisisterm = True
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                
            elif JackTokenizer.symbol(self.tokenizer.curr_token) == "(":
                #chamada de sub-rotina direta
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

                self.tokenizer.advance()
                self.CompileExpressionList()
                self.tokenizer.advance()

                #Esperado ending )
                if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
                    return False

                thisisterm = True
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                
            elif JackTokenizer.symbol(self.tokenizer.curr_token) == ".":
                #var chamada de sub-rotina
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                
                self.tokenizer.advance()
                #Esperando identifier
                if not JackTokenizer.identifier(self.tokenizer.curr_token):
                    return False
                
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                    
                self.tokenizer.advance()
                #Esperando (
                if JackTokenizer.symbol(self.tokenizer.curr_token) != "(":
                    return False

                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                self.tokenizer.advance()
                
                self.CompileExpressionList()

                #Esperando closing )
                if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
                    return False

                thisisterm = True
                self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
                
        if thisisterm == True:
            self.tokenizer.advance()
            
        self._output("</term>")
        
    def CompileExpressionList(self):
        """Compiles a (possibly empty) comma-separated list of expressions."""
        self._output("<expressionList>")
        #expressão?
        self.CompileExpression()
        
        #(, expressão)*
        while JackTokenizer.symbol(self.tokenizer.curr_token) == ",":
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            self.CompileExpression()
            
        self._output("</expressionList>")
        
    def CompileSubroutineCall(self):
        #Compile uma chamada de sub-rotina.
        if not JackTokenizer.identifier(self.tokenizer.curr_token):
            return False
        
        self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        
        self.tokenizer.advance()

        if JackTokenizer.symbol(self.tokenizer.curr_token) == "(":
            #chamada de função direta

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

            self.tokenizer.advance()
            self.CompileExpressionList()

            #Esperado ending )
            if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
                return False

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))

        elif JackTokenizer.symbol(self.tokenizer.curr_token) == ".":
            #chamada de método

            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            #Esperando identifier para nome do método
            if not JackTokenizer.identifier(self.tokenizer.curr_token):
                return False
            
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            #Esperando (
            if JackTokenizer.symbol(self.tokenizer.curr_token) != "(":
                return False
            
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
            
            self.tokenizer.advance()
            self.CompileExpressionList()
            
            if JackTokenizer.symbol(self.tokenizer.curr_token) != ")":
                return False 
            self._output(JackTokenizer.token_type(self.tokenizer.curr_token))
        else:
            return False
        
        self.tokenizer.advance()
        
    def _output(self, strtowrite):
        #Grava a string no arquivo de saída xml. 
        self.xmlout.write(strtowrite)
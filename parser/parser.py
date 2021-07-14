

class Parser():

    def __init__(self):

        # recebe o arquivo com os tokens 
        self.file_input_lexer = ""
        self.file_output_parser = ""

        self.file_lexer = open(self.file_input_lexer, "r")
        self.tokens = self.file_lexer.readlines()

    
    def compileClass(self):

        if( 'class' in self.tokens): #.....
           
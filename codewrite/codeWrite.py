class Codewrite:

    def __init__(self, input_stream):
        self.input_stream = input_stream
        # corrigir saida ... .vm
        self.outfile = open(self.outfile,"w") 

        self.kindDict = {
            "POINTER" : "pointer",
            "THAT"    : "that",
            "THIS"    : "this",
            "STATIC"  : "static",
            "TEMP"    : "temp",
            "ARG"     : "argument",
            "LOCAL"   : "local",
            "CONST"   : "constant",
            "FIELD"   : "this"
        }
        # return ...
    
    def push(self, kind, index):
        receive_kind = self.kindDict.get(kind)

        if(receive_kind != None):
            self._output("push {} {}".format(receive_kind,index),file=self.outfile)
            
        else:
            self._output("ERROR push")
        
    def pop(self, kind, index):
        receive_kind = self.kindDict.get(kind)

        if(receive_kind != None):
            self._output("pop {} {}".format(receive_kind,index),file=self.outfile)
            
        else:
            self._output("ERROR pop")

    def ifgotoWrite(self, label):
        self._output("if-goto {}".format(label),file=self.outfile)

    def gotoWrite(self, label):
        self._output("goto {}".format(label),file=self.outfile)

    def labelWrite(self, label):
        self._output("label {}".format(label),file=self.outfile)
        
    def callWrite(self, name, arg_len):
        self._output("call {} {}".format(name, arg_len),file=self.outfile)
        
    def returnWrite(self):
        self._output("return",file=self.outfile)
        
    def functionWrite(self, name, local_len):
        self._output("function {} {}".format(name,local_len),file=self.outfile)

    def expressionWrite(self, term):
        # ---------------
        return 0

    def _output(self, strtowrite):
        #Grava a string no arquivo de saída xml. 
        self.outfile.write(strtowrite)

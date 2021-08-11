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
                print("push {} {}".format(receive_kind,index),file=self.outfile)
            
            else:
                print("ERROR push")
        
        def pop(self, kind, index):
            receive_kind = self.kindDict.get(kind)

            if(receive_kind != None):
                print("pop {} {}".format(receive_kind,index),file=self.outfile)
            
            else:
                print("ERROR pop")

        def ifgotoWrite(self, label):
            print("if-goto {}".format(label),file=self.outfile)

        def gotoWrite(self, label):
            print("goto {}".format(label),file=self.outfile)

        def labelWrite(self, label):
            print("label {}".format(label),file=self.outfile)
        
        def callWrite(self, name, arg_len):
            print("call {} {}".format(name, arg_len),file=self.outfile)
        
        def returnWrite(self):
            print("return",file=self.outfile)
        
        def functionWrite(self, name, local_len):
            print("function {} {}".format(name,local_len),file=self.outfile)

        def expressionWrite(self, term):
            # ---------------
            return 0

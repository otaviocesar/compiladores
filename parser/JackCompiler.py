#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''
from JackAnalyser import JackAnalyser
from JackTokenizer import JackTokenizer

import os.path
import sys

def main():
    print('----------------- Analise Sintática ------------------------')    
    jackfilename = "SquareGame.jack"
    (jfilename, jextension) = os.path.splitext(jackfilename)
    jtokresultfilename = jfilename + ".xml"
    
    with open(jackfilename, 'r') as f:
        tk = JackTokenizer(f.readlines())
    engine = JackAnalyser(tk, jtokresultfilename)
        
    comParse = engine.CompileClass()
    if comParse == False:
        print ("Invalid parse")

    print('----------------- Arquivo Gerado com Sucesso------------------')
    
if __name__ == '__main__':
    main()


 
        
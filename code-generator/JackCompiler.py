#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort
'''
import os
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer


def main():

    print('----------------- Gerador de Código ------------------------') 
    jackfilename = "Point.jack"
    (jfilename, jextension) = os.path.splitext(jackfilename)
    jtokresultfilename = jfilename + ".vm"
    
    with open(jackfilename, 'r') as f:
        tk = JackTokenizer(f.readlines())
    engine = CompilationEngine(tk, jtokresultfilename)
    engine.compile_class()
    
    print('----------------- Arquivo Gerado com Sucesso------------------')


if __name__ == '__main__':
    main()

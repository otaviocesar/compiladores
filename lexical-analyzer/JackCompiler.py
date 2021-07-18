#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''
import JackTokenizer
import os.path
import sys

def main():
    print('----------------- Analise Léxica------------------------')
    # Chamando o arquivo main.jack e imprimindo os tokens enumerados.  
    with open('Square.jack', 'r') as f:
        TEST_LINES = f.readlines()
    TOKENIZER = JackTokenizer.JackTockenizer(TEST_LINES)

    jackfilename = "Square.jack"
    (jfilename, jextension) = os.path.splitext(jackfilename)
    jtokresultfilename = jfilename + "T.xml"
    with open(jtokresultfilename, "w") as jtokresult:
        jtokresult.write("<tokens>")

        for i, token in enumerate(TOKENIZER.tokens):
            print(i, token)
            print(JackTokenizer.JackTockenizer.token_type(token))
            jtokresult.write(JackTokenizer.JackTockenizer.token_type(token))

        jtokresult.write("</tokens>")    
    print('----------------- Arquivo Gerado com Sucesso------------------')

if __name__ == '__main__':
    main()


 
        
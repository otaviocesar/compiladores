import sys
import os.path
import translator

inputfile= sys.argv[1]
inputfile = inputfile.strip()
if os.path.isfile(inputfile)== False:
    print("Arquivo não encontrado!");
    sys.exit()
size=len(inputfile)
if inputfile[size-2:size] != "vm":
    print("Formato inválido!")
else:
    outputfile = inputfile.replace("vm","asm")
    translator.translate(inputfile, outputfile)
    
def binaryInstruction(command,label_val):
    newline=""
    if command == "add":
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "AM=M-1\n" 
        newline += "M=D+M\n" 
        newline += "@SP\n"
        newline += "M=M+1\n" 
    elif command == "sub":
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "AM=M-1\n" 
        newline += "M=M-D\n" 
        newline += "@SP\n"
        newline += "M=M+1\n" 
    elif command == "or":
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "M=D|M\n" 
    elif command == "and":
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "M=D&M\n" 
    elif command == "eq":
        label = "Alabel" + str(label_val)
        label_val += 1
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "D=M-D\n" 
        newline += "M=-1\n" 
        newline += "@eqTrue" + label + "\n" 
        newline += "D;JEQ\n"
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "M=0\n" 
        newline += "(eqTrue" + label + ")\n"
    elif command == "gt":
        label = "Alabel" + str(label_val)
        label_val += 1
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "D=M-D\n" 
        newline += "M=-1\n" 
        newline += "@gtTrue" + label + "\n" 
        newline += "D;JGT\n"
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "M=0\n" 
        newline += "(gtTrue" + label + ")\n"
    elif command == "lt":
        label = "Alabel" + str(label_val)
        label_val += 1
        newline += "@SP\n" 
        newline += "AM=M-1\n"
        newline += "D=M\n" 
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "D=M-D\n" 
        newline += "M=-1\n" 
        newline += "@ltTrue" + label + "\n" 
        newline += "D;JLT\n"
        newline += "@SP\n" 
        newline += "A=M-1\n"
        newline += "M=0\n" 
        newline += "(ltTrue" + label + ")\n" 
    else:
        newline = "Sintaxe Inválida"
    return newline, label_val
	
def unaryInstruction(command):
    newline=""
    if command == "neg":
        newline += "@SP\n" 
        newline += "A=M-1\n" 
        newline += "M=-M\n"  
    elif command == "not":
        newline += "@SP\n" 
        newline += "A=M-1\n" 
        newline += "M=!M\n" 
    else :
        newline = "Sintaxe Inválida"
    return newline

def pushPopInstruction(line):
    newline=""
    command=line.split(' ')[0]
    size=len(command)  
    if command[size-1] == '\n' :
        command=command[0:size-1]
    segment=line.split(' ')[1]
    size=len(segment)  
    if segment[size-1] == '\n' :
        segment=segment[0:size-1]
    index=line.split(' ')[2]
    size=len(index)  
    if index[size-1] == '\n' :
        index=index[0:size-1]
    if command == "push":
        if segment == "constant":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@SP\n"
            newline += "A=M\n" 
            newline += "M=D\n" 
            newline += "@SP\n" 
            newline += "M=M+1\n" 
        elif segment == "static":
            newline += "@" + index + "\n"
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n" 
            newline += "M=D\n"
            newline += "@SP\n"
            newline += "M=M+1\n"
        elif segment == "this":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@THIS\n"
            newline += "A=M+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        elif segment == "that":
            newline += "@" + index + "\n"
            newline += "D=A\n"
            newline += "@THAT\n"
            newline += "A=M+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        elif segment == "argument":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@ARG\n"
            newline += "A=M+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        elif segment == "local":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@LCL\n"
            newline += "A=M+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        elif segment == "temp":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@5\n"
            newline += "A=A+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        elif segment == "pointer":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@3\n"
            newline += "A=A+D\n" 
            newline += "D=M\n"
            newline += "@SP\n" 
            newline += "A=M\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "M=M+1\n"
        else:
            newline += "Sintaxe Inválida"
    elif command == "pop":
        if segment == "static":
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@" + index + "\n"
            newline += "M=D\n"
        elif segment == "this":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@THIS\n"
            newline += "D=M+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        elif segment == "that":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@THAT\n"
            newline += "D=M+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        elif segment == "argument":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@ARG\n"
            newline += "D=M+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        elif segment == "local":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@LCL\n"
            newline += "D=M+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        elif segment == "pointer":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@3\n"
            newline += "D=A+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        elif segment == "temp":
            newline += "@" + index + "\n" 
            newline += "D=A\n"
            newline += "@5\n"
            newline += "D=A+D\n" 
            newline += "@R13\n"
            newline += "M=D\n"
            newline += "@SP\n" 
            newline += "AM=M-1\n"
            newline += "D=M\n"
            newline += "@R13\n" 
            newline += "A=M\n"
            newline += "M=D\n"
        else:
            newline +="Sintaxe Inválida"
    else:
        newline +="Sintaxe Inválida"
    return newline
	
def translate(inputfile, outputfile):
    arith_logic_table_binary=['add', 'sub', 'eq' , 'gt' , 'lt' , 'and' , 'or' ]
    arith_logic_unary=['not', 'neg']
    label_val =0
    file_descriptor=open(inputfile, "r")
    with open(outputfile, 'w') as asm_file:
        newline= ""
        for line in file_descriptor:
            if line[0] == " ":
                line=line.strip()
                line, sep, tail = line.partition('//')
                line=line.strip()  
            if (line[:2] != "//") and (line[:2] != "/*") and (line[:2] !="/*") and (line != '\n'):
                command=line.partition(' ')[0]
                size=len(command)  
                if command[size-1] == '\n' :
                    command=command[0:size-1]
                if command == "push" or command == "pop" :
                    newline= pushPopInstruction(line)
                elif command in  arith_logic_table_binary :
                    newline, label_val= binaryInstruction(command,label_val)
                elif command in arith_logic_unary:
                    newline= unaryInstruction(command)
                else :
                    print("Sintaxe Inválida")
                    break
                if newline == "Sintaxe Inválida":
                    break
                else:
                    asm_file.write(newline + '\n')
        newline=""
        newline += "(END)\n" 
        newline += "@END\n"
        newline += "0;JMP\n"
        asm_file.write(newline + '\n')
    asm_file.close()
    file_descriptor.close()
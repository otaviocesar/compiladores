@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@eqTrueAlabel0
D;JEQ
@SP
A=M-1
M=0
(eqTrueAlabel0)

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@16
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@eqTrueAlabel1
D;JEQ
@SP
A=M-1
M=0
(eqTrueAlabel1)

@16
D=A
@SP
A=M
M=D
@SP
M=M+1

@17
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@eqTrueAlabel2
D;JEQ
@SP
A=M-1
M=0
(eqTrueAlabel2)

@892
D=A
@SP
A=M
M=D
@SP
M=M+1

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@ltTrueAlabel3
D;JLT
@SP
A=M-1
M=0
(ltTrueAlabel3)

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@892
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@ltTrueAlabel4
D;JLT
@SP
A=M-1
M=0
(ltTrueAlabel4)

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@891
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@ltTrueAlabel5
D;JLT
@SP
A=M-1
M=0
(ltTrueAlabel5)

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@gtTrueAlabel6
D;JGT
@SP
A=M-1
M=0
(gtTrueAlabel6)

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@gtTrueAlabel7
D;JGT
@SP
A=M-1
M=0
(gtTrueAlabel7)

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
D=M-D
M=-1
@gtTrueAlabel8
D;JGT
@SP
A=M-1
M=0
(gtTrueAlabel8)

@57
D=A
@SP
A=M
M=D
@SP
M=M+1

@31
D=A
@SP
A=M
M=D
@SP
M=M+1

@53
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
AM=M-1
M=D+M
@SP
M=M+1

@112
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
AM=M-1
M=M-D
@SP
M=M+1

@SP
A=M-1
M=-M

@SP
AM=M-1
D=M
@SP
A=M-1
M=D&M

@82
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP
AM=M-1
D=M
@SP
A=M-1
M=D|M

@SP
A=M-1
M=!M

(END)
@END
0;JMP


# Implementação de um Compilador


## Etapas

	1. Desenvolvimento do analisador léxico
	2. Projeto do analisador léxico e sintático
	3. Desenvolvimento do analisador sintático 
    4. Projeto do gerador de código intermediário 
	5. Desenvolvimento do gerador de código intermediário
    6. Projeto do tradutor - Parte1 
    7. Projeto do tradutor - Parte2
	

## Analisador Léxico
### Especificação da microsintaxe
-------------------
* Palavras reservadas: 

	* 'class' | 'constructor' | 'function' | 'method' | 'field' | 'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' | 'false' | 'null' | 'this' | 'let' |  do' | 'if' | 'else' | 'while' | 'return’

- Símbolos: 
	* '{' | '}' | '(' | ')' | '[' | ']' | '. ' | ', ' | '; ' | '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~'

- Inteiros: um número decimal inteiro
- Strings: "uma sequência de caracteres Unicode entre aspas dupla"
- Identificadores: uma sequência de letras, digitos e *undescore* ( '_' ) não iniciando com um dígito.

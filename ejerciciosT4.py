import sys
import ply.lex as lex
tokens = (
    #ejercicio 2
    "NUM_CONTINUOS",
    "NUM_ENTEROS",
    "PARIZ",
    "PARDER",
    #ejercicio 3
    "SUMA",
    "RESTA",
    "COMA",
    "MULTIPLICACION",
    "DIVISION",
    #ejercicio 4
    "MENOR",
    "MAYOR",
    "MENOR_IGUAL",
    "MAYOR_IGUAL",
    "IGUAL",
    "DIFERENTE",
    #ejercicio 5    
    "PRINT",
    "INT",
    "FOR",
    "WHILE",
    "SWITCH",
    "CASE",
    "IF",
    "ELSE",
    "BREAK",
    "DO",
    "ASIGNAR",
    #ejercicio 1
    "VARIABLE"
)
t_ignore = "\t"
def t_space(t):
    r"\s+"
    t.lexer.lineno += t.value.count("\n")

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(chr(27) + "[1;31m" + "\t ERROR: Illegal character" + chr(27) + "[0m")
    print("\t\tLine: " + str(t.lexer.lineno) + "\t=> " + t.value[0])
    t.lexer.skip(1)



#numeros continuos
def t_NUM_CONTINUOS(t):
    r"\d+.\d+"
    return t
def t_NUM_ENTEROS(t):
    r"\d+"
    return t   
#operadores aritmeticos
t_SUMA=r"\+"
t_PARIZ=r"\("
t_PARDER=r"\)"
t_COMA=r"\,"
t_RESTA=r"\-"
t_MULTIPLICACION=r"\*"
t_DIVISION=r"\/"
t_ASIGNAR=r"\="
#operadores relacionales
t_MENOR=r"\<"
t_MAYOR=r"\>"
t_MENOR_IGUAL=r"\<="
t_MAYOR_IGUAL=r"\>="
t_IGUAL=r"=="
t_DIFERENTE=r"!="
#palabras reservadas
def t_PRINT(t):
    r"print"
    return t

def t_FOR(t):
    r"for"
    return t

def t_WHILE(t):
    r"while"
    return t

def t_SWITCH(t):
    r"switch"
    return t

def t_CASE(t):
    r"print"
    return t

def t_IF(t):
    r"if"
    return t

def t_ELSE(t):
    r"else"
    return t

def t_BREAK(t):
    r"break"
    return t

def t_DO(t):
    r"do"
    return t

#variables
def t_VARIABLE(t):
    r"\w+(\w\d)*"
    return t

lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        script = sys.argv[1]

        scriptfile = open(script, "r")
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print(chr(27) + "[0;36m" + "INICIA ANALISIS LEXICO" + chr(27) + "[0m")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print("\t"+ str(i)+ " - "+ "Line: "+ str(tok.lineno)+ "\t"+ str(tok.type)+ "\t-->  "+ str(tok.value))
            i += 1

        print(chr(27) + "[0;36m" + "TERMINA ANALISIS LEXICO" + chr(27) + "[0m")

    else:
        print(chr(27) + "[0;31m" + "Pase el archivo de scritp DART como parametro")
        print(chr(27) + "[0;36m"+ "\t$ python ejerciciosT4.py"+ chr(27)+ "[1;31m"+ " prueba.dart"+ chr(27)+ "[0m")
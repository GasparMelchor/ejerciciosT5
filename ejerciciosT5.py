import sys
import os
import codecs
from sys import stdin
import ply.yacc as yacc
from ejerciciosT4 import tokens


VERBOSE=1
precedence = (
    ('right','IGUAL','DIFERENTE'),
    ('nonassoc','MENOR','MENOR_IGUAL'),
    ('nonassoc','MAYOR','MAYOR_IGUAL'),
    ('left','RESTA','SUMA'),
    ('left','DIVISION','MULTIPLICACION')
)
#('left','MENOR','MENOR_IGUAL'),
def p_sentencia1(p):
    '''sentencia : WHILE parentesis condicional parentesis'''
    print("sentencia while")

def p_sentencia2(p):
    '''sentencia : IF parentesis condicional parentesis'''
    print("sentencia IF")

def p_parentesis1(p):
    '''parentesis : PARIZ'''

def p_parentesis2(p):
    '''parentesis : PARDER'''

def p_asignacioin1(p):
    '''asignacion : VARIABLE ASIGNAR cantidad'''
    print("OPERACION ASIGNAR A UN NUMERO")

def p_asignacion2(p):
    '''asignacion : VARIABLE ASIGNAR operacion'''
    print("OPERACION ASIGNAR A UNA OPERACION")

def p_operacion1(p):
    '''operacion : cantidad SUMA cantidad'''
    print("OPERACION SUMA")

def p_operacio2(p):
    '''operacion : cantidad RESTA cantidad'''
    print("OPERACION RESTA")

def p_operacion3(p):
    '''operacion : cantidad MULTIPLICACION cantidad'''
    print("OPERACION MULTIPLICACION")

def p_operacion4(p):
    '''operacion : cantidad DIVISION cantidad'''
    print("OPERACION DIVISION")

def p_condicional1(p):
    '''condicional : cantidad MENOR cantidad'''
    print("condicional menor que")

def p_condicional2(p):
    '''condicional : cantidad MENOR_IGUAL cantidad'''
    print("condicional menorIGUAL que")

def p_condicional3(p):
    '''condicional : cantidad MAYOR cantidad'''
    print("condicional MAYOR que")

def p_condicional4(p):
    '''condicional : cantidad MAYOR_IGUAL cantidad'''
    print("condicional MAYOR_IGUAL que")

def p_condicional5(p):
    '''condicional : cantidad IGUAL cantidad'''
    print("condicional IGUAL que")

def p_cantidad1(p):
    '''cantidad : NUM_CONTINUOS'''
    print("CONTINUOS")

def p_cantidad2(p):
    '''cantidad : NUM_ENTEROS'''
    print("ENTEROS")

def p_cantidad3(p):
    '''cantidad : VARIABLE'''
    print("VARIABLES")

def p_error(p):
    if VERBOSE:
        if p is not None:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            print ("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
        else:
            print(chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print("\t\tLine:  "+str(ejerciciosT4.lexer.lineno))

    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)

        print(chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        parser.parse(scriptdata, tracking=False)
        #print("Hola bebe, no tienes errores sintacticos")
        print(chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print(chr(27)+"[0;31m"+"Pase el archivo de script PHP como parametro:")
        print(chr(27)+"[0;36m"+"\t$ python ejerciciosT5.py"+chr(27)+"[1;31m"+" prueba.dart"+chr(27)+"[0m")
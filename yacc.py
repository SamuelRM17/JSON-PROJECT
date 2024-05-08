import inspect
import ply.yacc as yacc
import ply.lex as lex  # Importa lex
from lex import tokens
import csv
import sys

def p_json(p):
    'json : LLAVE_IZQ elementos LLAVE_DER'
    p[0] = p[1] + p[2] + p[3]

def p_elementos_1(p):
    'elementos : par COMA elementos'
    p[0] = p[1] + p[2] + p[3]

def p_elementos_2(p):
    'elementos : par'
    p[0] = p[1]

def p_par_id(p):
    'par : ID DOSPUNTOS objeto'
    p[0] = p[1] + p[2] + p[3]

def p_par_name(p):
    'par : NAME DOSPUNTOS CADENA'
    p[0] = p[1] + p[2] + p[3]

def p_par_email(p):
    'par : EMAIL DOSPUNTOS CADENA'
    p[0] = p[1] + p[2] + p[3]

def p_par_movie_id(p):
    'par : MOVIE_ID DOSPUNTOS objeto'
    p[0] = p[1] + p[2] + p[3]

def p_par_text(p):
    'par : TEXT DOSPUNTOS CADENA'
    p[0] = p[1] + p[2] + p[3]

def p_par_date(p):
    'par : DATE DOSPUNTOS objeto'
    p[0] = p[1] + p[2] + p[3]

def p_par_id(p):
    'par : CADENA DOSPUNTOS objeto'
    p[0] = p[1] + p[2] + p[3]

def p_par_value(p):
    'par : CADENA DOSPUNTOS CADENA'
    p[0] = p[1] + p[2] + p[3]

def p_objeto_1(p):
    'objeto : LLAVE_IZQ par LLAVE_DER'
    p[0] = p[1] + p[2] + p[3]

def p_objeto_2(p):
    'objeto : LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DER'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_objeto_3(p):
    'objeto : LLAVE_IZQ DATE DOSPUNTOS LLAVE_IZQ NUMBERLONG DOSPUNTOS CADENA LLAVE_DER LLAVE_DER'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

parser = yacc.yacc()

with open('/Users/samuelromero/Desktop/LexYaccMiniProject/JSON/JSON-PROJECT/test.json', 'r') as file:
    contenido_archivo = file.read()

# Asegúrate de que lex.lexer está definido correctamente en el módulo lex
lex.lexer.input(contenido_archivo)

for tok in lex.lexer:
    print(tok)

# Analiza la entrada
resultado = parser.parse(contenido_archivo)
print(resultado)

rules = []
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isfunction(obj) and name.startswith('p_'):
        docstring = inspect.getdoc(obj)
        if docstring:
            rule, definition = docstring.split(' : ')
            rules.append({'rule': rule, 'definition': definition})


with open('grammar_rules.csv', 'w', newline='') as csvfile:
    fieldnames = ['rule', 'definition']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for rule in rules:
        writer.writerow(rule)
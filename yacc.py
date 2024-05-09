import inspect
import json
import ply.yacc as yacc
import ply.lex as lex  # Importa lex
from lex import tokens
import csv
import sys

def p_json(p):
    'json : CORCHETE_IZQ elementos CORCHETE_DER'
    p[0]= p[1] + p[2] + p[3]
#Esta es de la recursiva
def p_elementos_1(p):
    'elementos : LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DER COMA elementos'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10] + p[11] + p[12] + p[13] + p[14] + p[15]
#esta incluye nomas una
def p_elementos_2(p):
    'elementos : LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DER'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10] + p[11] + p[12] + p[13]

def p_ID(p):
    'p_ID : ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DER'
    p[0]= p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_name(p):
    'p_name : NAME DOSPUNTOS CADENA'
    p[0]= p[1] + p[2] + p[3]

def p_email(p):
    'p_email : EMAIL DOSPUNTOS CADENA'
    p[0]= p[1] + p[2] + p[3]

def p_movie_id(p):
    'p_movie_id : MOVIE_ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DER'
    p[0]= p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_text(p):
    'p_text : TEXT DOSPUNTOS CADENA'
    p[0]= p[1] + p[2] + p[3]

def p_date(p):
    'p_date : DATE DOSPUNTOS LLAVE_IZQ SDATE DOSPUNTOS LLAVE_IZQ NUMBERLONG DOSPUNTOS CADENA LLAVE_DER LLAVE_DER'
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9] + p[10] + p[11]

def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

parser = yacc.yacc()

with open('/Users/samuelromero/Desktop/LexYaccMiniProject/JSON/JSON-PROJECT/test.json', 'r') as file:
    contenido_archivo = file.read()

lex.lexer.input(contenido_archivo)

for tok in lex.lexer:
    print(tok)

resultado = parser.parse(contenido_archivo)
#print(resultado)

#Transformamos el resultado a un diccionario
data = json.loads(resultado)
print(data)


campos = [
    "_id",
    "name",
    "email",
    "movie_id",
    "text",
    "date"
]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=campos)

    writer.writeheader()

    for usuario in data:
        dic_usuario = {
            "_id": usuario["_id"]["$oid"],
            "name": usuario["name"],
            "email": usuario["email"],
            "movie_id": usuario["movie_id"]["$oid"],
            "text": usuario["text"],
            "date": usuario["date"]["$date"]["$numberLong"]
            
        }
        writer.writerow(dic_usuario)


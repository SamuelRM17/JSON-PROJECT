import ply.yacc as yacc
from lex import tokens
import lex
def p_html(p):
    'HTML : html CONTENT html_end'
    p[0] = p[1] + p[2] +p[3]
    print(p[0])

def p_content(p):
    'CONTENT : HEADER BODY'
    p[0] = p[1] + p[2]
    print(p[0])

def p_header(p):
    'HEADER : head TITLE head_end'
    p[0] = p[1] + p[2] +p[3]
    print(p[0])

def p_title(p):
    'TITLE : title TEXTO title_end'
    p[0] = p[1] + p[2] +p[3]

def p_body(p):
    'BODY : body H1 PARAGRAPH body_end'
    p[0] = p[1] + p[2] +p[3] +p[4]
    print(p[0])

def p_h1(p):
    'H1 : h1 TEXTO h1_end'
    p[0] = p[1] + p[2] +p[3]
    print(p[0])

    
def p_paragraph(p):
    'PARAGRAPH : p TEXTO p_end PARAGRAPH'
    p[0] = p[1] + p[2] + p[3]+ p[4]
    print(p[0])


def p_paragraph_2(p):
    'PARAGRAPH : '
    p[0] = ''
    print(p[0])


def p_text(p):
    'TEXTO : texto'
    p[0] = p[1]
    print(p[0])

def p_text1(p):
    'TEXTO : '
    p[0] = ''

def p_error(p):
    print("Syntax error in input!" + str(p))

parser = yacc.yacc()

with open('html/html_prueba2-1.html', 'r') as file:
    file_content = file.read()

lex.lexer.input(file_content)

for tok in lex.lexer:
    print(tok)

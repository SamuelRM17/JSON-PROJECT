import ply.yacc as yacc
from lex import tokens
import lex
def p_json(p):
    'JSON : OBJECT'
    p[0] = p[1]
    print(p[0])

def p_object(p):
    'OBJECT : LBRACE PAIR_LIST RBRACE'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_pair_list(p):
    'PAIR_LIST : PAIR COMMA PAIR_LIST'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_pair_list_single(p):
    'PAIR_LIST : PAIR'
    p[0] = p[1]
    print(p[0])

def p_pair(p):
    'PAIR : STRING COLON VALUE'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_value(p):
    '''VALUE : STRING
             | NUMBER
             | OBJECT
             | ARRAY
             | TRUE
             | FALSE
             | NULL'''
    p[0] = p[1]
    print(p[0])

def p_array(p):
    'ARRAY : LBRACKET ELEMENT_LIST RBRACKET'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_element_list(p):
    'ELEMENT_LIST : ELEMENT COMMA ELEMENT_LIST'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_element_list_single(p):
    'ELEMENT_LIST : ELEMENT'
    p[0] = p[1]
    print(p[0])

def p_element(p):
    'ELEMENT : VALUE'
    p[0] = p[1]
    print(p[0])

def p_string(p):
    'STRING : QUOTE CHAR_LIST QUOTE'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_char_list(p):
    'CHAR_LIST : CHAR CHAR_LIST'
    p[0] = p[1] + p[2]
    print(p[0])

def p_char_list_single(p):
    'CHAR_LIST : CHAR'
    p[0] = p[1]
    print(p[0])

def p_number(p):
    'NUMBER : INTEGER FRACTION EXPONENT'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_integer(p):
    '''INTEGER : DIGIT
               | DIGIT1_9 DIGITS'''
    p[0] = p[1]
    print(p[0])

def p_fraction(p):
    'FRACTION : DOT DIGITS'
    p[0] = p[1] + p[2]
    print(p[0])

def p_exponent(p):
    'EXPONENT : E SIGN DIGITS'
    p[0] = p[1] + p[2] + p[3]
    print(p[0])

def p_sign(p):
    '''SIGN : PLUS
            | MINUS'''
    p[0] = p[1]
    print(p[0])

def p_digits(p):
    'DIGITS : DIGIT DIGITS'
    p[0] = p[1] + p[2]
    print(p[0])

def p_digits_single(p):
    'DIGITS : DIGIT'
    p[0] = p[1]
    print(p[0])

def p_true(p):
    'TRUE : true'
    p[0] = p[1]
    print(p[0])

def p_false(p):
    'FALSE : false'
    p[0] = p[1]
    print(p[0])

def p_null(p):
    'NULL : null'
    p[0] = p[1]
    print(p[0])

def p_error(p):
    print("Syntax error in input!" + str(p))

parser = yacc.yacc()

with open('/Users/samuelromero/Desktop/LexYaccMiniProject/JSON/JSON-PROJECT/test.json', 'r') as file:
    file_content = file.read()

lex.lexer.input(file_content)

for tok in lex.lexer:
    print(tok)

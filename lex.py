import ply.lex as lex
tokens = (
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'COLON',
    'STRING',
    'NUMBER',
    'TRUE',
    'FALSE',
    'NULL'
)

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_COLON = r':'
t_STRING = r'"([^"\\]|\\.)*"'
t_NUMBER = r'-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?'
t_TRUE = r'true'
t_FALSE = r'false'
t_NULL = r'null'
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)


#ignoramos los tabs
t_ignore = '\t\n'

#cualquier token que no esté en los tokens definidos
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


# while input_str != '':
#     print('Para terminar introduce ENTER --- ')
#     input_str = input('Entrada a validar sintácticamente: ')

#     if input_str != '':
#         lexer.input(input_str)
        
#         for tok in lexer:
#             print(tok)


import ply.lex as lex

tokens = (
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'LLAVE_IZQ',
    'LLAVE_DER',
    'COMA',
    'DOSPUNTOS',
    'CADENA',
    'ID',
    'OID',
    'NAME',
    'EMAIL',
    'MOVIE_ID',
    'TEXT',
    'DATE',
    'NUMBERLONG',
    'SDATE'
)


t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r','
t_DOSPUNTOS = r':'
t_CADENA = r'"([^"\\]|\\.)*"'



def t_ID(t):
    r'"\_id"'
    return t

def t_OID(t):
    r'"\$oid"'
    return t

def t_NAME(t):
    r'"name"'
    return t

def t_EMAIL(t):
    r'"email"'
    return t

def t_MOVIE_ID(t):
    r'"movie_id"'
    return t

def t_TEXT(t):
    r'"text"'
    return t

def t_DATE(t):
    r'"date"'
    return t
def t_NUMBERLONG(t):
    r'"\$numberLong"'
    return t
def t_SDATE(t):
    r'"\$date"'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
import ply.lex as lex

tokens = (
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
    'NUMBERLONG'
)

t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r','
t_DOSPUNTOS = r':'
t_CADENA = r'"([^"\\]|\\.)*"'
t_ID = r'"\_id"'
t_OID = r'"\$oid"'
t_NAME = r'"name"'
t_EMAIL = r'"email"'
t_MOVIE_ID = r'"movie_id"'
t_TEXT = r'"text"'
t_DATE = r'"date"'
t_NUMBERLONG = r'"\$numberLong"'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
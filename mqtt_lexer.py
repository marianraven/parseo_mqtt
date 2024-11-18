import ply.lex as lex

# Lista de tokens
tokens = [
    'DISPOSITIVO',
    'MENSAJE',
    'A',
    'CON',
    'KEY',
    'ENCRIPTADO',
    'AUTH',
    'MQTT',
    'TOPIC',
    'CONECTAR',
    'DESCONECTAR',
    'PUBLICAR',
    'SUSCRIBIRSE',
    'DESUSCRIBIRSE',
    'VALOR',
    'TRUE',
    'FALSE'
]

# Expresiones regulares para tokens simples
t_A = r'A'
t_CON = r'CON'
t_KEY = r'KEY'
t_ENCRIPTADO = r'ENCRIPTADO'
t_AUTH = r'AUTH'
t_MQTT = r'MQTT'
t_CONECTAR = r'CONECTAR'
t_DESCONECTAR = r'DESCONECTAR'
t_PUBLICAR = r'PUBLICAR'
t_SUSCRIBIRSE = r'SUSCRIBIRSE'
t_DESUSCRIBIRSE = r'DESUSCRIBIRSE'
t_TOPIC = r'[tT][oO][pP][iI][cC]_[a-zA-Z0-9_]+'
t_TRUE = r'[tT][rR][uU][eE]'
t_FALSE = r'[fF][aA][lL][sS][eE]'

# Expresiones regulares más complejas
def t_DISPOSITIVO(t):
    r'[dD][iI][sS][pP][oO][sS][iI][tT][iI][vV][oO]_[a-zA-Z0-9]+'
    return t

def t_MENSAJE(t):
    r'[mM][eE][nN][sS][aA][jJ][eE]_[a-zA-Z0-9_]+'
    return t

# Manejo de valores entre comillas dobles
def t_VALOR(t):
    r'\"[^\"]*\"'
    return t

# Caracteres a ignorar
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

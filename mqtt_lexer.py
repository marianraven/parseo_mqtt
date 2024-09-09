import ply.lex as lex

# Definición de tokens iniciales
tokens = (
    'DISPOSITIVO', 'MENSAJE', 'ENVIAR', 'A', 'CON', 'KEY', 'VALOR',
    'ENCRIPTADO', 'AUTH', 'CONCURRENTE', 'COLA', 'MQTT', 'TOPIC',
    'CONECTAR', 'DESCONECTAR', 'PUBLICAR', 'SUSCRIBIRSE', 'DESUSCRIBIRSE'
)

# Expresiones regulares para los tokens
t_ENVIAR = r'enviar'
t_A = r'a'
t_CON = r'con'
t_KEY = r'key'
t_VALOR = r'\"[^\"]*\"'
t_ENCRIPTADO = r'encriptado'
t_AUTH = r'auth'
t_CONCURRENTE = r'concurrente'
t_COLA = r'cola'
t_MQTT = r'mqtt'
t_TOPIC = r'topic'
t_CONECTAR = r'conectar'
t_DESCONECTAR = r'desconectar'
t_PUBLICAR = r'publicar'
t_SUSCRIBIRSE = r'suscribirse'
t_DESUSCRIBIRSE = r'desuscribirse'
t_ignorar = ' \t'

def t_DEVICE(t):
    r'dispositivo_[0-9]+'
    return t

def t_MENSAJE(t):
    r'mensaje_[a-zA-Z_]+'
    return t

# Manejo errores léxicos
def t_error(t):
    print(f"Caracter ilegal '{t.valor[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
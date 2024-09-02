import ply.lex as lex

# Definición de tokens iniciales
tokens = (
    'DEVICE', 'MESSAGE', 'SEND', 'TO', 'WITH', 'KEY', 'VALUE',
    'ENCRYPT', 'AUTH', 'CONCURRENT', 'QUEUE', 'MQTT', 'TOPIC',
    'CONNECT', 'DISCONNECT', 'PUBLISH', 'SUBSCRIBE', 'UNSUBSCRIBE'
)

# Expresiones regulares para los tokens
t_SEND = r'send'
t_TO = r'to'
t_WITH = r'with'
t_KEY = r'key'
t_VALUE = r'\"[^\"]*\"'
t_ENCRYPT = r'encrypt'
t_AUTH = r'auth'
t_CONCURRENT = r'concurrent'
t_QUEUE = r'queue'
t_MQTT = r'mqtt'
t_TOPIC = r'topic'
t_CONNECT = r'connect'
t_DISCONNECT = r'disconnect'
t_PUBLISH = r'publish'
t_SUBSCRIBE = r'subscribe'
t_UNSUBSCRIBE = r'unsubscribe'
t_ignore = ' \t'

def t_DEVICE(t):
    r'device_[0-9]+'
    return t

def t_MESSAGE(t):
    r'message_[a-zA-Z_]+'
    return t

# Manejo errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()
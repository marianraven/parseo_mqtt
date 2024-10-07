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
   'QOS',
   'NUMERO',
   'VALOR',
   'VALOR_STRING',  # Token para valores entre comillas
   'TRUE',
   'FALSE'
]

# Expresiones regulares para tokens simples
t_A = r'(?i)a'
t_CON = r'(?i)con'
t_KEY = r'(?i)key'
t_ENCRIPTADO = r'(?i)encriptado'
t_AUTH = r'(?i)auth'
t_MQTT = r'(?i)mqtt'
t_CONECTAR = r'(?i)conectar'
t_DESCONECTAR = r'(?i)desconectar'
t_PUBLICAR = r'(?i)publicar'
t_SUSCRIBIRSE = r'(?i)suscribirse'
t_DESUSCRIBIRSE = r'(?i)desuscribirse'
t_QOS = r'(?i)qos'
t_TOPIC = r'(?i)topic_[a-zA-Z_0-9]+'
t_TRUE = r'(?i)true'
t_FALSE = r'(?i)false'

# Expresiones regulares más complejas
def t_DISPOSITIVO(t):
   r'(?i)dispositivo_[0-9]+'  # Maneja el formato de dispositivo y reconoce sensitive case
   return t

def t_MENSAJE(t):
   r'(?i)mensaje_[a-zA-Z0-9_]+'  # Permite letras y números
   return t

# Expresión regular para manejar valores entre comillas dobles
def t_VALOR_STRING(t):
   r'\"[^\"]*\"'  # Captura cualquier valor entre comillas dobles
   t.type = 'VALOR_STRING'  # Cambio el tipo a VALOR_STRING
   return t

# Expresión regular para manejar la palabra 'valor'
def t_VALOR(t):
   r'(?i)valor'  # Captura la palabra "valor"
   return t

# Expresión regular para manejar números(QoS)
def t_NUMERO(t):
   r'[0-9]+'  
   t.value = int(t.value)  # Convierto el valor a entero
   return t

# Función para manejar errores léxicos
def t_error(t):
   print(f"Error léxico: Caracter ilegal '{t.value[0]}'")
   t.lexer.skip(1)

# Caracteres a ignorar tabulaciones y espacios
t_ignore = ' \t'

# Definición de saltos de línea para el conteo de líneas
def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

# Construcción del lexer
lexer = lex.lex()
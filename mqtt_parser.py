import ply.yacc as yacc
from mqtt_lexer import tokens
from cryptography.fernet import Fernet #Encontre que esta librería me servía para la encriptacion de los mensajes

# Variables globales para manejar el estado de autenticación y encriptación
auth_required = False
username = ""
password = ""
encryption_enabled = False
qos_level = 0  # Valor predeterminado de QoS

# Clave y suite de encriptación
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

def p_programa(p):
   'programa : comandos'
   print("Programa analizado correctamente.")

def p_comandos(p):
   '''comandos : comando
               | comando comandos'''
   pass

def p_comando(p):
   '''comando : conectar
              | desconectar
              | publicar
              | suscribirse
              | desuscribirse
              | habilitar_encriptado
              | habilitar_auth
              | establecer_qos'''

def p_habilitar_encriptado(p):
   '''habilitar_encriptado : ENCRIPTADO A valor_booleano'''
   global encryption_enabled
   encryption_enabled = p[3]
   print(f"Encriptación habilitada: {encryption_enabled}")

def p_valor_booleano(p):
   '''valor_booleano : TRUE
                     | FALSE'''
   p[0] = (p[1].lower() == 'true')

def p_habilitar_auth(p):
   'habilitar_auth : AUTH VALOR_STRING VALOR_STRING'
   global username, password, auth_required
   username = p[2].strip('"')
   password = p[3].strip('"')
   auth_required = True
   print(f"Autenticación habilitada para usuario: {username}")

def p_establecer_qos(p):
   'establecer_qos : QOS NUMERO'
   global qos_level
   qos_level = p[2]
   print(f"Nivel de QoS establecido: {qos_level}")

def p_conectar(p):
   'conectar : CONECTAR MQTT DISPOSITIVO'
   print(f"Conectando a {p[3]}...")

def p_desconectar(p):
   'desconectar : DESCONECTAR MQTT DISPOSITIVO'
   print(f"Desconectando de {p[3]}...")

def p_publicar(p):
   'publicar : PUBLICAR MENSAJE A TOPIC CON KEY VALOR_STRING'
   global encryption_enabled, cipher_suite

   # Autenticación requerida
   if auth_required and not username:
       print("Error: Se requiere autenticación para publicar mensajes.")
       return

   mensaje = p[2]
   topic = p[4]
   key = p[6]

   # Si la encriptación está habilitada, encripta el mensaje
   if encryption_enabled:
       mensaje = cipher_suite.encrypt(mensaje.encode()).decode()  # Encripta el mensaje
       print(f"Mensaje encriptado: {mensaje}")

   print(f"Enviando mensaje {mensaje} a {topic} con clave {key} (QoS: {qos_level})...")

def p_suscribirse(p):
   'suscribirse : SUSCRIBIRSE A TOPIC'
   if auth_required and not username:
       print("Error: Se requiere autenticación para suscribirse a tópicos.")
   else:
       print(f"Suscribiéndose a {p[3]}... (QoS: {qos_level})")

def p_desuscribirse(p):
   'desuscribirse : DESUSCRIBIRSE A TOPIC'
   if auth_required and not username:
       print("Error: Se requiere autenticación para desuscribirse de tópicos.")
   else:
       print(f"Desuscribiéndose de {p[3]}... (QoS: {qos_level})")

def p_error(p):
   if p:
       print(f"Error de sintaxis en el token '{p.value}'")
   else:
       print("Error de sintaxis en EOF")

# Construcción del parser
parser = yacc.yacc()

def analizar(codigo):
   return parser.parse(codigo)

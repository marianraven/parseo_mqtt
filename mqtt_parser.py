import ply.yacc as yacc
from mqtt_lexer import tokens
from cryptography.fernet import Fernet #Encontre que esta librería me servía para la encriptacion de los mensajes


# Variables globales para manejar el estado de autenticación y encriptación
auth_required = False
username = ""
password = ""
encryption_enabled = False

# Clave y suite de encriptación
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

connected_devices = {}

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
               | habilitar_auth'''

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
    'habilitar_auth : AUTH VALOR VALOR'
    global username, password, auth_required
    username = p[2].strip('"')
    password = p[3].strip('"')
    auth_required = True
    print(f"Autenticación habilitada para usuario: {username}")

def p_conectar(p):
    'conectar : CONECTAR MQTT DISPOSITIVO'
    global connected_devices
    device_name = p[3]
    if device_name in connected_devices:
        print(f"Advertencia: {device_name} ya está conectado.")
    else:
        connected_devices[device_name] = True
        print(f"Conectando a {device_name}...")

def p_desconectar(p):
    'desconectar : DESCONECTAR MQTT DISPOSITIVO'
    device_name = p[3]
    if device_name in connected_devices:
        del connected_devices[device_name]
        print(f"Desconectando de {device_name}...")
    else:
        print(f"Advertencia: {device_name} no estaba conectado.")

def p_publicar(p):
    'publicar : PUBLICAR DISPOSITIVO MENSAJE A TOPIC CON KEY VALOR'
    global encryption_enabled, cipher_suite

    device_name = p[2]
    mensaje = p[3]
    topic = p[5]
    key = p[7]

    if device_name not in connected_devices:
        print(f"Error: El dispositivo {device_name} no está conectado.")
        return

    # Autenticación requerida
    if auth_required and not username:
        print("Error: Se requiere autenticación para publicar mensajes.")
        return

    # Si la encriptación está habilitada, encripta el mensaje
    if encryption_enabled:
        mensaje = cipher_suite.encrypt(mensaje.encode()).decode()
        print(f"Mensaje encriptado: {mensaje}")

    print(f"Dispositivo {device_name} publica el mensaje {mensaje} a {topic} con clave {key}")

def p_suscribirse(p):
    'suscribirse : SUSCRIBIRSE A TOPIC'
    if auth_required and not username:
        print("Error: Se requiere autenticación para suscribirse a tópicos.")
    else:
        print(f"Suscribiéndose a {p[3]}...")

def p_desuscribirse(p):
    'desuscribirse : DESUSCRIBIRSE A TOPIC'
    if auth_required and not username:
        print("Error: Se requiere autenticación para desuscribirse de tópicos.")
    else:
        print(f"Desuscribiéndose de {p[3]}...")

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

# Construcción del parser
parser = yacc.yacc()

def analizar(codigo):
    return parser.parse(codigo)

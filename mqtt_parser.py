import ply.yacc as yacc
from mqtt_lexer import tokens
from cryptography.fernet import Fernet

# Variables globales para manejar el estado de autenticación y encriptación
auth_required = False
username = ""
password = ""
encryption_enabled = False

# Clave y suite de encriptación
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

connected_devices = {}

# Diccionario para almacenar las credenciales de los dispositivos
device_credentials = {}

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

# Función para autenticar el dispositivo
def autenticar_dispositivo(device_name, device_username, device_password):
    global username, password
    if device_username == username and device_password == password:
        connected_devices[device_name] = True
        print(f"Dispositivo {device_name} autenticado correctamente.")
    else:
        print(f"Error: Credenciales incorrectas para el dispositivo {device_name}.")
        connected_devices[device_name] = False

def p_conectar(p):
    'conectar : CONECTAR MQTT DISPOSITIVO'
    global connected_devices, device_credentials
    device_name = p[3]
    if device_name in connected_devices:
        print(f"Advertencia: {device_name} ya está conectado.")
    else:
        connected_devices[device_name] = False  # Inicialmente no autenticado
        print(f"Conectando a {device_name}...")
        # Simulación de autenticación
        if auth_required:
            username_input = input(f"Ingrese usuario para {device_name}: ")
            password_input = input(f"Ingrese contraseña para {device_name}: ")
            autenticar_dispositivo(device_name, username_input, password_input)
        else:
            connected_devices[device_name] = True  # Autenticación no requerida
            print(f"Dispositivo {device_name} conectado sin autenticación.")

# Diccionario para almacenar las suscripciones de los dispositivos a los tópicos
topic_subscriptions = {}

def p_suscribirse(p):
    'suscribirse : SUSCRIBIRSE DISPOSITIVO A TOPIC'
    device_name = p[2]
    topic = p[4]

    if device_name not in connected_devices:
        print(f"Error: El dispositivo {device_name} no está conectado.")
        return

    # Verificar autenticación
    if auth_required and connected_devices[device_name] == False:
        print(f"Error: El dispositivo {device_name} no está autenticado. No puede suscribirse.")
        return

    # Registrar la suscripción al tópico
    if topic not in topic_subscriptions:
        topic_subscriptions[topic] = []
    topic_subscriptions[topic].append(device_name)
    print(f"Dispositivo {device_name} se suscribe al tópico {topic}.")
    
def p_publicar(p):
    'publicar : PUBLICAR DISPOSITIVO MENSAJE A TOPIC CON KEY VALOR'
    global encryption_enabled, cipher_suite

    device_name = p[2]
    mensaje = p[3]
    topic = p[5]
    key = p[7]

    if device_name not in connected_devices:
        print(f"Error: {device_name} no está conectado.")
        return

    # Verificar autenticación
    if auth_required and connected_devices[device_name] == False:
        print(f"Error: El dispositivo {device_name} no está autenticado. No puede publicar.")
        return

    # Si la encriptación está habilitada, encripta el mensaje
    if encryption_enabled:
        mensaje = cipher_suite.encrypt(mensaje.encode()).decode()
        print(f"Mensaje encriptado: {mensaje}")

    # Mostrar los dispositivos suscritos al tópico
    if topic in topic_subscriptions:
        suscriptores = topic_subscriptions[topic]
        print(f"Dispositivos suscritos a {topic}: {', '.join(suscriptores)}")
        print(f"Dispositivo {device_name} publica el mensaje {mensaje} a {topic} con clave {key}")
    else:
        print(f"No hay dispositivos suscritos al tópico {topic}.")



def p_desconectar(p):
    'desconectar : DESCONECTAR MQTT DISPOSITIVO'
    device_name = p[3]
    if device_name in connected_devices:
        del connected_devices[device_name]
        print(f"Desconectando de {device_name}...")
    else:
        print(f"Advertencia: {device_name} no estaba conectado.")

def p_desuscribirse(p):
    'desuscribirse : DESUSCRIBIRSE DISPOSITIVO A TOPIC'
    device_name = p[2]
    topic = p[4]
    if device_name not in connected_devices:
        print(f"Error: El dispositivo {device_name} no está conectado.")
    else:
        print(f"Dispositivo {device_name} se desuscribe del tópico {topic}.")

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

# Función para autenticar el dispositivo
def autenticar_dispositivo(device_name, device_username, device_password):
    global username, password
    if device_username == username and device_password == password:
        connected_devices[device_name] = True
        print(f"Dispositivo {device_name} autenticado correctamente.")
    else:
        print(f"Error: Credenciales incorrectas para el dispositivo {device_name}.")
        connected_devices[device_name] = False

# Construcción del parser
parser = yacc.yacc()

def analizar(codigo):
    return parser.parse(codigo)
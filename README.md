# Proyecto MQTT-Lenguaje

## Descripción

Bienvenido al proyecto **MQTT-Lenguaje**, un lenguaje de programación especializado en interactuar con el protocolo MQTT. 
Este lenguaje facilita la comunicación entre dispositivos IoT mediante una sintaxis simple y directa, permitiendo la declaración de variables, suscripciones a tópicos, publicaciones de mensajes, el uso de estructuras condicionales básicas e iteraciones.

El proyecto está implementado en Python, utilizando la biblioteca PLY (Python Lex-Yacc) para el análisis léxico y sintáctico.

## Características del Lenguaje

- **Declaración de Variables:** Se pueden declarar variables y asignarles valores, lo que permite manejar datos.
- **Suscripciones a Tópicos:** Facilita la suscripción a tópicos específicos para recibir mensajes automáticamente cuando estos son publicados.
- **Publicación de Mensajes:** Permite publicar mensajes en tópicos, enviando datos entre diferentes dispositivos o servicios conectados al broker MQTT.
- **Condicionales Básicos :** Incluye estructuras condicionales para controlar el flujo del programa basándose en el contenido de los mensajes.
- **Iteraciones:** Implementa bucles para repetir acciones múltiples veces, lo que permite un control más detallado sobre la ejecución del código y la automatización de tareas repetitivas.
- **Extensibilidad:** El lenguaje está diseñado para ser fácilmente ampliable, permitiendo la inclusión de más características en futuras versiones.

## Estructura del Proyecto
## mqtt_lexer.py 
Este archivo contiene el analizador léxico (lexer), responsable de definir y reconocer los tokens del lenguaje, tales como palabras clave, operadores y símbolos.
## mqtt_parser.py
Aquí se define el analizador sintáctico (parser), que especifica la gramática del lenguaje y construye el árbol de sintaxis a partir de los tokens identificados por el lexer.
## main.py
Es el archivo principal del proyecto, utilizado para probar el funcionamiento del lexer y el parser con ejemplos de código escritos en MQTT-Lenguaje.
## test
Archivo/s destinado/s a pruebas automatizadas para validar el funcionamiento correcto del lexer, el parser y las nuevas funcionalidades.

## Instalación y Uso

Para comenzar a utilizar MQTT-Lenguaje, sigue estos pasos:

1. **Clona el repositorio desde GitHub:**

    ```bash
    git clone https://github.com/marianraven/parseo_mqtt.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd mqtt-lenguaje
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip3 install ply
    ```

4. **Ejecuta el archivo principal para probar el lenguaje:**

    ```bash
    python3 main.py
    ```
## Especificaciones

## Definición de Tokens en el Lexer

A continuación se proporciona una explicación detallada de cada token definido en el archivo `lexer.py`, junto con sus expresiones regulares y su propósito en el análisis léxico del lenguaje basado en MQTT.

## Definición de Tokens

**DEVICE**  
- **Expresión Regular**: `r'device_[0-9]+'`  
- **Descripción**: Coincide con identificadores de dispositivos en el formato `device_<número>`, donde `<número>` es una secuencia de dígitos.  
- **Ejemplo**: `device_01`

**MESSAGE**  
- **Expresión Regular**: `r'message_[a-zA-Z_]+'`  
- **Descripción**: Coincide con identificadores de mensajes en el formato `message_<cadena>`, donde `<cadena>` es una secuencia de letras o guiones bajos.  
- **Ejemplo**: `message_alert`

**SEND**  
- **Expresión Regular**: `r'send'`  
- **Descripción**: Coincide con la palabra clave `send`. Se usa para indicar una operación de envío de datos en el lenguaje.

**TO**  
- **Expresión Regular**: `r'to'`  
- **Descripción**: Coincide con la palabra clave `to`. Se usa para especificar el destino en las operaciones.

**WITH**  
- **Expresión Regular**: `r'with'`  
- **Descripción**: Coincide con la palabra clave `with`. Se usa para indicar el uso de una clave o valor asociado en las operaciones.

**KEY**  
- **Expresión Regular**: `r'key'`  
- **Descripción**: Coincide con la palabra clave `key`. Se usa para especificar que el siguiente valor es una clave.

**VALUE**  
- **Expresión Regular**: `r'\"[^\"]*\"'`  
- **Descripción**: Coincide con un valor entre comillas dobles. Permite capturar cualquier texto dentro de comillas.  
- **Ejemplo**: `"mysecretkey"`

**ENCRYPT**  
- **Expresión Regular**: `r'encrypt'`  
- **Descripción**: Coincide con la palabra clave `encrypt`. Se usa para indicar una operación de cifrado de datos.

**AUTH**  
- **Expresión Regular**: `r'auth'`  
- **Descripción**: Coincide con la palabra clave `auth`. Se usa para indicar una operación de autenticación.

**CONCURRENT**  
- **Expresión Regular**: `r'concurrent'`  
- **Descripción**: Coincide con la palabra clave `concurrent`. Se usa para indicar que una operación se realizará de manera concurrente.

**QUEUE**  
- **Expresión Regular**: `r'queue'`  
- **Descripción**: Coincide con la palabra clave `queue`. Se usa para indicar que un mensaje se añadirá a una cola.

**MQTT**  
- **Expresión Regular**: `r'mqtt'`  
- **Descripción**: Coincide con la palabra clave `mqtt`. Se usa para especificar que la operación se refiere al protocolo MQTT.

**TOPIC**  
- **Expresión Regular**: `r'topic'`  
- **Descripción**: Coincide con la palabra clave `topic`. Se usa para especificar el tópico en las operaciones MQTT.

**CONNECT**  
- **Expresión Regular**: `r'connect'`  
- **Descripción**: Coincide con la palabra clave `connect`. Se usa para indicar una operación de conexión a un dispositivo.

**DISCONNECT**  
- **Expresión Regular**: `r'disconnect'`  
- **Descripción**: Coincide con la palabra clave `disconnect`. Se usa para indicar una operación de desconexión de un dispositivo.

**PUBLISH**  
- **Expresión Regular**: `r'publish'`  
- **Descripción**: Coincide con la palabra clave `publish`. Se usa para indicar una operación de publicación de un mensaje.

**SUBSCRIBE**  
- **Expresión Regular**: `r'subscribe'`  
- **Descripción**: Coincide con la palabra clave `subscribe`. Se usa para indicar una operación de suscripción a un tópico.

**UNSUBSCRIBE**  
- **Expresión Regular**: `r'unsubscribe'`  
- **Descripción**: Coincide con la palabra clave `unsubscribe`. Se usa para indicar una operación de desuscripción de un tópico.

**t_ignore**  
- **Valor**: `' \t'`  
- **Descripción**: Especifica los caracteres que deben ser ignorados durante el análisis léxico. En este caso, se ignoran los espacios en blanco y tabulaciones.

## Funciones del Lexer

**t_error**  
- **Descripción**: Maneja errores léxicos. Imprime un mensaje de error cuando se encuentra un carácter no permitido y omite ese carácter para continuar el análisis.

**t_DEVICE y t_MESSAGE**  
- **Descripción**: Definen cómo se deben reconocer los tokens `DEVICE` y `MESSAGE`, respectivamente, utilizando expresiones regulares personalizadas.

## Construcción del Lexer

**lex.lex()**  
- **Descripción**: Construye el analizador léxico (`lexer`) utilizando las definiciones de tokens y reglas proporcionadas. El analizador léxico escaneará el texto de entrada y generará tokens basados en las expresiones regulares definidas.

## Gramáticas
Las gramáticas determinan cómo se deben estructurar las sentencias del lenguaje. 

Algunas producciones básicas:

Programa es un conjunto de declaraciones y comandos.

programa : comandos
Comandos: pueden incluir operaciones como conectar, desconectar, enviar mensajes, suscribirse, etc.

comandos : comando
         | comando comandos

Comando: una acción que el dispositivo puede realizar.

comando : conectar
        | desconectar
        | enviar_mensaje
        | suscribirse
        | desuscribirse

Conectar: iniciar una conexión MQTT.
conectar : CONNECT MQTT DEVICE
Desconectar: terminar una conexión MQTT.

desconectar : DISCONNECT MQTT DEVICE
Enviar Mensaje: enviar un mensaje a un tópico específico.

enviar_mensaje : SEND MESSAGE TO TOPIC WITH KEY VALUE
Suscribirse: suscribirse a un tópico para recibir mensajes.

suscribirse : SUBSCRIBE TO TOPIC
Desuscribirse: desuscribirse de un tópico.

desuscribirse : UNSUBSCRIBE FROM TOPIC
Estas producciones permiten manejar operaciones básicas como conectarse, desconectarse, enviar mensajes, y gestionar suscripciones.

Operaciones Permitidas con el Lenguaje
Conectar a un Broker MQTT: Permite establecer una conexión con un servidor MQTT para enviar y recibir mensajes.

Desconectar del Broker MQTT: Permite finalizar la conexión activa con el servidor MQTT.

Enviar Mensajes: Enviar mensajes a un tópico específico usando ciertos parámetros como claves y valores.

Suscribirse y Desuscribirse a Tópicos: Permite recibir mensajes de ciertos tópicos y dejar de recibir mensajes de otros.

Palabras válidas de entrada
CONNECT, DISCONNECT, SEND, TO, WITH, KEY, VALUE, UNSUBSCRIBE, MQTT, DEVICE, MESSAGE, TOPIC, QUEUE, CONCURRENT, ENCRYPT, AUTH

## Ejemplos de Programas

### Conectar a un dispositivo MQTT
CONNECT MQTT device_1

### Enviar un mensaje a un tópico
SEND message_hello TO topic_home WITH key "greeting" value "Hello World"

### Suscribirse a un tópico
CONNECT MQTT device_1
SUBSCRIBE TO topic_home

### Desconectar después de enviar un mensaje
CONNECT MQTT device_1
SEND message_update TO topic_home WITH key "status" value "updated"
DISCONNECT MQTT device_1

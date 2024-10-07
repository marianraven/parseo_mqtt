# Proyecto MQTT-Lenguaje

## Descripción

Bienvenido al proyecto **MQTT-Lenguaje**, un lenguaje de programación especializado en interactuar con el protocolo MQTT. 
Este lenguaje facilita la comunicación entre dispositivos IoT mediante una sintaxis simple y directa, permitiendo la declaración de variables, suscripciones a tópicos, publicaciones de mensajes, el uso de estructuras condicionales básicas e iteraciones.

![Escenario MQTT](https://github.com/user-attachments/assets/8ce8fa98-cbf1-4ec0-b2df-6764e2fffd93)

El proyecto está implementado en Python, utilizando la biblioteca PLY (Python Lex-Yacc) para el análisis léxico y sintáctico.
Link al blog para más especificaciones: https://www.hivemq.com/blog/mqtt-packets-comprehensive-guide/

## Características del Lenguaje

- **Declaración de Variables:**  Permite declarar variables y asignarles valores.
- **Suscripciones a Topics:** Facilita la suscripción a tópicos específicos para recibir mensajes automáticamente cuando estos son publicados.
- **Publicación de Mensajes:** Permite publicar mensajes en tópicos, enviando datos entre diferentes dispositivos o servicios conectados al broker MQTT.
- **Condicionales Básicos :** Incluye estructuras condicionales para controlar el flujo del programa.
- **Iteraciones:** Implementa bucles para repetir acciones múltiples veces, lo que permite un control más detallado sobre la ejecución del código y la automatización de tareas repetitivas.
- **Extensibilidad:** El lenguaje está diseñado para ser fácilmente ampliable, permitiendo la inclusión de más características en futuras versiones.

## Estructura del Proyecto
## mqtt_lexer.py 
Contiene el analizador léxico (lexer), responsable de definir y reconocer los tokens del lenguaje.
## mqtt_parser.py
Define el analizador sintáctico (parser), que especifica la gramática del lenguaje y construye el árbol de sintaxis a partir de los tokens identificados por el lexer.
## main.py
Es el archivo principal del proyecto, utilizado para probar el funcionamiento del lexer y el parser(tiene asociado el archivo entrada.txt, aunque finalmente decidi poner archivos de test más exaustivos).
## test1 y test2_complejos
Archivos destinados a pruebas automatizadas para validar el funcionamiento del lexer, parser y nuevas funcionalidades

## Instalación y Uso

Para comenzar a utilizar MQTT-Lenguaje, sigue estos pasos:

1. **Clona el repositorio desde GitHub:**

    ```bash
    git clone https://github.com/marianraven/parseo_mqtt.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd parseo_mqtt
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip3 install ply
    pip3 install cryptography

    ```

4. **Ejecuta el archivo principal para probar el lenguaje:**

    ```bash
    python3 main.py 
    python3 test1.py
    python3 test2_complejos
    ```
# Especificaciones

## Definición de Tokens en el Lexer
A continuación se proporciona una explicación detallada de cada token definido en el archivo `lexer.py`, junto con sus expresiones regulares y su propósito.

### Definición de Tokens

#### DISPOSITIVO
- **Expresión Regular**: `r'dispositivo_[0-9]+'`
- **Descripción**: Coincide con identificadores en el formato `dispositivo_<número>`.
- **Ejemplo**: `dispositivo_01`

#### MENSAJE
- **Expresión Regular**: `r'mensaje_[a-zA-Z_]+'`
- **Descripción**: Coincide con identificadores en el formato `mensaje_<cadena>`.
- **Ejemplo**: `mensaje_alerta`

#### PUBLICAR
- **Expresión Regular**: `r'publicar'`
- **Descripción**: Indica una operación de envío de datos.

#### A
- **Expresión Regular**: `r'a'`
- **Descripción**: Especifica el destino en las operaciones.

#### CON
- **Expresión Regular**: `r'con'`
- **Descripción**: Indica el uso de una clave o valor asociado.

#### KEY
- **Expresión Regular**: `r'key'`
- **Descripción**: Especifica que el siguiente valor es una clave.

#### VALOR
- **Expresión Regular**: `r'\"[^\"]*\"'`
- **Descripción**: Captura cualquier texto dentro de comillas.
- **Ejemplo**: `"mysecretkey"`

#### ENCRIPTADO
- **Expresión Regular**: `r'encriptado'`
- **Descripción**: Indica una operación de cifrado.

#### AUTH
- **Expresión Regular**: `r'auth'`
- **Descripción**: Indica una operación de autenticación.

#### MQTT
- **Expresión Regular**: `r'mqtt'`
- **Descripción**: Se refiere al protocolo MQTT.

#### TOPIC
- **Expresión Regular**: `r'topic'`
- **Descripción**: Especifica el tópico en las operaciones.

#### CONECTAR
- **Expresión Regular**: `r'(?i)conectar'`
- **Descripción**: Indica una operación de conexión.

#### DESCONECTAR
- **Expresión Regular**: `r'(?i)desconectar'`
- **Descripción**: Indica una operación de desconexión.

#### SUSCRIBIRSE
- **Expresión Regular**: `r'suscribirse'`
- **Descripción**: Indica una operación de suscripción.

#### DESUSCRIBIRSE
- **Expresión Regular**: `r'desuscribirse'`
- **Descripción**: Indica una operación de desuscripción.

#### t_ignore
- **Valor**: `' \t'`
- **Descripción**: Especifica caracteres que se ignoran durante el análisis.

## Funciones del Lexer
- `t_error`: Maneja errores léxicos y omite caracteres no permitidos.
- `t_DISPOSITIVO` y `t_MENSAJE`: Definen cómo se reconocen los tokens DISPOSITIVO y MENSAJE.

## Construcción del Lexer
- `lex.lex()`: Construye el analizador léxico utilizando las definiciones de tokens y reglas.

## Gramáticas
Las gramáticas determinan cómo se deben estructurar las sentencias del lenguaje. 

Algunas producciones básicas:

Programa es un conjunto de declaraciones y comandos.


```plaintext
<programa> ::= <comandos>

<comandos> ::= <comando> | <comando> <comandos> 

<comando> ::= <conectar> | <desconectar> | <publicar> | <suscribirse> | <desuscribirse> 

<conectar> ::= CONECTAR MQTT <dispositivo> 

<desconectar> ::= DESCONECTAR MQTT <dispositivo> 

<publicar> ::= PUBLICAR <mensaje> A <topic> CON KEY <valor_string> VALOR <valor>  

<suscribirse> ::= SUSCRIBIRSE A <topic> 

<desuscribirse> ::= DESUSCRIBIRSE A <topic> 

<encriptar> ::= ENCRIPTADO KEY <key> VALOR <valor> 

<auth> ::= AUTH <dispositivo> VALOR <valor> 

<qos> ::= QOS <numero>

```

Estas producciones permiten manejar operaciones básicas como conectarse, desconectarse y publicar mensajes, así como realizar operaciones de cifrado y autenticación.

## Operaciones Permitidas con el Lenguaje
- **Conectar a un Broker MQTT**: Establece una conexión con un servidor MQTT.
- **Desconectar del Broker MQTT**: Finaliza la conexión activa.
- **Publicar Mensajes**: Envía mensajes a un tópico específico.
- **Suscribirse y Desuscribirse a Tópicos**: Permite recibir o dejar de recibir mensajes de tópicos.
- **Encriptar Valores**: Cifra información antes de ser enviada.
- **Autenticación**: Verifica la identidad del dispositivo que se conecta.

## Palabras válidas de entrada
CONECTAR, DESCONECTAR, PUBLICAR, A, CON, KEY, VALOR, DESUSCRIBIRSE, MQTT, DISPOSITIVO, MENSAJE, TOPIC, ENCRIPTADO, AUTH, QOS

## Ejemplos de Programas
Conectar a un dispositivo MQTT**

 ```
CONECTAR MQTT dispositivo_1
 ```

Publicar un mensaje a un tópico


```
PUBLICAR mensaje_hola A topic_casa CON KEY "valor_secreto"
```
Suscribirse a un tópico(del dispositivo ya conectado anteriormente)

```
CONECTAR MQTT dispositivo_1
SUSCRIBIRSE A topic_casa
```
Desconectar después de publicar un mensaje

```
CONECTAR MQTT dispositivo_1
PUBLICAR mensaje_update A topic_casa CON KEY "valor_actualizado"
DESCONECTAR MQTT dispositivo_1
```
Encriptar un valor

```
ENCRIPTADO KEY "clave_secreta" VALOR "dato_confidencial"
```
Autenticarse en un dispositivo

```
AUTH dispositivo_1
```
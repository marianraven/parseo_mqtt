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
Es el archivo principal del proyecto, utilizado para probar el funcionamiento del lexer y el parser(tiene asociado el archivo entrada.txt, se podría cambiar a entrada1.txt).
## entrada.txt y entrada1.txt
Archivos de programas destinados a pruebas automatizadas para validar el funcionamiento del lexer, parser y nuevas funcionalidades.
## Archivos generados automáticamente por PLY: `parser.out` y `parsertab.py`

Cuando utilizamos la librería **PLY** (Python Lex-Yacc) para crear el analizador léxico y sintáctico, se generan automáticamente dos archivos: `parser.out` y `parsertab.py`. Estos archivos son necesarios para el funcionamiento del analizador pero no deben ser editados manualmente.

---

### Método de análisis: LALR
El método **LALR** (*Look-Ahead LR*) es un tipo de análisis sintáctico utilizado por el analizador generado. Este método:
- Combina las ventajas de los métodos **SLR** y **LR**.
- Es eficiente tanto en memoria como en tiempo de procesamiento.
- Es ideal para lenguajes de programación y lenguajes específicos como MQTT.

---

### `parser.out`
Este archivo:
- Es un registro detallado del análisis sintáctico generado a partir de la gramática definida en el código fuente.
- Contiene:
  - **Reglas de gramática** con sus correspondientes acciones o funciones en Python.
  - **Estados del parser** y cómo cada uno responde a los diferentes tokens.
  - **Conflictos** o ambigüedades en la gramática (si las hubiese).
- Es útil para depurar el diseño de la gramática del lenguaje.

---

### `parsertab.py`
Este archivo:
- Contiene las **estructuras internas** necesarias para que el analizador funcione:
  - Tablas de **acciones** para decidir cómo manejar cada token.
  - Tablas de **transiciones** entre estados (usadas al reconocer no terminales).
  - Definiciones de las **producciones de la gramática** y sus componentes.
- Es generado automáticamente y no se modifica directamente.
- Actúa como una base técnica para que el analizador interprete correctamente las reglas del lenguaje.

---



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
    ```
# Especificaciones

## Definición de Tokens en el Lexer
A continuación se proporciona una explicación detallada de cada token definido en el archivo `lexer.py`, junto con sus expresiones regulares y su propósito.

### Definición de Tokens

| **Token**           | **Expresión Regular**                | **Descripción**                                           | **Ejemplo**          |
|---------------------|--------------------------------------|-----------------------------------------------------------|-----------------------|
| **DISPOSITIVO**     | `r'[dD][iI][sS][pP][oO][sS][iI][tT][iI][vV][oO]_[a-zA-Z0-9]+'` | Coincide con identificadores en el formato `dispositivo_<valor>`. | `dispositivo_01`     |
| **MENSAJE**         | `r'[mM][eE][nN][sS][aA][jJ][eE]_[a-zA-Z0-9_]+'` | Coincide con identificadores en el formato `mensaje_<valor>`. | `mensaje_alerta1`    |
| **PUBLICAR**        | `r'(?i)publicar'`                   | Indica una operación de envío de datos (insensible al caso). | `Publicar`           |
| **A**               | `r'a'`                              | Especifica el destino en las operaciones.                 | `a`                  |
| **CON**             | `r'con'`                            | Indica el uso de una clave o valor asociado.              | `con`                |
| **KEY**             | `r'key'`                            | Especifica que el siguiente valor es una clave.           | `key`                |
| **VALOR**           | `r'\"[^\"]*\"'`                     | Captura cualquier texto dentro de comillas.               | `"textovalor"`      |
| **ENCRIPTADO**      | `r'encriptado'`                     | Indica una operación de cifrado.                          | `encriptado`         |
| **AUTH**            | `r'auth'`                           | Indica una operación de autenticación.                    | `auth`               |
| **MQTT**            | `r'mqtt'`                           | Se refiere al protocolo MQTT.                             | `mqtt`               |
| **TOPIC**           | `r'[tT][oO][pP][iI][cC]_[a-zA-Z0-9_]+'` | Especifica el tópico en las operaciones.                  | `Topic_sensores`     |
| **CONECTAR**        | `r'(?i)conectar'`                   | Indica una operación de conexión al broker.    | `Conectar`           |
| **DESCONECTAR**     | `r'(?i)desconectar'`                | Indica una operación de desconexión al broker. | `Desconectar`        |
| **SUSCRIBIRSE**     | `r'suscribirse'`                    | Indica una operación de suscripción a un topic.                      | `suscribirse`        |
| **DESUSCRIBIRSE**   | `r'desuscribirse'`                  | Indica una operación de desuscripción a un topic.                    | `desuscribirse`      |
| **TRUE**            | `r'(?i)true'`                       | Representa un valor booleano verdadero.                   | `True`               |
| **FALSE**           | `r'(?i)false'`                      | Representa un valor booleano falso.                       | `False`              |

## Funciones del Lexer
- `t_ignore`: Especifica caracteres que se ignoran durante el análisis.
- `t_error`: Maneja errores léxicos y omite caracteres no permitidos.
- `t_DISPOSITIVO` y `t_MENSAJE`: Definen cómo se reconocen los tokens DISPOSITIVO y MENSAJE.


## Construcción del Lexer
- `lex.lex()`: Construye el analizador léxico utilizando las definiciones de tokens y reglas.

## Gramática
En términos generales, las gramáticas determinan cómo se deben estructurar las sentencias del lenguaje. De este modo, se realiza el manejo estructurado de lo que está permitido.

### Gramática del lenguaje MQTT

En esta gramatica se pueden apreciar las sigueintes sentencias:

Programa es un conjunto de declaraciones y comandos.


```plaintext
<programa> ::= <comandos>

<comandos> ::= <comando> | <comando> <comandos> 

<comando> ::= <conectar> | <desconectar> | <publicar> | <suscribirse> | <desuscribirse> 

<conectar> ::= CONECTAR MQTT <dispositivo> 

<desconectar> ::= DESCONECTAR MQTT <dispositivo> 

<publicar> ::= PUBLICAR <dispositivo> <mensaje> A <topic> CON KEY <valor>   

<suscribirse> ::= SUSCRIBIRSE A <topic> 

<desuscribirse> ::= DESUSCRIBIRSE A <topic> 

<encriptar> ::= ENCRIPTADO TRUE | ENCRIPTADO FALSE 

<auth> ::= AUTH <valor> <valor> 

```

Estas producciones permiten manejar operaciones básicas como conectarse, desconectarse y publicar mensajes, así como realizar operaciones de cifrado y autenticación.

## Operaciones Permitidas con el Lenguaje
- **Conectar a un Broker MQTT**: Establece una conexión con un servidor MQTT.
- **Desconectar del Broker MQTT**: Finaliza la conexión activa.
- **Publicar Mensajes**: Envía mensajes desde un dispositivo a un tópico específico.
- **Suscribirse y Desuscribirse a Tópicos**: Permite recibir o dejar de recibir mensajes de tópicos.
- **Encriptar Valores**: Cifra información antes de ser enviada.
- **Autenticación**: Verifica la identidad del dispositivo que se conecta.

## Palabras válidas de entrada
CONECTAR, DESCONECTAR, PUBLICAR, A, CON, KEY, VALOR, DESUSCRIBIRSE, MQTT, DISPOSITIVO, MENSAJE, TOPIC, ENCRIPTADO, AUTH, TRUE, FALSE.

## Ejemplos de Programas
Conectar a un dispositivo MQTT**

 ```
CONECTAR MQTT dispositivo_SensorTemperatura
 ```

Publicar un mensaje a un tópico


```
PUBLICAR dispositivo_SensorTemperatura mensaje_humedad55 A topic_temperatura CON KEY "claveprivada"
```
Suscribirse a un tópico(del dispositivo ya conectado anteriormente)

```
CONECTAR MQTT dispositivo_SensorTemperatura
SUSCRIBIRSE dispositivo_SensorTemperatura A topic_temperatura
```
Desconectar después de publicar un mensaje

```
DESCONECTAR MQTT dispositivo_SensorTemperatura
```
Encriptar un valor

```
ENCRIPTADO TRUE
```
Autenticarse en un dispositivo

```
AUTH "admin" "admin123"
```
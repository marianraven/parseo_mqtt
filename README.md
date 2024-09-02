# Proyecto MQTT-Lenguaje

## Descripción

Bienvenido al proyecto **MQTT-Lenguaje**, un lenguaje de programación especializado en interactuar con el protocolo MQTT. 
Este lenguaje facilita la comunicación entre dispositivos IoT mediante una sintaxis simple y directa, permitiendo la declaración de variables, suscripciones a tópicos, publicaciones de mensajes, el uso de estructuras condicionales básicas e iteraciones.

El proyecto está implementado en Python, utilizando la biblioteca PLY (Python Lex-Yacc) para el análisis léxico y sintáctico.

## Características del Lenguaje

- **Declaración de Variables:** Se pueden declarar variables y asignarles valores, lo que permite manejar datos.
- **Suscripciones a Tópicos:** Facilita la suscripción a tópicos específicos para recibir mensajes automáticamente cuando estos son publicados.
- **Publicación de Mensajes:** Permite publicar mensajes en tópicos, enviando datos entre diferentes dispositivos o servicios conectados al broker MQTT.
- **Condicionales Básicos (`if-else`):** Incluye estructuras condicionales para controlar el flujo del programa basándose en el contenido de los mensajes.
- **Iteraciones (`for` y `while`):** Implementa bucles para repetir acciones múltiples veces, lo que permite un control más detallado sobre la ejecución del código y la automatización de tareas repetitivas.
- **Extensibilidad:** El lenguaje está diseñado para ser fácilmente ampliable, permitiendo la inclusión de más características en futuras versiones.

## Estructura del Proyecto
# mqtt_lexer.py 
Este archivo contiene el analizador léxico (lexer), responsable de definir y reconocer los tokens del lenguaje, tales como palabras clave, operadores y símbolos.
# mqtt_parser.py
Aquí se define el analizador sintáctico (parser), que especifica la gramática del lenguaje y construye el árbol de sintaxis abstracta (AST) a partir de los tokens identificados por el lexer.
# main.py
Es el archivo principal del proyecto, utilizado para probar el funcionamiento del lexer y el parser con ejemplos de código escritos en MQTT-Lenguaje.
# tests
Un directorio destinado a pruebas automatizadas para validar el funcionamiento correcto del lexer, el parser y las nuevas funcionalidades.

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
    pip install ply
    ```

4. **Ejecuta el archivo principal para probar el lenguaje:**

    ```bash
    python main.py
    ```
